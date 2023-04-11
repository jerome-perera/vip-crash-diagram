#Importing Modules
import pandas as pd
# import numpy as np
# import re
from pprint import pprint
import matplotlib.pyplot as plt
import math
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
import os
import PythonCleaning

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


class Symbol_Map:
    def data_cleaner(file_name, intersection_center):

        #Reading in file, separating latitude and longitude of center of intersection
        crash_data = pd.read_csv(file_name)
        input_lat = intersection_center[0]
        input_long = intersection_center[1]

        #Coordinates of bounding square
        lat_max = input_lat + 0.0005
        lat_min = input_lat - 0.0005
        long_max = input_long + 0.0005
        long_min = input_long - 0.0005
        
        #A Pandas dataframe, filtering to only include data within coords +- 0.0005 latitude and longitude from intersection_center
        within_intersection = crash_data[(crash_data.loc[:,'Longitude'].astype(float) <= long_max) & \
                                        (crash_data.loc[:,'Longitude'].astype(float) >= long_min) & \
                                        (crash_data.loc[:,'Latitude (Crash Level)'].astype(float) <= lat_max) & \
                                        (crash_data.loc[:,'Latitude (Crash Level)'].astype(float) >= lat_min)]
        
        
        #A Pandas dataframe with maneuvers, directions, and vehicle types for each collision in specified intersection
        #Creating a new dataframe will keep the original intact if other data needs to be extracted at a later time
        for_symbology = within_intersection[['Direction of Movement', 'Vehicle Maneuver (Crash Level) ', 'First Harmful Event']].copy()
        
        #Renaming columns of dataframe for convenience
        for_symbology.rename(columns = {'Vehicle Maneuver (Crash Level) ' : 'Maneuver', 'Direction of Movement' : 'Direction', 'First Harmful Event' : 'Vehicle Type' }, inplace = True)
        
        
        #Simplifying/cleaning vehicle types to pass on to other code
        
        #Dropping rows that are missing data, as that crash cannot be plotted
        #We have already masked the original dataframe to only include Manuever, Direction, and Vehicle Type columns.
        #If any of these pieces of data is missing, it is impossible to plot.
        #In the future, the code will use natural language processing (looking for keywords) in the crash narrative, to fill these empty values.
        for_symbology.dropna(inplace = True, axis = 0)

        
        #Casting string values into lists and manipulating formatting
        for_symbology['Direction'] = for_symbology['Direction'].apply(lambda x:x.replace("[",""))
        for_symbology['Direction'] = for_symbology['Direction'].apply(lambda x:x.replace("]",""))
        for_symbology['Direction'] = for_symbology['Direction'].apply(lambda x:x.replace('''\"''',""))
        for_symbology['Direction'] = for_symbology['Direction'].apply(lambda x:x.split(","))
        
        for_symbology['Maneuver'] = for_symbology['Maneuver'].apply(lambda x:x.replace("[",""))
        for_symbology['Maneuver'] = for_symbology['Maneuver'].apply(lambda x:x.replace("]",""))
        for_symbology['Maneuver'] = for_symbology['Maneuver'].apply(lambda x:x.replace('''\"''',""))
        for_symbology['Maneuver'] = for_symbology['Maneuver'].apply(lambda x:x.split(","))
        
        for_symbology['Vehicle Type'] = for_symbology['Vehicle Type'].apply(lambda x:x.replace("[",""))
        for_symbology['Vehicle Type'] = for_symbology['Vehicle Type'].apply(lambda x:x.replace("]",""))
        for_symbology['Vehicle Type'] = for_symbology['Vehicle Type'].apply(lambda x:x.replace("Motor Vehicle in Motion","Vehicle"))
        for_symbology['Vehicle Type'] = for_symbology['Vehicle Type'].apply(lambda x:x.replace("Parked Motor Vehicle","Parked"))
        for_symbology['Vehicle Type'] = for_symbology['Vehicle Type'].apply(lambda x:x.replace('''\"''',""))
        for_symbology['Vehicle Type'] = for_symbology['Vehicle Type'].apply(lambda x:x.split(","))
        
        #Filtering out rows with crashes with anything other than 2 vehicles (or 1 vehicle, 1 pedestrian). In a future version of the program,
        #cases such as these will be handled. For now, the program will deal with simpler cases.
        #for_symbology = for_symbology[len(for_symbology["Vehicle Type"])]
        num_involved = []
        maneuv_accepted = []
        for eachrow in for_symbology.values:
            num_involved.append(len(eachrow[2])) 
            maneuv_accepted.append("Straight" in eachrow[1] or "Turning Right" in eachrow[1] or "Turning Left" in eachrow[1])
        for_symbology["Num Involved"] = num_involved
        for_symbology["Maneuver Accepted"] = maneuv_accepted
        
        #
        #
        #
        #
        #
        #
        #Separating crash scenarios we are currently capable of handling from those 
        #we will be able to handle in the future. Cases we are not able to 
        #handle will be returned to the user so they can manually plot.
        #________________________________________________________________#
        #1. We can only plot crashes involving 2 vehicles/pedestrian
        for_symbology = for_symbology[for_symbology["Num Involved"] == 2]
        #2. We can only handle the following manuevers: "Straight", "Turning Right", "Turning Left"
        for_symbology = for_symbology[for_symbology["Maneuver Accepted"] == True]
        # Cases we can't plot: _______________________
        #
        #
        #
        #
        #
        

        #Checks the Vehicle Type column for presence of "Pedestrian". Creates new column with boolean values to indicate if pedestrian found. 
        ped_list = []
        for eachrow in for_symbology.values:
            if "Pedestrian" in eachrow[2]:
                ped_list.append(True)
            else:
                ped_list.append(False)   
        for_symbology["PedPresent"] = ped_list
                
        
        for_symbology.reset_index(inplace = True)
        for_symbology.rename(columns = {'index':'Orig. Index'}, inplace = True)
        
        for_symbology_list = for_symbology.values.tolist()
        final_list = []
        for item in for_symbology_list:
            #Each sublist in final_list represents 1 crash. Format is: 
            #v1dir, v1manuev, v2dir, v2manuev, side_swipe, stationary_present, stationary_dir
            
            #If pedestrian not present:
            if "Pedestrian" not in item[3]:
                #If "Changing Lanes" appears as a Maneuver, Sideswipe = True
                if "Changing Lanes" not in item [2]:
                    sub_list = [item[1][0],item[2][0],item[1][1],item[2][1], False, False, False]
                    #sub_list = [v1dir, v1manuev, v1dir, v1manuev, sideswipe=False, stationary_present=False, stationary_dir=False]
                elif "Changing Lanes" in item [2]:#If changing lanes is present, crash must be a sideswipe
                    change_lane_index = item[2].index("Changing Lanes")
                    if change_lane_index == 1:
                        maneuv_index = 0
                    else:
                        maneuv_index = 1
                    sub_list = [item[1][0],item[2][maneuv_index],item[1][1],item[2][maneuv_index], True, False, False]
                    #sub_list = [v1dir, v1manuev, v1dir, v1manuev, sideswipe=True, stationary_present=False, stationary_dir=False]
                
            
            #Else pedestrian present (and None is one of the directions), ensure other direction is 
            #assigned to the vehicle:
            elif "Pedestrian" in item[3]:
                ped_index = item[3].index("Pedestrian")
                none_index = item[1].index("None")
                if ped_index == 1:
                    veh_index = 0
                else:
                    veh_index = 1
                if none_index == 1:
                    veh_dir_index = 0
                else:
                    veh_dir_index = 1
                sub_list = [item[1][veh_dir_index],item[2][0],item[1][none_index], "None", False, True, False]
                #sub_list = [v1dir, v1manuev, peddir, pedmanuver=None, sideswipe=False, stationary_present=True, stationary_dir=False]
            final_list.append(sub_list)
        
        formatted_df = pd.DataFrame(final_list, columns = ["V1 Dir", "V1 Manuev", "V2 Dir", "V2 Maneuv", "Sideswipe", "Stationary Present", "Stationary Dir"])
        for_symbology.to_csv("cleaned_crash_data.csv", index = True)
        formatted_df.to_csv("formatted_data.csv", index = True) #formatted df shows contents of final_list
        
        # pprint(final_list) #final_list is what will be passed onto other parts of code for plotting
        #return for_symbology
        return final_list
        #return pd.concat([for_symbology, formatted_df], axis = 1)


    #INPUT BUTTON
    symbol_list = []



    file = "CollisionsDataset5000ft.csv"
    center = (33.75713, -84.38610)
    for sublist in data_cleaner(file, center):
        symbol_list.append(Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5],sublist[6]))

    # symbol_list.extend((
    #     Symbol("South", "Turning Right", "South", "Turning Right", "Parked Vehicle", "", False), #1
    #     Symbol("South", "Turning Left", "South", "Turning Left", "Parked Vehicle", "", False), #2
    #     Symbol("North", "Turning Right", "North", "Turning Right", "Parked Vehicle", "", False), #3
    #     Symbol("North", "Turning Left", "North", "Turning Left", "Parked Vehicle", "", False), #4
    #     Symbol("West", "Turning Right", "West", "Turning Right", "Parked Vehicle", "", False) #5
    #     # Symbol("West", "Turning Left", "West", "Turning Left", "Parked Vehicle", "", False), #6
    #     # Symbol("East", "Turning Right", "East", "Turning Right", "Parked Vehicle", "", False), #7
    #     # Symbol("East", "Turning Left", "East", "Turning Left", "Parked Vehicle", "", False), #8
    #     # Symbol("South", "Turning Right", "South", "Turning Right", "Parked Vehicle", "", False), #9
    #     # Symbol("South", "Turning Left", "South", "Turning Left", "Parked Vehicle", "", False), #10
    #     # Symbol("North", "Turning Right", "North", "Turning Right", "Parked Vehicle", "", False), #11
    #     # Symbol("North", "Turning Left", "North", "Turning Left", "Parked Vehicle", "", False), #12
    #     # Symbol("West", "Turning Right", "West", "Turning Right", "Parked Vehicle", "", False), #13
    #     # Symbol("West", "Turning Left", "West", "Turning Left", "Parked Vehicle", "", False), #14
    #     # Symbol("East", "Turning Right", "East", "Turning Right", "Parked Vehicle", "", False), #15
    #     # Symbol("East", "Turning Left", "East", "Turning Left", "Parked Vehicle", "", False), #16
    #     # Symbol("South", "Turning Right", "South", "Turning Right", "Parked Vehicle", "", False), #17
    #     # Symbol("South", "Turning Left", "South", "Turning Left", "Parked Vehicle", "", False), #18
    #     # Symbol("North", "Turning Right", "North", "Turning Right", "Parked Vehicle", "", False), #19
    #     # Symbol("North", "Turning Left", "North", "Turning Left", "Parked Vehicle", "", False), #20
    #     # Symbol("West", "Turning Right", "West", "Turning Right", "Parked Vehicle", "", False), #21
    #     # Symbol("West", "Turning Left", "West", "Turning Left", "Parked Vehicle", "", False), #22
    #     # Symbol("East", "Turning Right", "East", "Turning Right", "Parked Vehicle", "", False), #23
    #     # Symbol("East", "Turning Left", "East", "Turning Left", "Parked Vehicle", "", False), #24
    #     # Symbol("South", "Turning Right", "South", "Turning Right", "Parked Vehicle", "", False), #25
    #     # Symbol("South", "Turning Left", "South", "Turning Left", "Parked Vehicle", "", False), #26
    #     # Symbol("North", "Turning Right", "North", "Turning Right", "Parked Vehicle", "", False), #27
    #     # Symbol("North", "Turning Left", "North", "Turning Left", "Parked Vehicle", "", False), #28
    #     # Symbol("West", "Turning Right", "West", "Turning Right", "Parked Vehicle", "", False), #29
    #     # Symbol("West", "Turning Left", "West", "Turning Left", "Parked Vehicle", "", False), #30
    #     # Symbol("East", "Turning Right", "East", "Turning Right", "Parked Vehicle", "", False), #31
    #     # Symbol("East", "Turning Left", "East", "Turning Left", "Parked Vehicle", "", False), #32
    #     # Symbol("East", "Turning Left", "East", "Turning Left", "Parked Vehicle", "", False) #33
    # ))

    file_list = []
    # Creating and saving all symbols into computer
    symbolCount = 1
    for symbol in symbol_list:
        symbol.plot()
        png_string = 'symbol' + str(symbolCount) + '.png'
        plt.savefig(png_string, bbox_inches='tight',transparent=True)
        file_list.append(png_string)
        symbolCount = symbolCount + 1
    def _init_ (self):
        self.file_list = file_list
    print (file_list)


    # DELETE FILES BUTTTON
    # for i in range(1, symbolCount + 1):
    #     string_delete = 'symbol' + str(symbolCount) + '.png'
    #     file_path = "/Users/rishimachanpalli/personal-vip/" + string_delete
    #     if os.path.isfile(file_path):
    #         os.remove(file_path)
    #         print("File has been deleted")
    #     else:
    #         print("File does not exist")
    #     symbolCount = symbolCount - 1


## Future data cleaning: 4 OR 3 vehicles, "Backing", "Stopped", "Entering and Leaving", ect
