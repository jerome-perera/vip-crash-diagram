import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from Symbol import Symbol_Map
import random
from scipy.interpolate import make_interp_spline, BSpline
from scipy.ndimage import rotate
import os

plt.rcParams["figure.figsize"] = [12, 6]  # increase figure size

# intersection plotting
x1 = [0, 24, 24]  # line 1
y1 = [24, 24, 0]
x2 = [48, 48, 72]  # line 2
y2 = [0, 24, 24]
x3 = [72, 48, 48]  # line 3
y3 = [48, 48, 72]
x4 = [24, 24, 0]  # line 4
y4 = [72, 48, 48]

# centerline and stopbar plotting
x5 = [x1[2] + 12, x1[1] + 12, x2[1]]  # north #make it simple
y5 = [y1[2], y1[1], y2[1]]
x6 = [x3[2] - 12, x3[1] - 12, x4[1]]  # south
y6 = [y3[2], y3[1], y4[1]]
x7 = [x1[0], x1[1], x1[1]]  # east
y7 = [y1[0] + 12, y1[1] + 12, y1[1]]
x8 = [x3[0], x3[1], x3[1]]  # west
y8 = [y3[0] - 12, y3[1] - 12, y3[1]]

# create grid of subplots
fig, axs = plt.subplots(1, 2, gridspec_kw={'width_ratios': [2, 1]})

# plot road on first subplot
axs[0].plot(x1, y1, color="black")
axs[0].plot(x2, y2, color="black")
axs[0].plot(x3, y3, color="black")
axs[0].plot(x4, y4, color="black")
axs[0].plot(x5, y5, color="orange")
axs[0].plot(x6, y6, color="orange")
axs[0].plot(x7, y7, color="orange")
axs[0].plot(x8, y8, color="orange")


# Right Turn Trajectories (Red)
if 'South-Turning Right' in Symbol_Map.trajectories:
    x9 = [18, 27, 30]
    y9 = [42, 48, 54]
    spl = make_interp_spline(x9, y9, k=2)
    xs = np.linspace(18, 30, 102)
    ys = spl(xs)
    axs[0].plot(xs, ys, color="red", linestyle="dotted")
    axs[0].arrow(20, 41.75, -1, 0, color="red", width=0.1, head_width=0.5, length_includes_head=True)

if 'East-Turning Right' in Symbol_Map.trajectories:
    x9 = [18, 24, 30]
    y9 = [30, 27, 18]
    spl = make_interp_spline(x9, y9, k=2)
    xs = np.linspace(18, 30, 102)
    ys = spl(xs)
    axs[0].plot(xs, ys, color="red", linestyle="dotted")
    axs[0].arrow(29, 20, 0.5, -1, color="red", width=0.1, head_width=0.5, length_includes_head=True)

if 'North-Turning Right' in Symbol_Map.trajectories:
    x9 = [42, 45, 54]
    y9 = [18, 24, 30]
    spl = make_interp_spline(x9, y9, k=2)
    xs = np.linspace(42, 54, 102)
    ys = spl(xs)
    axs[0].plot(xs, ys, color="red", linestyle="dotted")
    axs[0].arrow(52, 30.25, 1, 0, color="red", width=0.1, head_width=0.5, length_includes_head=True)

if 'West-Turning Right' in Symbol_Map.trajectories:
    x9 = [42, 48, 54]
    y9 = [54, 45, 42]
    spl = make_interp_spline(x9, y9, k=2)
    xs = np.linspace(42, 54, 102)
    ys = spl(xs)
    axs[0].plot(xs, ys, color="red", linestyle="dotted")
    axs[0].arrow(43, 52.25, -0.5, 1, color="red", width=0.1, head_width=0.5, length_includes_head=True)



# Long Left Turn (Purple)
if 'Long South-Turning Left' in Symbol_Map.trajectories:
    x10 = [30, 34, 36, 40, 42, 48, 54]
    y10 = [54, 42, 40, 36, 34, 30, 30]
    spl2 = make_interp_spline(x10, y10, k=2)
    xs2 = np.linspace(30, 54, 102)
    ys2 = spl2(xs2)
    axs[0].plot(xs2, ys2, color="purple", linestyle="dotted")
    axs[0].arrow(52, 29.5, 1, 0, color="purple", width=0.1, head_width=0.5, length_includes_head=True)

if 'Long East-Turning Left' in Symbol_Map.trajectories:
    x10 = [18, 30, 32, 36, 38, 42, 43]
    y10 = [30, 34, 36, 40, 42, 48, 51]
    spl2 = make_interp_spline(x10, y10, k=2)
    xs2 = np.linspace(18, 43.25, 102)
    ys2 = spl2(xs2)
    axs[0].plot(xs2, ys2, color="purple", linestyle="dotted")
    axs[0].arrow(43.25, 52, 0.25, 1, color="purple", width=0.1, head_width=0.5, length_includes_head=True)

if 'Long North-Turning Left' in Symbol_Map.trajectories:
    x10 = [24, 30, 32, 36, 37.75, 40.25, 41.5, 41.75]
    y10 = [42, 38, 36, 32, 30,    24, 20,   19]
    spl2 = make_interp_spline(x10, y10, k=2)
    xs2 = np.linspace(18, 41.75, 102)
    ys2 = spl2(xs2)
    axs[0].plot(xs2, ys2, color="purple", linestyle="dotted")
    axs[0].arrow(19.75, 43, -1, 0, color="purple", width=0.1, head_width=0.5, length_includes_head=True)

if 'Long West-Turning Left' in Symbol_Map.trajectories:
    x10 = [29, 30, 34, 36, 40, 42, 54]
    y10 = [21, 24, 30, 32, 36, 38, 41.5]
    spl2 = make_interp_spline(x10, y10, k=2)
    xs2 = np.linspace(28.5, 54, 102)
    ys2 = spl2(xs2)
    axs[0].plot(xs2, ys2, color="purple", linestyle="dotted")
    axs[0].arrow(28.75, 20, -0.25, -1, color="purple", width=0.1, head_width=0.5, length_includes_head=True)



# Short Left Turn (Green)
if 'Short North-Turning Left' in Symbol_Map.trajectories:
    x10 = [18, 30, 42]
    y10 = [36, 30, 18]
    spl2 = make_interp_spline(x10, y10, k=2)
    xs2 = np.linspace(18, 42, 102)
    ys2 = spl2(xs2)
    axs[0].plot(xs2, ys2, color="green", linestyle="dotted")
    axs[0].arrow(19.5, 35.5, -.5, .25, color="green", width=0.1, head_width=0.5, length_includes_head=True)

if 'Short East-Turning Left' in Symbol_Map.trajectories:
    x10 = [18, 30, 36]
    y10 = [30, 42, 54]
    spl2 = make_interp_spline(x10, y10, k=2)
    xs2 = np.linspace(18, 36, 102)
    ys2 = spl2(xs2)
    axs[0].plot(xs2, ys2, color="green", linestyle="dotted")
    axs[0].arrow(35.25, 52.25, .5, 1, color="green", width=0.1, head_width=0.5, length_includes_head=True)

if 'Short South-Turning Left' in Symbol_Map.trajectories:
    x10 = [30, 42, 54]
    y10 = [54, 42, 36]
    spl2 = make_interp_spline(x10, y10, k=2)
    xs2 = np.linspace(30, 54, 102)
    ys2 = spl2(xs2)
    axs[0].plot(xs2, ys2, color="green", linestyle="dotted")
    axs[0].arrow(52.5, 36.375, .5, -.25, color="green", width=0.1, head_width=0.5, length_includes_head=True)

if 'Short West-Turning Left' in Symbol_Map.trajectories:
    x10 = [36, 42, 54]
    y10 = [18, 30, 42]
    spl2 = make_interp_spline(x10, y10, k=2)
    xs2 = np.linspace(36, 54, 102)
    ys2 = spl2(xs2)
    axs[0].plot(xs2, ys2, color="green", linestyle="dotted")
    axs[0].arrow(37-0.1275, 20, -.5, -1, color="green", width=0.1, head_width=0.5, length_includes_head=True)




# Add dotted lightblue line for stopbar
axs[0].plot([0, 72], [42, 42], linestyle='dotted', color='lightblue')
axs[0].arrow(15, 42, -1, 0, color="lightblue", width=0.1, head_width=0.5, length_includes_head=True)

axs[0].plot([42, 42], [0, 72], linestyle='dotted', color='lightblue')
axs[0].arrow(42, 57, 0, 1, color="lightblue", width=0.1, head_width=0.5, length_includes_head=True)

axs[0].plot([30, 30], [0, 72], linestyle='dotted', color='lightblue')
axs[0].arrow(30, 15, 0, -1, color="lightblue", width=0.1, head_width=0.5, length_includes_head=True)

axs[0].plot([0, 72], [30, 30], linestyle='dotted', color='lightblue')
axs[0].arrow(57, 30, 1, 0, color="lightblue", width=0.1, head_width=0.5, length_includes_head=True)












# Symbols being added to the plot
def getImage(path):
    return OffsetImage(plt.imread(path, format="jpg"), zoom=.1)
paths = Symbol_Map.file_list
x = [30, 36, 42, 42, 18, 24, 30, 34, 38, 42, 54, 36, 30, 42, 18, 32, 36, 40, 54, 30, 42, 36, 18, 30, 34, 38, 42, 48, 54, 30, 30, 36, 42]
y = [54, 54, 54, 48, 42, 42, 42, 42, 42, 42, 42, 40, 38, 38, 36, 36, 36, 36, 36, 34, 34, 32, 30, 30, 30, 30, 30, 30, 30, 24, 18, 18, 18]
node_num = 1
for x0, y0, path in zip(x, y, paths):
    if path.startswith("unplotted"):
        node_num += 1
    else:
        ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
        axs[0].add_artist(ab)
        axs[0].text(x0, y0-1.75, str(node_num), color='black', ha='center', va='center', fontsize=8, weight='bold')
        node_num += 1

axs[0].legend()
axs[0].set_xticks(np.arange(0, 84, 12))
axs[0].set_yticks(np.arange(0, 84, 12))
axs[0].set_aspect('equal')


# generate data for table with labels in first column
data = np.concatenate((np.arange(1, 34).reshape(-1, 1), np.random.randint(low=0, high=100, size=(33, 2))), axis=1)

# set all non-first column elements to 0
data[:, 1:] = 0


for i in range(1, 34): 
    data[i-1, 1] = Symbol_Map.max_counter[i-1]
    data[i-1, 2] = Symbol_Map.data_counter[i-1]

# add table to second subplot
table = axs[1].table(cellText=data, colLabels=['Location', 'Most Common Crash', 'Total Crashes'], loc='center', cellLoc='center')

# adjust table properties
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2) # scale the table

# adjust cell heights
for cell in table._cells:
    table._cells[cell]._text.set_fontsize(10) # reduce font size of text in cell
    table._cells[cell].set_height(0.02) # reduce height of cell
    table._cells[cell].set_width(0.3) # reduce width of cell

axs[1].axis('off') # turn off axis

# adjust subplot sizes and spacing
plt.subplots_adjust(wspace=0.1) # or a smaller value as needed
plt.tight_layout()
plt.show()
