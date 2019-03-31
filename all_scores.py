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
    #print(from_js_route_pts)

    #import the grid 2d list here
    #grid = Grid(33.707, 34.3343, -118.1554, -118.6661, 0.01, grid_file)
    grid = Grid(pickle_file_name = grid_file)

    #get scores for each entry of route_points
    lat_lon_scores = []
    for i in range(0,len(from_js_route_pts)):
        curr_route_point = from_js_route_pts[i]
        lat_lon_scores.append([curr_route_point.get_lat(),curr_route_point.get_lon(),grid.get_score(curr_route_point, radius)])
    #print([scores[2] for scores in lat_lon_scores])
    min_score, max_score = get_min_max_scores(grid_file, radius)
    #print(min_score)
    #print(max_score)
    normalized = normalize_scores(lat_lon_scores, min_score, max_score)
    #print(normalized)
    #print(lon_lat_score
    #return lat_lon_scores
    return normalized

def get_min_max_scores(grid_file, radius):
    grid_obj = Grid(pickle_file_name = grid_file)
    if (grid_obj.max_score is not None):
        print("here")
        return grid_obj.min_score, grid_obj.max_score
    grid = grid_obj.get_grid()
    max_score = float('-inf')
    min_score = float('inf')

    for y in range(0,len(grid)):
        #print('one row')
        for x in range(0, len(grid[0])):
            for p in grid[y][x]:
                max_score = max(max_score, grid_obj.get_score(p, radius))
                min_score = min(min_score, grid_obj.get_score(p, radius))

    #update grid object with max, min scores and repickle
    grid_obj.min_score = min_score
    grid_obj.max_score = max_score
    pickle.dump(grid_obj, open(grid_file, "wb" ))
    return min_score, max_score

def normalize_scores(lat_lon_scores, min_score, max_score):
    normalized_scores = [[score[0], score[1], score[2]/max_score] for score in lat_lon_scores]
    #normalized_scores = [[score[0],score[1],0.001] if score[2]<=0 else score for score in normalized_scores]
    normalized_scores = [[score[0],score[1],0.999] if score[2]>=1 else score for score in normalized_scores ]
    # log_norms=[]
    # for i in range(len(normalized_scores)):
    #     curr_norm = normalized_scores[i]
    #     #print(curr_norm[2])
    #     curr_norm[2]=log10(curr_norm[2])/log10(max_score)
    #     log_norms.append(curr_norm)
    # log_norms = [[score[0],score[1],0.001] if score[2]<=0 else score for score in log_norms]
    # log_norms = [[score[0],score[1],0.999] if score[2]>=1 else score for score in log_norms]
    #normalized_scores = [[score[0],score[1],score[2]/max_score] for score in normalized_scores]
    return normalized_scores




def str_to_point(route_string):
    route_lat_lon_list = route_string.split(" ")
    lat = float(route_lat_lon_list[0])
    lon = float(route_lat_lon_list[1])
    point_object = Point(lat,lon)
    return point_object
