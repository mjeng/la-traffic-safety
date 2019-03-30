from point import Point
from grid import Grid
import simplejson as json

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
        lat_lon_scores.append((curr_route_point.get_lat(),curr_route_point.get_lon(),grid.get_score(curr_route_point, radius)))

    #min_score, max_score = get_min_max_scores(grid_file, radius)
    #normalized = normalize_scores(lat_lon_scores, min_score, max_score)

    #print(lon_lat_score
    return lat_lon_scores
    #return normalized

def get_min_max_scores(grid_file, radius):
    grid = Grid(pickle_file_name = grid_file)
    max_score = float('-inf')
    min_score = float('inf')
    lat = grid.min_lat
    lon = grid.min_lon
    while (lat < grid.max_lat):
        while (lon < grid.max_lon):
            score = grid.get_score(Point(lat, lon), radius)
            max_score = max(score, max_score)
            min_score = min(score, min_score)
            lat += 2 * radius
            lon += 2 * radius
    return min_score, max_score

def normalize_scores(lat_lon_scores, min_score, max_score):
    normalized_scores = [(score[0], score[1], (score[2] - min_score)/max_score) for score in lat_lon_scores]
    return normalized_scores




def str_to_point(route_string):
    route_lat_lon_list = route_string.split(" ")
    lat = float(route_lat_lon_list[0])
    lon = float(route_lat_lon_list[1])
    point_object = Point(lat,lon)
    return point_object
