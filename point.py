class Point:
    __slots__ = ['lat', 'lon','accident_type']
    def __init__(self,lat,lon):
        self.lat = lat
        self.lon = lon

    def get_lat(self):
        return self.lat

    def get_lon(self):
        return self.lon

    def set_lat(self, latitude):
        self.lat = lattitude

    def set_lon(self, longitude):
        self.lon = longitude
