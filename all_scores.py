from point import Point
from grid import Grid
import simplejson as json

def get_all_scores(route_points,grid_file):
    #parse the string of list of lists into a list of points
    from_js_route_pts = json.loads(route_points)
    from_js_route_pts = map(str_to_point,from_js_route_pts)

    #import the grid 2d list here
    grid = Grid(grid_file)
    #get scores for each entry of route_points
    all_scores=[]
    for i in range(0,len(from_js_rout_pts)):
        all_scores.append(grid.get_score(from_js_route_pts))

def str_to_point(route_string):
    route_lat_lon_list = route_string.split(" ")
    lat = route_lat_lon_list[0]
    lon = route_lat_lon_list[1]
    point_object = Point(lat,lon)
    return point_object
