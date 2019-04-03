from point import Point
from grid import Grid
import simplejson as json
import pickle
from math import log10

def get_all_scores(route_points,grid_file,radius):
    """
    Takes in route points, and the file for the grid object. Returns a list of tuples (lat,lon,score) for every point on the route
    """
    #parse the string of list of lists into a list of points
    from_js_route_pts = json.loads(route_points)
    from_js_route_pts = [str_to_point(s) for s in from_js_route_pts]

    #import the grid 2d list here
    #grid = Grid(33.707, 34.3343, -118.1554, -118.6661, 0.01, grid_file)
    grid = Grid(pickle_file_name = grid_file)

    #get scores for each entry of route_points
    lat_lon_scores = []
    for i in range(0,len(from_js_route_pts)):
        curr_route_point = from_js_route_pts[i]
        lat_lon_scores.append([curr_route_point.get_lat(),curr_route_point.get_lon(),grid.get_score(curr_route_point, radius)])
    max_score = get_min_max_scores(grid_file, radius)
    normalized = normalize_scores(lat_lon_scores, max_score)
    return normalized

def get_min_max_scores(grid_file, radius):
    grid_obj = Grid(pickle_file_name = grid_file)
    if (grid_obj.max_score is not None):
        return grid_obj.max_score
    else:
        grid = grid_obj.get_grid()
        max_score = float('-inf')

        temp=[]
        for y in range(0,len(grid)):
            for x in range(0, len(grid[0])):
                for p in grid[y][x]:
                    curr_pt_score = grid_obj.get_score(p,radius)
                    temp.append(curr_pt_score)
                    max_score = max(max_score, curr_pt_score)

        #update grid object with max, min scores and repickle
        grid_obj.max_score = max_score
        pickle.dump(grid_obj, open(grid_file, "wb" ))
        return max_score

def normalize_scores(lat_lon_scores, max_score):
    normalized_scores = [[score[0], score[1], score[2]/(max_score/2)] for score in lat_lon_scores]
    normalized_scores = [[score[0],score[1],0.999] if score[2]>=1 else score for score in normalized_scores ]
    return normalized_scores

def str_to_point(route_string):
    route_lat_lon_list = route_string.split(" ")
    lat = float(route_lat_lon_list[0])
    lon = float(route_lat_lon_list[1])
    point_object = Point(lat,lon)
    return point_object
