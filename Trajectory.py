import Lane
import matplotlib.pyplot as plt
import numpy as np

class Trajectory:
    def __init__(self, trajection_geometry):
        self.departing_lane = Lane()
        self.receiving_lane = Lane()
        self.trajection_geometry = trajection_geometry

    def compute_trajectory(self, departing_lane, receiving_lane):
        arr = np.zeros((2, 3))
        (x1, y1) = departing_lane.intersection_edge_point
        (x2, y2) = receiving_lane.intersection_edge_point
        arr[0, 0] = x1
        arr[1, 0] = y1
        arr[0, 1] = x2
        arr[1, 1] = y2
        return arr
