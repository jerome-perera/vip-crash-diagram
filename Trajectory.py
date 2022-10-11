import Lane
import matplotlib.pyplot as plt

class Trajectory:
    def __init__(self, trajection_geometry):
        self.departing_lane = Lane()
        self.receiving_lane = Lane()
        self.trajection_geometry = trajection_geometry

    def compute_xtrajectory(self, departing_lane, receiving_lane):
        (x1, y1) = departing_lane.intersection_edge_point
        (x2, y2) = receiving_lane.intersection_edge_point
        xcoord = [x1, x2]
        return xcoord

    def compute_ytrajectory(self, departing_lane, receiving_lane):
        (x1, y1) = departing_lane.intersection_edge_point
        (x2, y2) = receiving_lane.intersection_edge_point
        ycoord = [y1, y2]
        return ycoord
