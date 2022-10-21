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
    
    # plotting singular point.
    def plot_intersection():
        plt.plot(center_point_location[0], center_point_location[1])

    # plotting centerline for each leg.
    def plot_centerline_leg():
        for x in legs_collection:
            x_values = np.empty(x.leg_geometry.length, dtype=int)
            y_values = np.empty(x.leg_geometry.length, dtype=int)
            for i in range(0, x.leg_geometry.length - 1):
                x_values[i] = x.leg_geometry[i][0]
                y_values[i] = x.leg_geometry[i][1]
           plt.plot(x_values, y_values) 
    
    # plot the lane edges
    def plot_lane_edges:
        

    # plot the edge of the interesection edge
    def plot_intersection_edge: