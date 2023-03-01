from Lane import Lane
import seaborn
import bezier
import math
from shapely.geometry import Point, LineString
import matplotlib.pyplot as plt
import numpy as np

class Trajectory:
    def __init__(self, trajection_geometry):
        #self.departing_lane = Lane()
        #self.receiving_lane = Lane()
        self.trajection_geometry = trajection_geometry

    def compute_trajectory(self, point1, point2, point3, point4):
        d1 = math.dist(point1, point2)
        d2 = math.dist(point3, point4)
        dc = math.dist(point2, point3)
        dc1 = d1 + dc/2
        dc2 = d2 + dc/2

        dx1 = point2[0] - point1[0]
        dy1 = point2[1] - point1[1]

        k = math.sqrt((dc1*dc1)/(dx1*dx1 + dy1*dy1))
        c1x = point1[0]+ dx1*k
        c1y = point1[1]+ dy1*k
        c1x = round(c1x, 2)
        c1y = round(c1y, 2)
        print ("x and y coordinates of control point c1 is", (c1x, c1y))

        dx2 = point3[0] - point4[0]
        dy2 = point3[1] - point4[1]

        k = math.sqrt((dc2*dc2)/(dx2*dx2 + dy2*dy2))
        c2x = point4[0]+ dx2*k
        c2y = point4[1]+ dy2*k
        c2x = round(c2x, 2)
        c2y = round(c2y, 2)
        print ("x and y coordinates of control point c2 is", (c2x, c2y))

        e1 = [point1[0], point1[1]]
        e2 = [point4[0], point4[1]]
        c1 = [c1x, c1y]
        c2 = [c2x, c2y]

        #generate curve using bezier function
        nodes1 = np.array([[point1[0], point2[0], c1x, c2x, point3[0], point4[0]],
                        [point1[1], point2[1], c1y, c2y, point3[1], point4[1]]])
        curve1 = bezier.Curve.from_nodes(nodes1)
        seaborn.set()
        ax1 = curve1.plot(num_pts=256)
        plt.title("Bezier curve")
        x = np.array([point1[0], point2[0], c1x, c2x, point3[0], point4[0]])
        y = np.array([point1[1], point2[1], c1y, c2y, point3[1], point4[1]])
        plt.scatter(x,y)

        for i_x, i_y in zip(x, y):
            plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
        #plt.show()

        #angle of departing lane
        x1 = point1[0]
        y1 = point1[1]
        x2 = point2[0]
        y2 = point2[1]
        angle1 = np.arctan((y2-y1) / (x2-x1))
        print ("Departing lane angle is",math.degrees(angle1))

        #maneuver 1
        angle1 = math.degrees(angle1)
        if angle1 in range(0, 30):
            print ("Manuever = straight")
        if angle1 in range(31, 180):
            print ("Manuever = right")
        if angle1 in range(181, 330):
            print ("Manuever = left")
        if angle1 in range(331, 360):
            print ("Manuever = straight")
