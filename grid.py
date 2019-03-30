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

    # def __init__(self, grid_file):
    #     pick = pickle.load( open( grid_file, "rb" ) )
    #     self.min_lat = pick.min_lat
    #     self.max_lat = pick.max_lat
    #     self.min_lon = pick.min_lon
    #     self.max_lon = pick.max_lon
    #     self.step_size = pick.step_size
    #     self.grid = pick.grid


    def create_grid(self,data_file, pickle_file_name = None):
        """
        Takes in raw data, creates Grid instance.
        """
        #read CSV as pandas dataframe
        data = pd.read_csv(data_file)

        y_num = (self.max_lat - self.min_lat + 1) // self.step_size
        x_num = (self.max_lon - self.min_lon + 1) // self.step_size
        grid = [[[None] for i in range(x_num)] for j in range(y_num)]
        for index, row in data.iterrows():
            p = Point(row['Latitude'], row['Longitude'])
            row_index, col_index = self.index_helper(p)
            grid[row_index][col_index].append(p)
        self.grid = grid
        pickle.dump(self, open(pickle_file_name, "wb" ) )

    def get_score(self,pt, radius):
        actual_row_index, actual_col_index = self.index_helper(pt)
        potential_pts = []
        new_max_lat, col_index = self.index_helper(Point(pt.get_lat() + radius, pt.get_lon()))
        new_min_lat, col_index = self.index_helper(Point(pt.get_lat() - radius, pt.get_lon()))
        row_index, new_max_lon = self.index_helper(Point(pt.get_lat(), pt.get_lon() + radius))
        row_index, new_min_lon = self.index_helper(Point(pt.get_lat(), pt.get_lon() - radius))

        for lat in range(new_min_lat, new_max_lat+1):
            for lon in range(new_min_lon, new_max_lon+1):
                if self.in_bounds(lat, lon):
                    potential_pts.extend(self.grid[lat][lon])

        actual_num_valid = 0
        for p in potential_pts:
            squared_dist = (pt.get_lat() - p.get_lat())**2 + (pt.get_lon() - p.get_lon())**2
            if squared_dist ** 0.5 < radius:
                actual_num_valid+=1
        return actual_num_valid

    def index_helper(self,pt):
        row_index = (pt.get_lat() - self.min_lat) // self.step_size
        col_index = (pt.get_lon() - self.min_lon) // self.step_size
        return row_index, col_index

    def in_bounds(self,row_index, col_index):
        y_num = (self.max_lat - self.min_lat + 1) // self.step_size
        x_num = (self.max_lon - self.min_lon + 1) // self.step_size
        if row_index < 0 or row_index > (y_num - 1):
            return False
        if col_index < 0 or col_index > (x_num - 1):
            return False
        return True
