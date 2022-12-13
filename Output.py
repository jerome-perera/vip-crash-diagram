from Lane import Lane
# from Conflict import Conflict
from Intersection import Intersection
from Leg import *
from Trajectory import Trajectory

class Output:
    def init(self, id):
        self.id = id

    lane1 = Lane("ID1", 3, (11, 7), "departing")
    lane2 = Lane("ID2", 3, (11, 7), "receiving")
    lane3 = Lane("ID3", 3, (8, 10), "departing")
    lane4 = Lane("ID4", 3, (8, 10), "receiving")
    lane5 = Lane("ID5", 3, (5, 7), "departing")
    lane6 = Lane("ID6", 3, (5, 7), "receiving")
    lane7 = Lane("ID7", 3, (8, 4), "departing")
    lane8 = Lane("ID8", 3, (8, 4), "receiving")
    leg1 = Leg("IDL1", "right", 2, (lane1, lane2))
    leg2 = Leg("IDL2", "top", 2, (lane3, lane4))
    leg3 = Leg("IDL3", "left", 2, (lane5, lane6))
    leg4 = Leg("IDL4", "bottom", 2, (lane7, lane8))
    intersection1 = Intersection("ID", "name", (8, 7), 4, (leg1, leg2, leg3, leg4))
    trajectory1 = Trajectory("car1")
    
    right_lane_edge_point = lane1.intersection_edge_point
    top_lane_edge_point = lane3.intersection_edge_point
    left_lane_edge_point = lane5.intersection_edge_point
    bottom_lane_edge_point = lane7.intersection_edge_point

    rightArr = intersection1.computeSection(right_lane_edge_point, leg1.leg_geometry, lane1.lane_width)
    topArr = intersection1.computeSection(top_lane_edge_point, leg2.leg_geometry, lane3.lane_width)
    leftArr = intersection1.computeSection(left_lane_edge_point, leg3.leg_geometry, lane5.lane_width)
    bottomArr = intersection1.computeSection(bottom_lane_edge_point, leg4.leg_geometry, lane7.lane_width)

    intersection1.plot_intersection(rightArr, topArr, leftArr, bottomArr, right_lane_edge_point, top_lane_edge_point, left_lane_edge_point, bottom_lane_edge_point, trajectory1)