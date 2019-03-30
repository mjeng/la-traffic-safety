import pandas as pd
from point import Point
import pickle

class Grid:
    def __init__(self,min_lat,max_lat,min_lon,max_lon,step_size):
        self.min_lat = min_lat // 1
        self.max_lat = (max_lat + 1) // 1
        self.min_lon = (min_lon - 1) // 1
        self.max_lon = max_lon // 1
        self.step_size = step_size
        self.grid = None

    def __init__(self, grid_file):
        pick = pickle.load( open( grid_file, "rb" ) )
        self.min_lat = pick.min_lat
        self.max_lat = pick.max_lat
        self.min_lon = pick.min_lon
        self.max_lon = pick.max_lon
        self.step_size = pick.step_size
        self.grid = pick.grid


    @staticmethod
    def create_grid(data, pickle_file_name = None):
        """
        Takes in raw data, creates Grid instance.
        """
        #read CSV as pandas dataframe
        data = pd.read_csv("grid_file")

        y_num = (max_lat - min_lat + 1) // step_size
        x_num = (max_lon - min_lon + 1) // step_size
        grid = [[[None] for i in range(x_num)] for j in range(y_num)]
        for index, row in data.iterrows():
            Point p = Point(row['Latitude'], row['Longitude'])
            row_index, col_index = index_helper(p)
            grid[row_index][col_index].append(p)
        self.grid = grid
        pickle.dump(self, open(pickle_file_name, "wb" ) )

    def get_score(pt, radius):
        actual_row_index, actual_col_index = index_helper(pt)
        potential_pts = []
        new_max_lat, col_index = index_helper(Point(pt.get_lat() + radius, pt.get_lon()))
        new_min_lat, col_index = index_helper(Point(pt.get_lat() - radius, pt.get_lon()))
        row_index, new_max_lon = index_helper(Point(pt.get_lat(), pt.get_lon() + radius))
        row_index, new_min_lon = index_helper(Point(pt.get_lat(), pt.get_lon() - radius))

        for (lat in range(new_min_lat, new_max_lat+1)):
            for (lon in range(new_min_lon, new_max_lon+1)):
                if (in_bounds(lat, lon)):
                    potential_pts.extend(self.grid[lat][lon])

        actual_num_valid = 0
        for (p in potential_pts):
            squared_dist = (pt.get_lat() - p.get_lat())**2 + (pt.get_lon() - p.get_lon())**2
            if squared_dist ** 0.5 < radius:
                actual_num_valid++
        return actual_num_valid

    def index_helper(pt):
        row_index = (pt.get_lat() - self.min_lat) // step_size
        col_index = (pt.get_lon() - self.min_lon) // step_size
        return row_index, col_index

    def in_bounds(row_index, col_index):
        y_num = (max_lat - min_lat + 1) // step_size
        x_num = (max_lon - min_lon + 1) // step_size
        if (row_index < 0 || row_index > (y_num - 1)):
            return False
        if (col_index < 0 || col_index > (x_num - 1)):
            return False
        return True
