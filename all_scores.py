from point import Point
from grid import Grid
import simplejson as json

def get_all_scores(route_points,grid_file,radius):
    """
    Takes in route points, and the file for the grid object. Returns a list of tuples (lat,lon,score) for every point on the route
    """
    #parse the string of list of lists into a list of points
    from_js_route_pts = json.loads(route_points)
    from_js_route_pts = map(str_to_point,from_js_route_pts)

    #import the grid 2d list here
    grid = Grid(grid_file)

    #get scores for each entry of route_points
    all_scores = []
    lon_lat_score = []
    for i in range(0,len(from_js_rout_pts)):
        curr_route_point = from_js_route_pts[i]
        all_scores.append(grid.get_score(curr_route_point, radiu))
        ret.append((curr_route_point.get_lat,curr_route_point.get_lon,all_scores[i]))
    return lon_lat_score

def str_to_point(route_string):
    route_lat_lon_list = route_string.split(" ")
    lat = route_lat_lon_list[0]
    lon = route_lat_lon_list[1]
    point_object = Point(lat,lon)
    return point_object
