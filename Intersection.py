import matplotlib.pyplot as plt
import Trajectory

class Intersection:
    def __init__(self, ID, name, center_point_location, num_legs, legs_collection):
        self.ID = ID
        self.name = name
        self.center_point_location = center_point_location
        self.num_legs = num_legs
        self.legs_collection = legs_collection

    def plot_trajectory():
        plt.plot(Trajectory.compute_xtrajectory(Trajectory.departing_lane, Trajectory.receiving_lane),
         Trajectory.compute_ytrajectory(Trajectory.departing_lane, Trajectory.receiving_lane))
