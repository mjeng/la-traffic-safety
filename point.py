class Point:
    __slots__ = ['lat', 'lon','accident_type']
    def __init__(self,lat,lon,accident_type):
        self.lat = lat
        self.lon = lon
        self.accident_type = accident_type

    def get_lat(self):
        return self.lat

    def get_lon(self):
        return self.lon

    def get_accident_type(self):
        return self.accident_type

    def set_lat(self, latitude):
        self.lat = lattitude

    def set_lon(self, longitude):
        self.lon = longitude

    def set_accident_type(self, type):
        self.accident_type = type
