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

class Symbol:
    # Case by Case Approach
    def __init__ (v1Manuever, v2Manuever, v1Direction, v2Direction, xCord, yCord):
        this.v1Manuever = v1Manuever
        this.v2Manuever = v2Manuever
        this.v1Direction = v1Direction
        this.v2Direction = v2Direction
        this.xCord = conflict_point_location[0]
        this.yCord = conflict_point_location[1]

    # Setting up graph itself.
    plt.rcParams["figure.figsize"] = [3.5, 3.5]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    ax = fig.add_subplot()
    circle1 = plt.Circle((0.2, 0.2), radius=0.5, color='grey')
    ax.add_patch(circle1)

    # Common Crashes related to Two Trajectories
    # Manuevers: 0 = Straight, 90 = Left Turn, -90 = Right Turn
    # Direction: North, South, East, West
    if v1Manuever == 0 and v2Manuever == 0 and v1Direction == "North" and v2Direction == "West":
        # Drawing Vehicle 1 arrow.
        plt.plot([0,0],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0, .2, 0, 0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        plt.plot([0.3,0.5],[0.35,0.35], linewidth = '15', color = 'red')
        plt.arrow(0.3, 0.35, -0.005, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")

    if v1Manuever == 0 and v2Manuever == 0 and v1Direction == "North" and v2Direction == "East":
        # Drawing Vehicle 1 arrow.
        plt.plot([0.4,0.4],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0.4, .2, 0, 0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        plt.plot([-0.1,0.1],[0.35,0.35], linewidth = '15', color = 'red')
        plt.arrow(0.1, 0.35, 0.005, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")

    if v1Manuever == 0 and v2Manuever == 0 and v1Direction == "South" and v2Direction == "West":
        # Drawing Vehicle 1 arrow.
        plt.plot([0.4,0.4],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0.4, .2, 0, 0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        plt.plot([-0.1,0.1],[0.35,0.35], linewidth = '15', color = 'red')
        plt.arrow(0.1, 0.35, 0.005, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.rotate(180)

    if v1Manuever == 0 and v2Manuever == 0 and v1Direction == "South" and v2Direction == "East":
        # Drawing Vehicle 1 arrow.
        plt.plot([0.4,0.4],[0.2,0.4], linewidth = '15', color = 'darkorange')
        plt.arrow(0.4, .2, 0, -0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        plt.plot([-0.1,0.1],[-0.05,-0.05], linewidth = '15', color = 'red')
        plt.arrow(0.1, -0.05, 0.005, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")

    if v1Manuever == 0 and v2Manuever == -90 and v1Direction == "North" and v2Direction == "North":
        # Drawing Vehicle 1 arrow.
        plt.plot([0.4,0.4],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0.4, .2, 0, 0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([-0.1, 0.05, 0.1,0.12])
        y = np.array([0, 0.3, 0.3,0.3])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)      
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0.12, .3, 0.005, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")

    if v1Manuever == 0 and v2Manuever == -90 and v1Direction == "North" and v2Direction == "West":
        # Drawing Vehicle 1 arrow.
        plt.plot([0,0],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0, .2, 0, 0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([0.245,0.25, 0.4,0.45,0.5,0.55])
        y = np.array([0.355,0.34, 0.1,0.1, 0.1,0.1])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0.25, .37, 0, 0.005, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")

    if v1Manuever == 0 and v2Manuever == -90 and v1Direction == "South" and v2Direction == "South":
        # Drawing Vehicle 1 arrow.
        plt.plot([0.4,0.4],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0.4, .2, 0, 0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([-0.1, 0.05, 0.1,0.12])
        y = np.array([0, 0.3, 0.3,0.3])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)      
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0.12, .3, 0.005, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.rotate(180)

    if v1Manuever == 0 and v2Manuever == -90 and v1Direction == "South" and v2Direction == "East":
        # Drawing Vehicle 1 arrow.
        plt.plot([0,0],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0, .2, 0, 0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([0.245,0.25, 0.4,0.45,0.5,0.55])
        y = np.array([0.355,0.34, 0.1,0.1, 0.1,0.1])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0.25, .37, 0, 0.005, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.rotate(180)
    
    if v1Manuever == 0 and v2Manuever == -90 and v1Direction == "West" and v2Direction == "West":
        # Drawing Vehicle 1 arrow.
        plt.plot([0.4,0.4],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0.4, .2, 0, 0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([-0.1, 0.05, 0.1,0.12])
        y = np.array([0, 0.3, 0.3,0.3])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)      
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0.12, .3, 0.005, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.rotate(90)

    if v1Manuever == 0 and v2Manuever == -90 and v1Direction == "East" and v2Direction == "East":
        # Drawing Vehicle 1 arrow.
        plt.plot([0.4,0.4],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0.4, .2, 0, 0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([-0.1, 0.05, 0.1,0.12])
        y = np.array([0, 0.3, 0.3,0.3])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)      
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0.12, .3, 0.005, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.rotate(270)

    if v1Manuever == 0 and v2Manuever == 90 and v1Direction == "North" and v2Direction == "North":
        # Drawing Vehicle 1 arrow.
        plt.plot([0.4,0.4],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0.4, .2, 0, 0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([-0.1, 0.05, 0.1,0.12])
        y = np.array([0, 0.3, 0.3,0.3])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)      
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0.12, .3, 0.005, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)

    if v1Manuever == 0 and v2Manuever == 90 and v1Direction == "North" and v2Direction == "South":
        # Drawing Vehicle 1 arrow.
        plt.plot([0.33,0.33],[0.35,0.55], linewidth = '15', color = 'darkorange')
        plt.arrow(0.33, .32, 0, -0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([-0.1, 0.05, 0.1,0.12])
        y = np.array([-.1, 0.1, 0.1,0.1])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0.07, .1, 0.005, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        original_image = original_image.rotate(180)

    if v1Manuever == 0 and v2Manuever == 90 and v1Direction == "North" and v2Direction == "West":
        # Drawing Vehicle 1 arrow.
        x = np.array([-0.2, -0.05, 0.0025-0.05,0])
        y = np.array([0, 0.2, 0.2,0.2])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot([0.44,0.64],[0.2,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0.44, .2, -0.000000001, 0, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([-0.2, -0.05, 0.0025-0.05,0])
        y = np.array([0, 0.2, 0.2,0.2])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0, .2, 0.000001, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        original_image = original_image.rotate(90)

    if v1Manuever == 0 and v2Manuever == 90 and v1Direction == "North" and v2Direction == "East":
        # Drawing Vehicle 1 arrow.
        plt.plot([0,0],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0, .2, 0, 0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([0.245,0.25, 0.4,0.45,0.5,0.55])
        y = np.array([0.355,0.34, 0.1,0.1, 0.1,0.1])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0.25, .37, 0, 0.005, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)

    if v1Manuever == 0 and v2Manuever == 90 and v1Direction == "South" and v2Direction == "South":
        # Drawing Vehicle 1 arrow.
        plt.plot([0.4,0.4],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0.4, .2, 0, 0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([-0.1, 0.05, 0.1,0.12])
        y = np.array([0, 0.3, 0.3,0.3])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)      
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0.12, .3, 0.005, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        original_image = original_image.rotate(180)

    if v1Manuever == 0 and v2Manuever == 90 and v1Direction == "South" and v2Direction == "West":
        # Drawing Vehicle 1 arrow.
        plt.plot([0,0],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0, .2, 0, 0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([0.245,0.25, 0.4,0.45,0.5,0.55])
        y = np.array([0.355,0.34, 0.1,0.1, 0.1,0.1])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0.25, .37, 0, 0.005, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        original_image = original_image.rotate(180)

    if v1Manuever == 0 and v2Manuever == 90 and v1Direction == "South" and v2Direction == "West":
        # Drawing Vehicle 1 arrow.
        x = np.array([-0.2, -0.05, 0.0025-0.05,0])
        y = np.array([0, 0.2, 0.2,0.2])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot([0.44,0.64],[0.2,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0.44, .2, -0.000000001, 0, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([-0.2, -0.05, 0.0025-0.05,0])
        y = np.array([0, 0.2, 0.2,0.2])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0, .2, 0.000001, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        original_image = original_image.rotate(270)

    if v1Manuever == 0 and v2Manuever == 90 and v1Direction == "West" and v2Direction == "West":
        # Drawing Vehicle 1 arrow.
        plt.plot([0.4,0.4],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0.4, .2, 0, 0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([-0.1, 0.05, 0.1,0.12])
        y = np.array([0, 0.3, 0.3,0.3])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)      
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0.12, .3, 0.005, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        original_image = original_image.rotate(90)

    if v1Manuever == 0 and v2Manuever == 90 and v1Direction == "West" and v2Direction == "East":
        # Drawing Vehicle 1 arrow.
        plt.plot([0.33,0.33],[0.35,0.55], linewidth = '15', color = 'darkorange')
        plt.arrow(0.33, .32, 0, -0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([-0.1, 0.05, 0.1,0.12])
        y = np.array([-.1, 0.1, 0.1,0.1])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0.07, .1, 0.005, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        original_image = original_image.rotate(270)

    if v1Manuever == 0 and v2Manuever == 90 and v1Direction == "East" and v2Direction == "East":
        # Drawing Vehicle 1 arrow.
        plt.plot([0.4,0.4],[0,0.2], linewidth = '15', color = 'darkorange')
        plt.arrow(0.4, .2, 0, 0.005, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([-0.1, 0.05, 0.1,0.12])
        y = np.array([0, 0.3, 0.3,0.3])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)      
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0.12, .3, 0.005, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        original_image = original_image.rotate(270)

    if v1Manuever == -90 and v2Manuever == 0 and v1Direction == "North" and v2Direction == "East":
        # Drawing Vehicle 1 arrow.
        x = np.array([0.245,0.25, 0.4,0.45,0.5,0.55])
        y = np.array([0.355,0.34, 0.1,0.1, 0.1,0.1])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'darkOrange')
        plt.arrow(0.25, .37, 0, 0.005, width = 0.05, color = 'darkOrange')

        # Drawing Vehicle 2 arrow.
        plt.plot([0,0],[0,0.2], linewidth = '15', color = 'red')
        plt.arrow(0, .2, 0, 0.005, width = 0.05, color = 'red')


        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.rotate(270)

    if v1Manuever == -90 and v2Manuever == 0 and v1Direction == "South" and v2Direction == "West":
        # Drawing Vehicle 1 arrow.
        x = np.array([0.245,0.25, 0.4,0.45,0.5,0.55])
        y = np.array([0.355,0.34, 0.1,0.1, 0.1,0.1])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'darkOrange')
        plt.arrow(0.25, .37, 0, 0.005, width = 0.05, color = 'darkOrange')

        # Drawing Vehicle 2 arrow.
        plt.plot([0,0],[0,0.2], linewidth = '15', color = 'red')
        plt.arrow(0, .2, 0, 0.005, width = 0.05, color = 'red')


        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.rotate(90)

    if v1Manuever == 90 and v2Manuever == 0 and v1Direction == "North" and v2Direction == "South":
        # Drawing Vehicle 1 arrow.
        x = np.array([-0.1, 0.05, 0.1,0.12])
        y = np.array([-.1, 0.1, 0.1,0.1])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'darkOrange')
        plt.arrow(0.07, .1, 0.005, 0, width = 0.05, color = 'darkOrange')

        # Drawing Vehicle 2 arrow.
        plt.plot([0.33,0.33],[0.35,0.55], linewidth = '15', color = 'red')
        plt.arrow(0.33, .32, 0, -0.005, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)

    if v1Manuever == 90 and v2Manuever == 0 and v1Direction == "North" and v2Direction == "West":
        # Drawing Vehicle 1 arrow.
        x = np.array([0.245,0.25, 0.4,0.45,0.5,0.55])
        y = np.array([0.355,0.34, 0.1,0.1, 0.1,0.1])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'darkOrange')
        plt.arrow(0.25, .37, 0, 0.005, width = 0.05, color = 'darkOrange')

        # Drawing Vehicle 2 arrow.
        plt.plot([0,0],[0,0.2], linewidth = '15', color = 'red')
        plt.arrow(0, .2, 0, 0.005, width = 0.05, color = 'red')


        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.rotate(270)
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)

    if v1Manuever == 90 and v2Manuever == 0 and v1Direction == "North" and v2Direction == "East":
        # Drawing Vehicle 1 arrow.
        x = np.array([-0.2, -0.05, 0.0025-0.05,0])
        y = np.array([0, 0.2, 0.2,0.2])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'darkorange')
        plt.arrow(0, .2, 0.000001, 0, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        plt.plot([0.44,0.64],[0.2,0.2], linewidth = '15', color = 'red')
        plt.arrow(0.44, .2, -0.000000001, 0, width = 0.05, color = 'red')


        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)

    if v1Manuever == 90 and v2Manuever == 0 and v1Direction == "South" and v2Direction == "West":
        # Drawing Vehicle 1 arrow.
        x = np.array([-0.2, -0.05, 0.0025-0.05,0])
        y = np.array([0, 0.2, 0.2,0.2])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'darkorange')
        plt.arrow(0, .2, 0.000001, 0, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        plt.plot([0.44,0.64],[0.2,0.2], linewidth = '15', color = 'red')
        plt.arrow(0.44, .2, -0.000000001, 0, width = 0.05, color = 'red')


        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        original_image = original_image.rotate(180)

    if v1Manuever == 90 and v2Manuever == 0 and v1Direction == "South" and v2Direction == "East":
        # Drawing Vehicle 1 arrow.
        x = np.array([0.245,0.25, 0.4,0.45,0.5,0.55])
        y = np.array([0.355,0.34, 0.1,0.1, 0.1,0.1])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'darkOrange')
        plt.arrow(0.25, .37, 0, 0.005, width = 0.05, color = 'darkOrange')

        # Drawing Vehicle 2 arrow.
        plt.plot([0,0],[0,0.2], linewidth = '15', color = 'red')
        plt.arrow(0, .2, 0, 0.005, width = 0.05, color = 'red')


        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.rotate(90)
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)

    if v1Manuever == 90 and v2Manuever == 0 and v1Direction == "West" and v2Direction == "East":
        # Drawing Vehicle 1 arrow.
        x = np.array([-0.1, 0.05, 0.1,0.12])
        y = np.array([-.1, 0.1, 0.1,0.1])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'darkOrange')
        plt.arrow(0.07, .1, 0.005, 0, width = 0.05, color = 'darkOrange')

        # Drawing Vehicle 2 arrow.
        plt.plot([0.33,0.33],[0.35,0.55], linewidth = '15', color = 'red')
        plt.arrow(0.33, .32, 0, -0.005, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        original_image = original_image.rotate(90)

    if v1Manuever == 90 and v2Manuever == 90 and v1Direction == "North" and v2Direction == "West":
        # Drawing Vehicle 1 arrow.
        x = np.array([-0.2, -0.05, 0.0025-0.05,0])
        y = np.array([0, 0.2, 0.2,0.2])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'darkorange')
        plt.arrow(0, .2, 0.000001, 0, width = 0.05, color = 'darkorange')
            
        # Drawing Vehicle 2 arrow.
        z = np.array([0.02, 0.05, 0.15, 0.17, 0.2, 0.3,0.301])
        w = np.array([0.55,0.5455, 0.45, 0.449, 0.43, 0.35,0.35])
        Z_W_Spline = make_interp_spline(z, w)
        Z_ = np.linspace(z.min(), z.max(), 1000)
        W_ = Z_W_Spline(Z_)
        plt.plot(Z_,W_, linewidth = '15', color = 'red')
        plt.arrow(0.301, .37, 0, -0.000001, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)

    if v1Manuever == 90 and v2Manuever == 90 and v1Direction == "North" and v2Direction == "East":
        # Drawing Vehicle 1 arrow.
        z = np.array([0.02, 0.05, 0.15, 0.17, 0.2, 0.3,0.301])
        w = np.array([0.55,0.5455, 0.45, 0.449, 0.43, 0.35,0.35])
        Z_W_Spline = make_interp_spline(z, w)
        Z_ = np.linspace(z.min(), z.max(), 1000)
        W_ = Z_W_Spline(Z_)
        plt.plot(Z_,W_, linewidth = '15', color = 'darkorange')
        plt.arrow(0.301, .37, 0, -0.000001, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([-0.2, -0.05, 0.0025-0.05,0])
        y = np.array([0, 0.2, 0.2,0.2])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0, .2, 0.000001, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        original_image = original_image.rotate(270)

    if v1Manuever == 90 and v2Manuever == 90 and v1Direction == "South" and v2Direction == "West":
        # Drawing Vehicle 1 arrow.
        z = np.array([0.02, 0.05, 0.15, 0.17, 0.2, 0.3,0.301])
        w = np.array([0.55,0.5455, 0.45, 0.449, 0.43, 0.35,0.35])
        Z_W_Spline = make_interp_spline(z, w)
        Z_ = np.linspace(z.min(), z.max(), 1000)
        W_ = Z_W_Spline(Z_)
        plt.plot(Z_,W_, linewidth = '15', color = 'darkorange')
        plt.arrow(0.301, .37, 0, -0.000001, width = 0.05, color = 'darkorange')

        # Drawing Vehicle 2 arrow.
        x = np.array([-0.2, -0.05, 0.0025-0.05,0])
        y = np.array([0, 0.2, 0.2,0.2])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'red')
        plt.arrow(0, .2, 0.000001, 0, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        original_image = original_image.rotate(90)

    if v1Manuever == 90 and v2Manuever == 90 and v1Direction == "South" and v2Direction == "East":
        # Drawing Vehicle 1 arrow.
        x = np.array([-0.2, -0.05, 0.0025-0.05,0])
        y = np.array([0, 0.2, 0.2,0.2])
        X_Y_Spline = make_interp_spline(x, y)
        X_ = np.linspace(x.min(), x.max(), 1000)
        Y_ = X_Y_Spline(X_)
        plt.plot(X_,Y_, linewidth = '15', color = 'darkorange')
        plt.arrow(0, .2, 0.000001, 0, width = 0.05, color = 'darkorange')
            
        # Drawing Vehicle 2 arrow.
        z = np.array([0.02, 0.05, 0.15, 0.17, 0.2, 0.3,0.301])
        w = np.array([0.55,0.5455, 0.45, 0.449, 0.43, 0.35,0.35])
        Z_W_Spline = make_interp_spline(z, w)
        Z_ = np.linspace(z.min(), z.max(), 1000)
        W_ = Z_W_Spline(Z_)
        plt.plot(Z_,W_, linewidth = '15', color = 'red')
        plt.arrow(0.301, .37, 0, -0.000001, width = 0.05, color = 'red')

        # Remove plot details and then save produced as an image to then rotate if necessary.
        plt.axis("off")
        fig.savefig('plotcircles.png')
        original_image = Image.open("./plotcircles.png")
        original_image = original_image.transpose(method=Image.FLIP_LEFT_RIGHT)
        original_image = original_image.rotate(180)

    # Produce image
    original_image.show()

