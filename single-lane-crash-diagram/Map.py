import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from Symbol import Symbol_Map
import random

plt.rcParams["figure.figsize"] = [8, 8]
plt.rcParams["figure.autolayout"] = True

#intersection plotting
x1 = [0,24,24]  #line 1
y1 = [24,24,0]
x2 = [48,48,72] #line 2
y2 = [0,24,24]
x3 = [72,48,48] #line 3
y3 = [48,48,72]
x4 = [24,24,0]  #line 4
y4 = [72,48,48]

#centerline and stopbar plotting
x5 = [x1[2]+12,x1[1]+12,x2[1]] #north #make it simple
y5 = [y1[2],y1[1],y2[1]]
x6 = [x3[2]-12,x3[1]-12,x4[1]] #south
y6 = [y3[2],y3[1],y4[1]]
x7 = [x1[0],x1[1],x1[1]]     #east
y7 = [y1[0]+12,y1[1]+12,y1[1]]
x8 = [x3[0],x3[1],x3[1]]     #west
y8 = [y3[0]-12,y3[1]-12,y3[1]]
    
# Road being plotted
plt.plot(x1, y1, color="black")
plt.plot(x2, y2, color="black")
plt.plot(x3, y3, color="black")
plt.plot(x4, y4, color="black")
plt.plot(x5, y5, color="orange")
plt.plot(x6, y6, color="orange")
plt.plot(x7, y7, color="orange")
plt.plot(x8, y8, color="orange")

# Symbols being added to the plot
def getImage(path):
    return OffsetImage(plt.imread(path, format="jpg"), zoom=.1)

paths = Symbol_Map.file_list

x = []
y = []
for symbol in paths:
    x.append(random.uniform(0, 72))
    y.append(random.uniform(24, 48))

for x0, y0, path in zip(x, y, paths):
    ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
    plt.gca().add_artist(ab)

plt.legend()
plt.xticks(np.arange(0, 84, 12))
plt.yticks(np.arange(0, 84, 12))
plt.axis('equal')

plt.show()


# Tasks:
# 1) Connect Eric's data to Rishi's code.
# 2.5) Rishi should clean up symbology to make sure nothin is printed extra. For example, pedestrian crash locations should always be plotted manually.

# 2) Either hardcode location that have single crash point based on indivudual crash type or add bezier.

# 3) Make a counter that keeps track of the amount of each type of crash in the 33 different nodes. Should plot onto map only the most common occuring crash. If there is a tie select one of the highest randomly.
# 4) Eric should search through his data for crash types with multliple locations and store that in a seperate data file to give to traffic engineers to manually plot. Only allowed data should be plotted.

# 5) Test crash diagram on 20 single lane 2 roads intersections. Obtain accuracy first and then time reduction percentage.

# 6) Rishi sets up system to allow traffic engineers to manually input data locatation when needed.


# Point of tool: Shows the most common crashes occuring at certain parts of the intersection.



# Stopped is not there. 