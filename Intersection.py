import matplotlib.pyplot as plt
import Trajectory
import numpy as np

class Intersection:
    def __init__(self, ID, name, center_point_location, num_legs, legs_collection):
        self.ID = ID
        self.name = name
        self.center_point_location = center_point_location
        self.num_legs = num_legs
        self.legs_collection = legs_collection

    def plot_trajectory():
        arr = Trajectory.compute_trajectory(Trajectory.departing_lane, Trajectory.receiving_lane)
        plt.plot(arr[0, :], arr[1, :])
