import pandas as pd
from point import Point
import pickle
from math import log
from grid_cloud_storage import cloud_pickle_dump
from grid_cloud_storage import cloud_pickle_load

class Grid:
    def __init__(self, min_lat=None, max_lat=None, min_lon=None, max_lon=None, step_size=None, pickle_file_name=None):
        if pickle_file_name is None:
            self.min_lat = min_lat // 1
            self.max_lat = (max_lat + 1) // 1
            self.min_lon = (min_lon - 1) // 1
            self.max_lon = max_lon // 1
            self.step_size = step_size
            self.grid = None
            self.max_score = None
        else:
            #pick = pickle.load( open(pickle_file_name, "rb" ) )
            pick = cloud_pickle_load(pickle_file_name)
            self.min_lat = float(pick.min_lat)
            self.max_lat = float(pick.max_lat)
            self.min_lon = float(pick.min_lon)
            self.max_lon = float(pick.max_lon)
            self.step_size = float(pick.step_size)
            self.grid = pick.grid
            if (pick.max_score is not None):
                self.max_score = pick.max_score
            else:
                self.max_score = None



    def get_grid(self):
        return self.grid

    def create_grid(self,data_file, pickle_file_name = None):
        """
        Takes in raw data, creates Grid instance.
        """
        #read CSV as pandas dataframe
        data = pd.read_csv(data_file)

        y_num = (self.max_lat - self.min_lat + 1) // self.step_size
        #print(y_num)
        x_num = (self.max_lon - self.min_lon + 1) // self.step_size
        #print(x_num)
        y_num = int(y_num)
        x_num = int(x_num)
        grid = [[[] for i in range(x_num)] for j in range(y_num)]
        for _, row in data.iterrows():
            p = Point(row['Latitude'], row['Longitude'])
            row_index, col_index = self.index_helper(p)
            grid[row_index][col_index].append(p)
        self.grid = grid
        #print(grid)
        #pickle.dump(self, open(pickle_file_name, "wb" ) )
        cloud_pickle_dump(self, pickle_file_name)

    def get_score(self,pt, radius):
        actual_row_index, actual_col_index = self.index_helper(pt)
        potential_pts = []
        ##CHANGE
        vtemplat=pt.get_lat()
        vtemplon=pt.get_lon()

        new_max_lat, col_index = self.index_helper(Point(vtemplat + radius, vtemplon))
        new_min_lat, col_index = self.index_helper(Point(vtemplat - radius, vtemplon))
        row_index, new_max_lon = self.index_helper(Point(vtemplat, vtemplon + radius))
        row_index, new_min_lon = self.index_helper(Point(vtemplat, vtemplon - radius))

        for lat in range(new_min_lat, new_max_lat+1):
            for lon in range(new_min_lon, new_max_lon+1):
                if self.in_bounds(lat, lon):
                    potential_pts.extend(self.grid[lat][lon])

        actual_num_valid = 0
        for p in potential_pts:
            curr_point_lat = pt.get_lat()
            curr_point_lon = pt.get_lon()
            squared_dist = (curr_point_lat - p.get_lat())**2 + (curr_point_lon - p.get_lon())**2
            if squared_dist ** 0.5 < radius:
                actual_num_valid+=1
        return actual_num_valid

    def index_helper(self,pt):
        row_index = (float(pt.get_lat()) - self.min_lat) // self.step_size
        col_index = (float(pt.get_lon()) - self.min_lon) // self.step_size
        return int(row_index), int(col_index)

    def in_bounds(self,row_index, col_index):
        y_num = (self.max_lat - self.min_lat + 1) // self.step_size
        x_num = (self.max_lon - self.min_lon + 1) // self.step_size
        if row_index < 0 or row_index > (y_num - 1):
            return False
        if col_index < 0 or col_index > (x_num - 1):
            return False
        return True
