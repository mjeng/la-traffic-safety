from point import Point
from grid import Grid
import all_scores


g = Grid(33.707, 34.3343, -118.1554, -118.6661, 0.001)
g.create_grid("data/cleaned_2018_data.csv", "pickle_test.p")
