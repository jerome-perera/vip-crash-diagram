import matplotlib.pyplot as plt
from Trajectory import Trajectory
import Lane

class Intersection:
    def __init__(self, ID, name, center_point_location, num_legs, legs_collection):
        self.ID = ID
        self.name = name
        self.center_point_location = center_point_location
        self.num_legs = num_legs
        self.legs_collection = legs_collection

    def computeSection(self, laneEdgePoint, orientation, lane_width):
        if (orientation == "left"):
            leg_edge_x = (-1 * self.center_point_location[0], laneEdgePoint[0])
            leg_edge_y = (laneEdgePoint[1], laneEdgePoint[1])
                
            lane_stop_x = (laneEdgePoint[0] - 14.5, laneEdgePoint[0] - 14.5)
            lane_stop_y = (laneEdgePoint[1], laneEdgePoint[1] - lane_width)

            lane_edgeleft_x = (-1 * self.center_point_location[0], laneEdgePoint[0])
            lane_edgeleft_y = (laneEdgePoint[1] + lane_width, laneEdgePoint[1] + lane_width)
            
            lane_edgeright_x = (-1 * self.center_point_location[0], laneEdgePoint[0])
            lane_edgeright_y = (laneEdgePoint[1] - lane_width, laneEdgePoint[1] - lane_width)

            lane_dividerleft_x = (-1 * self.center_point_location[0], laneEdgePoint[0])
            lane_dividerleft_y = (laneEdgePoint[1] + (lane_width / 2), laneEdgePoint[1] + (lane_width / 2))

            lane_dividerright_x = (-1 * self.center_point_location[0], laneEdgePoint[0])
            lane_dividerright_y = (laneEdgePoint[1] - (lane_width / 2), laneEdgePoint[1] - (lane_width / 2))
            
            returnArray = [leg_edge_x, leg_edge_y, lane_stop_x, lane_stop_y, lane_edgeleft_x, lane_edgeleft_y, lane_edgeright_x,
                                lane_edgeright_y, lane_dividerleft_x, lane_dividerleft_y, lane_dividerright_x, lane_dividerright_y]
            return returnArray
        elif (orientation == "right"):
            leg_edge_x = (laneEdgePoint[0], self.center_point_location[0])
            leg_edge_y = (laneEdgePoint[1], laneEdgePoint[1])

            lane_stop_x = (laneEdgePoint[0] + 14.5, laneEdgePoint[0] + 14.5)
            lane_stop_y = (laneEdgePoint[1], laneEdgePoint[1] + lane_width)

            lane_edgeleft_x = (laneEdgePoint[0], self.center_point_location[0])
            lane_edgeleft_y = (laneEdgePoint[1] + lane_width, laneEdgePoint[1] + lane_width)

            lane_edgeright_x = (laneEdgePoint[0], self.center_point_location[0])
            lane_edgeright_y = (laneEdgePoint[1] - lane_width, laneEdgePoint[1] - lane_width)

            lane_dividerleft_x = (laneEdgePoint[0], self.center_point_location[0])
            lane_dividerleft_y = (laneEdgePoint[1] + (lane_width / 2), laneEdgePoint[1] + (lane_width / 2))

            lane_dividerright_x = (laneEdgePoint[0], self.center_point_location[0])
            lane_dividerright_y = (laneEdgePoint[1] - (lane_width / 2),laneEdgePoint[1] - (lane_width / 2))


            returnArray = [leg_edge_x, leg_edge_y, lane_stop_x, lane_stop_y, lane_edgeleft_x, lane_edgeleft_y, lane_edgeright_x,
                                lane_edgeright_y, lane_dividerleft_x, lane_dividerleft_y, lane_dividerright_x, lane_dividerright_y]
            return returnArray
        elif (orientation == "top"):
            leg_edge_x = (laneEdgePoint[0], laneEdgePoint[0])
            leg_edge_y = (laneEdgePoint[1], self.center_point_location[1])

            lane_stop_x = (laneEdgePoint[0] - lane_width, laneEdgePoint[0])
            lane_stop_y = (laneEdgePoint[1] + 14.5, laneEdgePoint[1] + 14.5)

            lane_edgeleft_x = (laneEdgePoint[0] - lane_width, laneEdgePoint[0] - lane_width)
            lane_edgeleft_y = (laneEdgePoint[1], self.center_point_location[1])

            lane_edgeright_x = (laneEdgePoint[0] + lane_width, laneEdgePoint[0] + lane_width)
            lane_edgeright_y = (laneEdgePoint[1], self.center_point_location[1])

            lane_dividerleft_x = (laneEdgePoint[0] - (lane_width / 2), laneEdgePoint[0] - (lane_width / 2))
            lane_dividerleft_y = (laneEdgePoint[1], self.center_point_location[1])

            lane_dividerright_x = (laneEdgePoint[0] + (lane_width / 2), laneEdgePoint[0] + (lane_width / 2))
            lane_dividerright_y = (laneEdgePoint[1], self.center_point_location[1])
            returnArray = [leg_edge_x, leg_edge_y, lane_stop_x, lane_stop_y, lane_edgeleft_x, lane_edgeleft_y, lane_edgeright_x,
                                lane_edgeright_y, lane_dividerleft_x, lane_dividerleft_y, lane_dividerright_x, lane_dividerright_y]
            return returnArray
        elif (orientation == "bottom"):
            leg_edge_x = (laneEdgePoint[0], laneEdgePoint[0])
            leg_edge_y = (-1 * self.center_point_location[1], laneEdgePoint[1])

            lane_stop_x = (laneEdgePoint[0], laneEdgePoint[0] + lane_width)
            lane_stop_y = (laneEdgePoint[1] - 14.5, laneEdgePoint[1] - 14.5)

            lane_edgeleft_x = (laneEdgePoint[0] - lane_width, laneEdgePoint[0] - lane_width)
            lane_edgeleft_y = (-1 * self.center_point_location[1], laneEdgePoint[1])

            lane_edgeright_x = (laneEdgePoint[0] + lane_width, laneEdgePoint[0] + lane_width)
            lane_edgeright_y = (-1 * self.center_point_location[1], laneEdgePoint[1])

            lane_dividerleft_x = (laneEdgePoint[0] - (lane_width / 2), laneEdgePoint[0] - (lane_width / 2))
            lane_dividerleft_y = (-1 * self.center_point_location[1], laneEdgePoint[1])

            lane_dividerright_x = (laneEdgePoint[0] + (lane_width / 2), laneEdgePoint[0] + (lane_width / 2))
            lane_dividerright_y = (-1 * self.center_point_location[1], laneEdgePoint[1])
            returnArray = [leg_edge_x, leg_edge_y, lane_stop_x, lane_stop_y, lane_edgeleft_x, lane_edgeleft_y, lane_edgeright_x,
                                lane_edgeright_y, lane_dividerleft_x, lane_dividerleft_y, lane_dividerright_x, lane_dividerright_y]
            return returnArray
        else:
            raise ValueError("Error: Orientation is not valid")
    
    # plotting singular point.
    def plot_intersection(self, rightArr, topArr, leftArr, bottomArr, right_lane_edge_point, top_lane_edge_point, left_lane_edge_point, bottom_lane_edge_point):
        plt.rcParams["figure.facecolor"] = '0.8'
        plt.xlim(-1 * self.center_point_location[0], self.center_point_location[0])
        plt.ylim(-1 * self.center_point_location[1], self.center_point_location[1])

        #Plot Right Graph
        plt.plot(right_lane_edge_point[0], right_lane_edge_point[1], marker='o', markersize=5, markeredgecolor="red", markerfacecolor="green")
        plt.plot(rightArr[0], rightArr[1], color='yellow')
        plt.plot(rightArr[2], rightArr[3], color='green')
        plt.plot(rightArr[4], rightArr[5], color="black")
        plt.plot(rightArr[6], rightArr[7], color="black")
        plt.plot(rightArr[8], rightArr[9], '--')
        plt.plot(rightArr[10], rightArr[11], '--')

        #Plot Top Graph
        plt.plot(top_lane_edge_point[0], top_lane_edge_point[1], marker='o', markersize=5, markeredgecolor="red", markerfacecolor="green")
        plt.plot(topArr[0], topArr[1], color='yellow')
        plt.plot(topArr[2], topArr[3], color='green')
        plt.plot(topArr[4], topArr[5], color='black')
        plt.plot(topArr[6], topArr[7], color='black')
        plt.plot(topArr[8], topArr[9], '--')
        plt.plot(topArr[10], topArr[11], '--')

        #Plot Left Graph
        plt.plot(left_lane_edge_point[0], left_lane_edge_point[1], marker='o', markersize=5, markeredgecolor="red", markerfacecolor="green")
        plt.plot(leftArr[0], leftArr[1], color='yellow')
        plt.plot(leftArr[2], leftArr[3], color='green')
        plt.plot(leftArr[4], leftArr[5], color='black')
        plt.plot(leftArr[6], leftArr[7], color='black')
        plt.plot(leftArr[8], leftArr[9], '--')
        plt.plot(leftArr[10], leftArr[11], '--')

        #Plot Bottom Graph
        plt.plot(bottom_lane_edge_point[0], bottom_lane_edge_point[1], marker='o', markersize=5, markeredgecolor="red", markerfacecolor="green")
        plt.plot(bottomArr[0], bottomArr[1], color='yellow')
        plt.plot(bottomArr[2], bottomArr[3], color='green')
        plt.plot(bottomArr[4], bottomArr[5], color='black')
        plt.plot(bottomArr[6], bottomArr[7], color='black')
        plt.plot(bottomArr[8], bottomArr[9], '--')
        plt.plot(bottomArr[10], bottomArr[11], '--')

        trajectory1 = Trajectory("car1")
        trajectory2 = Trajectory("car2")

        point1 = (130, 85)
        point2 = (110, 85)
        point3 = (95, 100)
        point4 = (95, 120)

        trajectory1.compute_trajectory(point1, point2, point3, point4)

        point1b = (137.5, 85)
        point2b = (117.5, 85)
        point3b = (95, 92.5)
        point4b = (95, 112.5)

        trajectory2.compute_trajectory(point1b, point2b, point3b, point4b)

        plt.show()
