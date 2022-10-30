import matplotlib.pyplot as plt
import math


intersection_center_point = (8, 7)
plt.xlim(0, 2 * intersection_center_point[0])
plt.ylim(0, 2 * intersection_center_point[1])
lane_width = 2

############################## Right lane #####################################
right_lane_edge_point = (10, 7)

right_leg_edge_x = (right_lane_edge_point[0], 2 * intersection_center_point[0])
right_leg_edge_y = (right_lane_edge_point[1], right_lane_edge_point[1])

right_lane_stop_x = (right_lane_edge_point[0], right_lane_edge_point[0])
right_lane_stop_y = (right_lane_edge_point[1], right_lane_edge_point[1] + lane_width)

right_lane_edgetop_x = (right_lane_edge_point[0], 2 * intersection_center_point[0])
right_lane_edgetop_y = (right_lane_edge_point[1] + lane_width, right_lane_edge_point[1] + lane_width)

right_lane_edgebottom_x = (right_lane_edge_point[0], 2 * intersection_center_point[0])
right_lane_edgebottom_y = (right_lane_edge_point[1] - lane_width, right_lane_edge_point[1] - lane_width)

right_lane_dividertop_x = (0, 2 * intersection_center_point[0])
right_lane_dividertop_y = (right_lane_edge_point[1] + (lane_width / 2), right_lane_edge_point[1] + (lane_width / 2))

right_lane_dividerbottom_x = (0, 2 * intersection_center_point[0])
right_lane_dividerbottom_y = (right_lane_edge_point[1] - (lane_width / 2), right_lane_edge_point[1] - (lane_width / 2))


############################## Top lane #####################################
top_lane_edge_point = (8, 9)

top_leg_edge_x = (top_lane_edge_point[0], top_lane_edge_point[0])
top_leg_edge_y = (top_lane_edge_point[1], 2 * intersection_center_point[1])

top_lane_stop_x = (top_lane_edge_point[0] - lane_width, top_lane_edge_point[0])
top_lane_stop_y = (top_lane_edge_point[1], top_lane_edge_point[1])

top_lane_edgeleft_x = (top_lane_edge_point[0] - lane_width, top_lane_edge_point[0] - lane_width)
top_lane_edgeleft_y = (top_lane_edge_point[1], 2 * intersection_center_point[1])

top_lane_edgeright_x = (top_lane_edge_point[0] + lane_width, top_lane_edge_point[0] + lane_width)
top_lane_edgeright_y = (top_lane_edge_point[1], 2 * intersection_center_point[1])

top_lane_dividerleft_x = (top_lane_edge_point[0] - (lane_width / 2), top_lane_edge_point[0] - (lane_width / 2))
top_lane_dividerleft_y = (0, 2 * intersection_center_point[1])

top_lane_dividerright_x = (top_lane_edge_point[0] + (lane_width / 2), top_lane_edge_point[0] + (lane_width / 2))
top_lane_dividerright_y = (0, 2 * intersection_center_point[1])


############################## Plot Top-Right Curve #########################

# arr = np.asfortranarray([
#     [top_lane_edge_point[0] + lane_width, top_lane_edge_point[0] + lane_width, right_lane_edge_point[0]]
#     [top_lane_edge_point[1] + lane_width, top_lane_edge_point[1], right_lane_edge_point[1] + lane_width]
# ])
# curve = bezier.Curve(arr, degree=2)

############################## Plot Trajectory Points #######################

point1 = (right_lane_edge_point[0], right_lane_edge_point[1] + (lane_width / 2))
point2 = (top_lane_edge_point[0] + (lane_width / 2), top_lane_edge_point[1])
plt.plot(point1[0], point1[1], marker='o', markersize=5, markeredgecolor="blue", markerfacecolor="green")
plt.plot(point2[0], point2[1], marker='o', markersize=5, markeredgecolor="blue", markerfacecolor="green")
xpoints = [point1[0], point2[0]]
ypoints = [point1[1], point2[1]]
plt.plot(xpoints, ypoints)

############################## Plot Right Graph #############################

plt.plot(right_lane_edge_point[0], right_lane_edge_point[1], marker='o', markersize=5, markeredgecolor="red", markerfacecolor="green")
plt.plot(right_leg_edge_x, right_leg_edge_y, "--")
plt.plot(right_lane_stop_x, right_lane_stop_y)
plt.plot(right_lane_edgetop_x, right_lane_edgetop_y)
plt.plot(right_lane_edgebottom_x, right_lane_edgebottom_y)
plt.plot(right_lane_dividertop_x, right_lane_dividertop_y)
plt.plot(right_lane_dividerbottom_x, right_lane_dividerbottom_y)

############################## Plot Top Graph ###############################

plt.plot(top_lane_edge_point[0], top_lane_edge_point[1], marker='o', markersize=5, markeredgecolor="red", markerfacecolor="green")
plt.plot(top_leg_edge_x, top_leg_edge_y, "--")
plt.plot(top_lane_stop_x, top_lane_stop_y)
plt.plot(top_lane_edgeleft_x, top_lane_edgeleft_y)
plt.plot(top_lane_edgeright_x, top_lane_edgeright_y)
plt.plot(top_lane_dividerleft_x, top_lane_dividerleft_y)
plt.plot(top_lane_dividerright_x, top_lane_dividerright_y)
