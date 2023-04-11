#Importing Modules
import pandas as pd
# import numpy as np
# import re
from pprint import pprint
import matplotlib.pyplot as plt
import math
# import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
import os

# Grouping Approach
class Symbol:
    def __init__(self, v1direction, v1manuever, v2direction, v2manuever, stationary_present, stationary_direction, side_swipe):
        self.v1manuever = v1manuever
        self.v2manuever = v2manuever
        self.v1direction = v1direction
        self.v2direction = v2direction
        self.v1 = (v1direction, v1manuever)
        self.v2 = (v2direction, v2manuever)
        self.side_swipe = side_swipe
        self.stationary_present = stationary_present
        self.stationary_direction = stationary_direction
        
        self.counter = 1
        self.adjust_v2 = 0
        self.adjust_vx = 0
        self.adjust_vy = 0
        
    def plot(self):

        # SETTING UP GRAPH FOR PLOTTING
        plt.rcParams["figure.figsize"] = [3.5,3.5]
        plt.rcParams["figure.autolayout"] = True
        fig = plt.figure()
        ax = fig.add_subplot()
        circle1 = plt.Circle((0.2, 0.2), radius=0.5, facecolor='grey', edgecolor='black', linewidth=15)

        ax.add_patch(circle1)
        plt.axis("off")

        #ALL STATIONARY OBJECTS
        # Plot pedestrian or bicycle arrowhead
        if (self.stationary_present == "Bicycle" or self.stationary_present == "Pedestrian"):
            if (self.stationary_direction == "North"):
                plt.arrow(0.2, 0, 0, 0.001, head_width=0.35, head_length=0.35, color = 'lightblue')
            elif (self.stationary_direction == "South"):
                plt.arrow(0.2, 0.3, 0, -0.001, head_width=0.35, head_length=0.35, color = 'lightblue')
            elif (self.stationary_direction == "West"):
                    plt.arrow(0.3, 0.2, -0.001, 0, head_width=0.35, head_length=0.35, color = 'lightblue')
            elif (self.stationary_direction == "East"):
                plt.arrow(0.1, 0.2, 0.001, 0, head_width=0.35, head_length=0.35, color = 'lightblue')
        # Plot pedestrian or bicycle arrowhead
        if (self.stationary_present == "Pedestrian"):
            # Draw the body
            ax.plot([0.2, 0.2], [0.2, 0.15], linewidth=3, color='black')
            # Draw the legs
            ax.plot([0.2, 0.17], [0.15, 0.05], linewidth=3, color='black')
            ax.plot([0.2, 0.23], [0.15, 0.05], linewidth=3, color='black')
            # Draw the arms
            ax.plot([0.2, 0.15], [0.2, 0.23], linewidth=3, color='black')
            ax.plot([0.2, 0.25], [0.2, 0.23], linewidth=3, color='black')
            # Draw the head
            ax.add_patch(plt.Circle((0.2, 0.25), radius=0.03, color='black'))
        elif (self.stationary_present == "Bicycle"):
            # Draw bicycle
            wheel1 = plt.Circle((0.15, 0.15), radius=0.02, color='black')
            wheel2 = plt.Circle((0.25, 0.15), radius=0.02, color='black')
            handle1 = plt.Rectangle((0.1, 0.2), 0.1, 0.01, color='black')
            handle2 = plt.Rectangle((0.23, 0.2), 0.05, 0.005, color='black')
            seat = plt.Rectangle((0.18, 0.2), 0.03, 0.015, color='black')
            pedal1 = plt.Rectangle((0.14, 0.13), 0.02, 0.03, color='black')
            pedal2 = plt.Rectangle((0.24, 0.13), 0.02, 0.03, color='black')
            chain = plt.Line2D([0.16, 0.24], [0.13, 0.13], color='black')
            ax.add_patch(wheel1)
            ax.add_patch(wheel2)
            ax.add_patch(handle1)
            ax.add_patch(handle2)
            ax.add_patch(seat)
            ax.add_patch(pedal1)
            ax.add_patch(pedal2)
            ax.add_line(chain)
        # Plot Parked Vehicle
        elif (self.stationary_present == "Parked Vehicle"):
            if (self.stationary_direction == "North"):
                plt.arrow(0.2, 0.1, 0, 0.001, width = 0.05, color = 'lightblue')
            elif (self.stationary_direction == "South"):
                plt.arrow(0.2, 0.3, 0, -0.001, width = 0.05, color = 'lightblue')
            elif (self.stationary_direction == "West"):
                plt.arrow(0.3, 0.2, -0.001, 0, width = 0.05, color = 'lightblue')
            elif (self.stationary_direction == "East"):
                plt.arrow(0.1, 0.2, 0.001, 0, width = 0.05, color = 'lightblue')

        # PLOTTING VEHICLE ARROWS
        def v_arrow(v, arrow_color):
            straight = "Straight"
            right = "Turning Right"
            left = "Turning Left"

            if (self.side_swipe == False):
                if self.counter %2 == 0:
                    if ((self.v1 == self.v2) or
                        (self.v1 == ("North",right) and self.v2 == ("East",straight)) or (self.v2 == ("North",right) and self.v1 == ("East",straight)) or 
                        (self.v1 == ("South",right) and self.v2 == ("West",straight)) or (self.v2 == ("South",right) and self.v1 == ("West",straight)) or
                    (self.v1 == ("West",right) and self.v2 == ("North",straight)) or (self.v2 == ("West",right) and self.v1 == ("North",straight)) or
                    (self.v1 == ("East",right) and self.v2 == ("South",straight)) or (self.v2 == ("East",right) and self.v1 == ("South",straight)) or

                        (self.v1 == ("North",left) and self.v2 == ("West",straight)) or (self.v2 == ("North",left) and self.v1 == ("West",straight)) or
                        (self.v1 == ("South",left) and self.v2 == ("East",straight)) or (self.v2 == ("South",left) and self.v1 == ("East",straight)) or
                        (self.v1 == ("West",left) and self.v2 == ("South",straight)) or (self.v2 == ("West",left) and self.v1 == ("South",straight)) or
                        (self.v1 == ("East",left) and self.v2 == ("North",straight)) or (self.v2 == ("East",left) and self.v1 == ("North",straight)) or 
                        
                        (self.v1 == ("North",left) and self.v2 == ("South",right)) or (self.v2 == ("North",left) and self.v1 == ("South",right)) or
                        (self.v1 == ("South",left) and self.v2 == ("North",right)) or (self.v2 == ("South",left) and self.v1 == ("North",right)) or
                        (self.v1 == ("West",left) and self.v2 == ("East",right)) or (self.v2 == ("West",left) and self.v1 == ("East",right)) or
                        (self.v1 == ("East",left) and self.v2 == ("West",right)) or (self.v2 == ("East",left) and self.v1 == ("West",right)) 
                    ):
                        self.adjust_v2= 0.5
                    else:
                        self.adjust_v2 = 0
                # Straight Vector (aka Through Turn Vector)
                if (v == ("North", straight)):
                    plt.arrow(0.2, -.3 + self.adjust_v2, 0, 0.25, width = 0.05, color = arrow_color)
                if (v == ("South", straight)):
                    plt.arrow(0.2, .7 - self.adjust_v2, 0, -0.25, width = 0.05, color = arrow_color)
                if (v == ("West", straight)):
                    plt.arrow(0.7 - self.adjust_v2, 0.2, -0.25, 0, width = 0.05, color = arrow_color)
                if (v == ("East", straight)):
                    plt.arrow(-0.3 + self.adjust_v2, 0.2, 0.25, 0, width = 0.05, color = arrow_color)

                # Turning Right Vector
                if (v == ("North", right)):
                    plt.plot([-0.2+self.adjust_v2,-0.2+self.adjust_v2],[0,0.2], linewidth = '10', color = arrow_color)
                    plt.arrow(-0.2+self.adjust_v2, 0.2, 0.15, 0, width = 0.05, color = arrow_color)
                if (v == ("South", right)):
                    plt.plot([0.6 - self.adjust_v2,.6 - self.adjust_v2],[0.2,0.4], linewidth = '10', color = arrow_color)
                    plt.arrow(0.6 - self.adjust_v2, 0.2, -0.15, 0, width = 0.05, color = arrow_color)
                if (v == ("West", right)):
                    plt.plot([0.2,0.4], [-0.2+self.adjust_v2,-0.2+self.adjust_v2], linewidth = '10', color = arrow_color)
                    plt.arrow(0.2,-0.2+self.adjust_v2, 0, 0.15, width = 0.05, color = arrow_color)
                if (v == ("East", right)):
                    plt.plot([0,0.2],[0.6 - self.adjust_v2,.6 - self.adjust_v2], linewidth = '10', color = arrow_color)
                    plt.arrow(0.2, 0.6 - self.adjust_v2, 0, -0.15, width = 0.05, color = arrow_color)
                    
                # Turning Left Vector
                if (v == ("North", left)):
                    plt.plot([0.6 - self.adjust_v2,.6 - self.adjust_v2],[0,0.2], linewidth = '10', color = arrow_color)
                    plt.arrow(0.6 - self.adjust_v2, 0.2, -0.15, 0, width = 0.05, color = arrow_color)
                if (v == ("South", left)):
                    plt.plot([-0.2+self.adjust_v2,-0.2+self.adjust_v2],[0.2,0.4], linewidth = '10', color = arrow_color)
                    plt.arrow(-0.2+self.adjust_v2, 0.2, 0.15, 0, width = 0.05, color = arrow_color)
                if (v == ("West", left)):
                    plt.plot([0.2,0.4],[0.6 - self.adjust_v2,.6 - self.adjust_v2], linewidth = '10', color = arrow_color)
                    plt.arrow(0.2, 0.6 - self.adjust_v2, 0, -0.15, width = 0.05, color = arrow_color)
                if (v == ("East", left)):
                    plt.plot([0.,0.2], [-0.2+self.adjust_v2,-0.2+self.adjust_v2], linewidth = '10', color = arrow_color)
                    plt.arrow(0.2,-0.2+self.adjust_v2, 0, 0.15, width = 0.05, color = arrow_color)
                    # v1 = v2
                # Special Cases
                self.counter += 1
            # Side-Swipe Crashes
            else:
                if (self.v1manuever == self.v2manuever):
                    self.adjust_vy= 0.25
                    if self.counter %2 == 0:
                        if (self.v1 == self.v2):
                            self.adjust_vx = 0.25
                        else:
                            self.adjust_vx = -0.25
                            
                    if self.counter %2 == 0:
                        self.adjust_v3 = 0.15
                    else:
                        self.adjust_v3 = -0.15

                    # Straight Same Direction Side-Swipes
                    if (self.v1 == self.v2 and self.v1manuever == straight):          
                        if (v == ("North", straight)):
                            plt.arrow(0.3 - self.adjust_vx, -.3 + self.adjust_vy, 0, 0.25, width = 0.05, color = arrow_color)
                        if (v == ("South", straight)):
                            plt.arrow(0.3 - self.adjust_vx, .7 - self.adjust_vy, 0, -0.25, width = 0.05, color = arrow_color)
                        if (v == ("West", straight)):
                            plt.arrow(0.7 - self.adjust_vy, 0.1 + self.adjust_vx, -0.25, 0, width = 0.05, color = arrow_color)
                        if (v == ("East", straight)):
                            plt.arrow(-0.3 + self.adjust_vy, 0.1 + self.adjust_vx, 0.25, 0, width = 0.05, color = arrow_color)
                    # Straight Opposite Direction Side-Swipes
                    elif (self.v1manuever == straight and self.v2manuever == straight):
                        if (v == ("North", straight)):
                            plt.arrow(0.1 - self.adjust_vx, -.3 + self.adjust_vy, 0, 0.25, width = 0.05, color = arrow_color)
                        if (v == ("South", straight)):
                            plt.arrow(0.1 - self.adjust_vx, .7 - self.adjust_vy, 0, -0.25, width = 0.05, color = arrow_color)
                        if (v == ("West", straight)):
                            plt.arrow(0.7 - self.adjust_vy, 0.3 + self.adjust_vx, -0.25, 0, width = 0.05, color = arrow_color)
                        if (v == ("East", straight)):
                            plt.arrow(-0.3 + self.adjust_vy, 0.3 + self.adjust_vx, 0.25, 0, width = 0.05, color = arrow_color)
                
                    elif ((self.v1manuever == right and self.v2manuever == right) or (self.v1manuever == left and self.v2manuever == left)):
                       # Turning Right Vector
                        if (v == ("North", right)):
                            plt.plot([0.1+self.adjust_v3,0.1+self.adjust_v3],[0-self.adjust_v3,0.2-self.adjust_v3], linewidth = '10', color = arrow_color)
                            plt.arrow(0.1+self.adjust_v3, 0.2-self.adjust_v3, 0.15, 0, width = 0.05, color = arrow_color)       

                        if (v == ("South", right)):
                            plt.plot([0.3 -self.adjust_v3,.3 -self.adjust_v3],[0.1+self.adjust_v3,0.3+self.adjust_v3], linewidth = '10', color = arrow_color)
                            plt.arrow(0.3 -self.adjust_v3, 0.1+self.adjust_v3, -0.15, 0, width = 0.05, color = arrow_color)

                        if (v == ("West", right)):
                            plt.plot([0.1 +self.adjust_v3,0.3 +self.adjust_v3], [0.1+self.adjust_v3, 0.1+self.adjust_v3], linewidth = '10', color = arrow_color)
                            plt.arrow(0.1 +self.adjust_v3,0.1+self.adjust_v3, 0, 0.15, width = 0.05, color = arrow_color)
                        if (v == ("East", right)):
                            plt.plot([0.1-self.adjust_v3,0.3 -self.adjust_v3],[0.3-self.adjust_v3, 0.3-self.adjust_v3], linewidth = '10', color = arrow_color)
                            plt.arrow(0.3 -self.adjust_v3,0.3-self.adjust_v3, 0, -0.15, width = 0.05, color = arrow_color)
                            
                        # Turning Left Vector
                        if (v == ("North", left)):
                            plt.plot([0.3 -self.adjust_v3,.3-self.adjust_v3],[0-self.adjust_v3,0.2-self.adjust_v3], linewidth = '10', color = arrow_color)
                            plt.arrow(0.3-self.adjust_v3, 0.2-self.adjust_v3, -0.15, 0, width = 0.05, color = arrow_color)
                            
                        if (v == ("South", left)):
                            plt.plot([0.1+self.adjust_v3,0.1+self.adjust_v3],[0.1+self.adjust_v3,0.3+self.adjust_v3], linewidth = '10', color = arrow_color)
                            plt.arrow(0.1+self.adjust_v3, 0.1+self.adjust_v3, 0.15, 0, width = 0.05, color = arrow_color)
                            
                        if (v == ("West", left)):
                            plt.plot([0.1+self.adjust_v3,0.3+self.adjust_v3],[0.3 - self.adjust_v3,.3 - self.adjust_v3], linewidth = '10', color = arrow_color)
                            plt.arrow(0.1+self.adjust_v3, 0.3 - self.adjust_v3, 0, -0.15, width = 0.05, color = arrow_color)
                            
                        if (v == ("East", left)):
                            plt.plot([0.1-self.adjust_v3,0.3-self.adjust_v3], [0.1+self.adjust_v3,0.1+self.adjust_v3], linewidth = '10', color = arrow_color)
                            plt.arrow(0.3-self.adjust_v3,0.1+self.adjust_v3, 0, 0.15, width = 0.05, color = arrow_color)  
            
                    self.counter += 1
        # Plotting Vehicles
        v_arrow(self.v1, 'red')
        v_arrow(self.v2,'darkorange')
        
        

symbol = Symbol("North", "Straight", "South", "Straight", "", "North", True)
symbol.plot()
