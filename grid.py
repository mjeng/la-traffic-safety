class Grid:
    def __init__(self,grid_file=None,min_lat,max_lat,min_lon,max_lon,grid,step_size):
        self.min_lat = min_lat
        self.max_lat = max_lat
        self.min_lon = min_lon
        self.max_lon = max_lon
        self.step_size = step_size
        self.grid = grid

    @staticmethod
    def create_grid(data):
        """
        Takes in raw data, creates Grid instance.
        """
        return

    def get_score(pt):
        return
