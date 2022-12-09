import matplotlib.pyplot as plt
import math
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
from scipy.interpolate import make_interp_spline
import Conflict
import Trajectory
import numpy as np
import math

class Symbols:
    # case by case approach
    def __init__(v1Manuever, v2Manuever, v1Direction, v2Direction):
        this.v1Manuever = v1Manuever
        this.v2Manuever = v2Manuever
        this.v1Direction = v1Direction
        this,v2Direction = v2Direction

    # Setting up graph itself.
    plt.rcParams["figure.figsize"] = [3.5, 3.5]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    ax = fig.add_subplot()
    circle1 = plt.Circle((0.2, 0.2), radius=0.5, color='grey')
    ax.add_patch(circle1)

    #use direction data to figure out direction and understand to find x or y value when comparing.
    #map symbol for Object1

    if v1Manuever == 0 and v2Manuever == 0 and v1Direction == "North" and v2Direction == "West":
        # Drawing Vehicle 2 arrow.
        plt.plot([0.3,0.5],[0.35,0.35], linewidth = '15', color = 'red')
        plt.arrow(0.3, 0.35, -0.005, 0, width = 0.05, color = 'red')

        #Drawing Vehicle 1 arrow.
        plt.plot([0,0],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0, .2, 0, 0.005, width = 0.05, color = 'darkorange')

    if v1Manuever == 0 and v2Manuever == 0 and v1Direction == "North" and v2Direction == "East":
        plt.plot([-0.1,0.1],[0.35,0.35], linewidth = '15', color = 'red')
        plt.arrow(0.1, 0.35, 0.005, 0, width = 0.05, color = 'red')

        plt.plot([0.4,0.4],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0.4, .2, 0, 0.005, width = 0.05, color = 'darkorange')

    if v1Manuever == 0 and v2Manuever == 0 and v1Direction == "North" and v2Direction == "East":
        plt.plot([-0.1,0.1],[-0.05,-0.05], linewidth = '15', color = 'red')
        plt.arrow(0.1, -0.05, 0.005, 0, width = 0.05, color = 'red')

        plt.plot([0.4,0.4],[0.2,0.4], linewidth = '15', color = 'darkorange')
        plt.arrow(0.4, .2, 0, -0.005, width = 0.05, color = 'darkorange')

    if v1Manuever == 0 and v2Manuever == 0 and v1Direction == "South" and v2Direction == "East":
        plt.plot([-0.1,0.1],[-0.05,-0.05], linewidth = '15', color = 'red')
        plt.arrow(0.1, -0.05, 0.005, 0, width = 0.05, color = 'red')

        plt.plot([0.4,0.4],[0.2,0.4], linewidth = '15', color = 'darkorange')
        plt.arrow(0.4, .2, 0, -0.005, width = 0.05, color = 'darkorange')

    if v1Manuever == 0 and v2Manuever == 0 and v1Direction == "South" and v2Direction == "West":
        plt.plot([0.3,0.5],[-0.05,-0.05], linewidth = '15', color = 'red')
        plt.arrow(0.3, -0.05, -0.005, 0, width = 0.05, color = 'red')

        plt.plot([0,0],[0.2,0.4], linewidth = '15', color = 'darkorange')
        plt.arrow(0, .2, 0, -0.005, width = 0.05, color = 'darkorange')

    if v1Manuever == 0 and v2Manuever == 90 and v1Direction == "North" and v2Direction == "North":
        x = np.array([-0.1, 0.05, 0.1,0.12])
        y = np.array([0, 0.3, 0.3,0.3])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)      
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0.12, .3, 0.005, 0, width = 0.05, color = 'red')

        plt.plot([0.4,0.4],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0.4, .2, 0, 0.005, width = 0.05, color = 'darkorange')

    if v1Manuever == 0 and v2Manuever == 90 and v1Direction == "North" and v2Direction == "West":
        x = np.array([0.245,0.25, 0.4,0.45,0.5,0.55])
        y = np.array([0.355,0.34, 0.1,0.1, 0.1,0.1])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0.25, .37, 0, 0.005, width = 0.05, color = 'red')

        plt.plot([0,0],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0, .2, 0, 0.005, width = 0.05, color = 'darkorange')

    #use direction data to figure out direction and understand to find x or y value when comparing.
    #map symbol for Object1
    if v1Manuever == "North" and v2Manuever == "North" and v1Direction == v2Direction :

        plt.rcParams["figure.figsize"] = [3.5, 3.5]
        plt.rcParams["figure.autolayout"] = True
        fig = plt.figure()
        ax = fig.add_subplot()
        circle1 = plt.Circle((0.2, 0.2), radius=0.5, color='grey')
        ax.add_patch(circle1)


        plt.plot([0.2,0.2],[0.25,0.45], linewidth = '15', color = 'red')
        x_values = [0.1,0.3,0.2,0.1]
        y_values = [0.45,0.45,0.55,0.45]

        for i in range (0,4):
            x_values[i] = 3.5 + (x_values[i] - 3.5) * math.cos(v1Direction) * x_values[i] - (y_values[i] - 3.5) * math.sin(v1Direction) * y_values[i]
            y_values[i] = 3.5 + (x_values[i] - 3.5) * math.sin(v1Direction) * x_values[i] + (y_values[i] - 3.5) * math.cos(v1Direction) * y_values[i]

        plt.plot(x_values2,y_values2, linewidth = '1', color = 'red')
        plt.fill_between(x_values2,y_values2, color = 'red')

        plt.plot([0.2,0.2],[-0.1,0.1], linewidth = '15', color = 'darkorange')
        x_values2 = [0.1,0.3,0.2,0.1]
        y_values2 = [0.1,0.1,0.2,0.1]

        for i in range (0,4):
            x_values2[i] = 3.5 + (x_values2[i] - 3.5) * math.cos(v1Direction) * x_values2[i] - (y_values2[i] - 3.5) * math.sin(v1Direction) * y_values2[i]
            y_values2[i] = 3.5 + (x_values2[i] - 3.5) * math.sin(v1Direction) * x_values2[i] + (y_values2[i] - 3.5) * math.cos(v1Direction) * y_values2[i]

        plt.plot(x_values2,y_values2, linewidth = '1', color = 'darkorange')
        plt.fill_between(x_values2,y_values2, color = 'darkorange')

        fig.savefig('plotcircles.png')

    # Turning off axis and saving image as a png picture that can be then placed in desired location on intersection.
    plt.axis("off")
    fig.savefig('plotcircles.png')
    original_Image = Image.open("./plotcircles.png")
    original_Image.show()
