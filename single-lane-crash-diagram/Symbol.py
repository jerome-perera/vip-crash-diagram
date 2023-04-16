#Importing Modules
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt
import math
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.cm as cm
import os

# sublist == ['West', 'Straight', 'West', 'Straight', True, False]

# Grouping Approach
class Symbol:
    def __init__(self, v1direction, v1manuever, v2direction, v2manuever, side_swipe, stationary_present):
        self.v1manuever = v1manuever
        self.v2manuever = v2manuever
        self.v1direction = v1direction
        self.v2direction = v2direction
        self.v1 = (v1direction, v1manuever)
        self.v2 = (v2direction, v2manuever)
        self.side_swipe = side_swipe
        self.stationary_present = stationary_present
        
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
        if (self.stationary_present == "Pedestrian"):
            # Draw the head
            ax.add_artist(plt.Circle((0.2, 0.3), 0.05, color='black'))

            # Draw the body
            ax.plot([0.2, 0.2], [0.2, 0.05], linewidth=6, color='black')

            # Draw the legs
            ax.plot([0.2, 0.12], [0.05, -0.03], linewidth=6, color='black')
            ax.plot([0.2, 0.28], [0.05, -0.03], linewidth=6, color='black')

            # Draw the arms
            ax.plot([0.2, 0.12], [0.2, 0.24], linewidth=6, color='black')
            ax.plot([0.2, 0.28], [0.2, 0.24], linewidth=6, color='black')

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
            rect = plt.Rectangle((0.1, 0.1), 0.2, 0.2, color="lightblue")
            ax.add_patch(rect)

        # PLOTTING VEHICLE ARROWS
        def v_arrow(v, arrow_color):
            straight = "Straight"
            right = "Turning Right"
            left = "Turning Left"
            stopped = "Stopped"

            #Random arrow in case empty string.
            if (self.v1manuever == "" and self.v2manuever == ""):
                plt.arrow(0.2, -.2, 0, 0.25, width = 0.05, color = arrow_color)
                
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
                
                # Stopped Vector (aka Through Turn Vector)
                if (v == ("North", stopped)):
                    plt.arrow(0.2, 0.1, 0, 0.001, width = 0.05, color = arrow_color)
                if (v == ("South", stopped)):
                    plt.arrow(0.2, 0.3, 0, -0.001, width = 0.05, color = arrow_color)
                if (v == ("West", stopped)):
                    plt.arrow(0.3, 0.2, -0.001, 0, width = 0.05, color = arrow_color)
                if (v == ("East", stopped)):
                    plt.arrow(0.1, 0.2, 0.001, 0, width = 0.05, color = arrow_color)

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
        if (self.v1manuever == "" and self.v2manuever == ""):
            v_arrow(self.v1, 'grey')
        else:            
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
        within_intersection = crash_data[(crash_data.loc[:,'Longitude'].astype(float) <= long_max) &                                      (crash_data.loc[:,'Longitude'].astype(float) >= long_min) &                                      (crash_data.loc[:,'Latitude (Crash Level)'].astype(float) <= lat_max) &                                      (crash_data.loc[:,'Latitude (Crash Level)'].astype(float) >= lat_min)]
        
        
        #A Pandas dataframe with maneuvers, directions, and vehicle types for each collision in specified intersection
        #Creating a new dataframe will keep the original intact if other data needs to be extracted at a later time
    #     for_symbology = within_intersection[['Direction of Movement', 'Vehicle Maneuver (Crash Level) ',\
    #                                          'First Harmful Event','Sideswipe-Same Direction','Manner of Collision: Sideswipe-Opposite Direction',\
    #                                         'Manner of Collision: Angle (Other)', 'Manner of Collision: Head On', 'Manner of Collision: Left Angle Crash',\
    #                                         'Manner of Collision: Not a Collision with Motor Vehicle', 'Manner of Collision: Rear End',\
    #                                         'Manner of Collision: Right Angle Crash', 'Bicycle Related', 'Bicycle Related -new',\
    #                                         'Pedestrian Related (Crash Level) ', 'Pedestrian Related (Person Level)',\
    #                                         '# of Pedestrians per crash ']].copy()
        
        for_symbology = within_intersection[['Direction of Movement', 'Vehicle Maneuver (Crash Level) ', 'First Harmful Event']].copy()
        

        
        #Renaming columns of dataframe for convenience
        for_symbology.rename(columns = {'Vehicle Maneuver (Crash Level) ' : 'Maneuver', 'Direction of Movement' : 'Direction', 'First Harmful Event' : 'Vehicle Type' }, inplace = True)
        
        #Simplifying/cleaning vehicle types to pass on to other code
        
        ############
        #DELETE DELETE DELETE#
        ############
        #Dropping rows that are missing data, as that crash cannot be plotted
        #We have already masked the original dataframe to only include Manuever, Direction, and Vehicle Type columns.
        #If any of these pieces of data is missing, it is impossible to plot.
        #In the future, the code will use natural language processing (looking for keywords) in the crash narrative, to fill these empty values.
        for_symbology.dropna(inplace = True, axis = 0)
        ############

        
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
            for eachmaneuver in eachrow[1]:
                accepted = False
                if eachmaneuver == "Straight" or eachmaneuver == "Turning Right" or eachmaneuver == "Turning Left" or eachmaneuver == "Stopped" or eachmaneuver == "Changing Lanes":
                    accepted = True
                else:
                    accepted = False
                    break
            maneuv_accepted.append(accepted)
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
        #2. We can only handle the following manuevers: "Straight", "Turning Right", "Turning Left", "Stopped"
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
            #v1dir, v1manuev, v2dir, v2manuev, side_swipe, stationary_present
            
            #If pedestrian not present:
            if "Pedestrian" not in item[3]:
                #If "Changing Lanes" appears as a Maneuver, Sideswipe = True
                if "Changing Lanes" not in item [2]:
                    sub_list = [item[1][0],item[2][0],item[1][1],item[2][1], False, False]
                    #sub_list = [v1dir, v1manuev, v1dir, v1manuev, sideswipe=False, stationary_present=False]
                elif "Changing Lanes" in item [2]:#If changing lanes is present, crash must be a sideswipe
                    change_lane_index = item[2].index("Changing Lanes")
                    if change_lane_index == 1:
                        maneuv_index = 0
                    else:
                        maneuv_index = 1
                    sub_list = [item[1][0],item[2][maneuv_index],item[1][1],item[2][maneuv_index], True, False]
                    #sub_list = [v1dir, v1manuev, v1dir, v1manuev, sideswipe=True, stationary_present=False]
                
            
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
                sub_list = [item[1][veh_dir_index],item[2][0],item[1][none_index], "None", False, "Pedestrian"]
                #sub_list = [v1dir, v1manuev, peddir, pedmanuver=None, sideswipe=False, stationary_present="Pedestrian"]
            final_list.append(sub_list)
        
        formatted_df = pd.DataFrame(final_list, columns = ["V1 Dir", "V1 Manuev", "V2 Dir", "V2 Maneuv", "Sideswipe", "Stationary Present"])
        for_symbology.to_csv("cleaned_crash_data.csv", index = True)
        formatted_df.to_csv("formatted_data.csv", index = True) #formatted df shows contents of final_list
        
        #return for_symbology
        #pprint(final_list) #final_list is what will be passed onto other parts of code for plotting
        #return for_symbology
        return final_list
        #return pd.concat([for_symbology, formatted_df], axis = 1)







    #INPUT BUTTON
    symbol_list = []
    symbol01 = Symbol("", "", "", "", False, False)
    symbol02 = Symbol("", "", "", "", False, False)
    symbol03 = Symbol("", "", "", "", False, False)
    symbol04 = Symbol("", "", "", "", False, False)
    symbol05 = Symbol("", "", "", "", False, False)
    symbol06 = Symbol("", "", "", "", False, False)
    symbol07 = Symbol("", "", "", "", False, False)
    symbol08 = Symbol("", "", "", "", False, False)
    symbol09 = Symbol("", "", "", "", False, False)
    symbol10 = Symbol("", "", "", "", False, False)
    symbol11 = Symbol("", "", "", "", False, False)
    symbol12 = Symbol("", "", "", "", False, False)
    symbol13 = Symbol("", "", "", "", False, False)
    symbol14 = Symbol("", "", "", "", False, False)
    symbol15 = Symbol("", "", "", "", False, False)
    symbol16 = Symbol("", "", "", "", False, False)
    symbol17 = Symbol("", "", "", "", False, False)
    symbol18 = Symbol("", "", "", "", False, False)
    symbol19 = Symbol("", "", "", "", False, False)
    symbol20 = Symbol("", "", "", "", False, False)
    symbol21 = Symbol("", "", "", "", False, False)
    symbol22 = Symbol("", "", "", "", False, False)
    symbol23 = Symbol("", "", "", "", False, False)
    symbol24 = Symbol("", "", "", "", False, False)
    symbol25 = Symbol("", "", "", "", False, False)
    symbol26 = Symbol("", "", "", "", False, False)
    symbol27 = Symbol("", "", "", "", False, False)
    symbol28 = Symbol("", "", "", "", False, False)
    symbol29 = Symbol("", "", "", "", False, False)
    symbol30 = Symbol("", "", "", "", False, False)
    symbol31 = Symbol("", "", "", "", False, False)
    symbol32 = Symbol("", "", "", "", False, False)
    symbol33 = Symbol("", "", "", "", False, False)
    symbol_list.extend((
        symbol01, symbol02, symbol03, symbol04, symbol05, symbol06, symbol07,symbol08, symbol09, symbol10,
        symbol11, symbol12, symbol13, symbol14, symbol15, symbol16, symbol17,symbol18, symbol19, symbol20,
        symbol21, symbol22, symbol23, symbol24, symbol25, symbol26, symbol27,symbol28, symbol29, symbol30,
        symbol31, symbol32, symbol33
    ))

    file = "CollisionsDataset5000ft.csv"
    center = (33.75713, -84.38610)
    data_counter = np.zeros(33)
    data_counter = data_counter.astype(int)
    max_counter = np.zeros(33)
    max_counter = data_counter.astype(int)
    total_crashes = 0

    for sublist in data_cleaner(file, center):
        max_count = 0
        total_crashes = total_crashes + 1
        for sublist2 in data_cleaner(file, center):
            if (sublist == sublist2):
                max_count = max_count + 1
        if (sublist == ['South', 'Stopped', 'North', 'Turning Left', False, False] or
            sublist == ['South', 'Stopped', 'North', 'Turning Right', False, False] or
            sublist == ['South', 'Stopped', 'North', 'Straight', False, False] or
            sublist == ['South', 'Stopped', 'East', 'Turning Left', False, False] or
            sublist == ['South', 'Stopped', 'East', 'Turning Right', False, False] or
            sublist == ['South', 'Stopped', 'East', 'Straight', False, False] or
            sublist == ['South', 'Stopped', 'West', 'Turning Left', False, False] or
            sublist == ['South', 'Stopped', 'West', 'Turning Right', False, False] or
            sublist == ['South', 'Stopped', 'West', 'Straight', False, False] or
            sublist == ['South', 'Stopped', 'South', 'Straight', False, False] or

            sublist == ['South', 'Straight', 'South', 'Straight', False, False]
        ):
            if max_counter[0] < max_count:
                max_counter[0] = max_count
                symbol_list[0]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[0] = data_counter[0] + 1

        if (sublist == ['East', 'Turning Left', 'East', 'Turning Left', True, False]):
            if max_counter[1] < max_count:
                max_counter[1] = max_count
                symbol_list[1]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[1] = data_counter[1] + 1

        if (sublist == ['North', 'Straight', 'West', 'Turning Right', False, False] or
            sublist == ['West', 'Turning Right', 'East', 'Turning Left', False, False]
        ):
            if max_counter[2] < max_count:
                max_counter[2] = max_count
                symbol_list[2]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[2] = data_counter[2] + 1

        if (sublist == ['North', 'Straight', 'East', 'Turning Left', False, False] or
            
            sublist == ['North', 'Straight', 'North', 'Straight', True, False]
            ):
            if max_counter[3] < max_count:
                max_counter[3] = max_count
                symbol_list[3]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[3] = data_counter[3] + 1

        if (sublist == ['West', 'Straight', 'South', 'Turning Right', False, False] or
            sublist == ['South', 'Turning Right', 'North', 'Turning Left', False, False]
        ):
            if max_counter[4] < max_count:
                max_counter[4] = max_count
                symbol_list[4]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[4] = data_counter[4] + 1

        if (sublist == ['West', 'Straight', 'North', 'Turning Left', False, False] or
            sublist == ['West', 'Straight', 'West', 'Straight', True, False]
            ):
            if max_counter[5] < max_count:
                max_counter[5] = max_count
                symbol_list[5]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[5] = data_counter[5] + 1

        if (sublist == ['West', 'Straight', 'South', 'Straight', False, False] or
            sublist == ['South', 'Straight', 'West', 'Straight', False, False]
        ):
            if max_counter[6] < max_count:
                max_counter[6] = max_count
                symbol_list[6]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[6] = data_counter[6] + 1

        if (sublist == ['West', 'Straight', 'South', 'Turning Left', False, False]):
            if max_counter[7] < max_count:
                max_counter[7] = max_count
                symbol_list[7]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[7] = data_counter[7] + 1

        if (sublist == ['West', 'Straight', 'East', 'Turning Left', False, False]):
            if max_counter[8] < max_count:
                max_counter[8] = max_count
                symbol_list[8]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[8] = data_counter[8] + 1

        if (sublist ==  ['North', 'Straight', 'West', 'Straight', False, False] or
             sublist ==  ['West', 'Straight', 'North', 'Straight', False, False]
        ):
            if max_counter[9] < max_count:
                max_counter[9] = max_count
                symbol_list[9]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[9]  = data_counter[9] + 1     

        if (sublist == ['West', 'Stopped', 'South', 'Turning Left', False, False] or
            sublist == ['West', 'Stopped', 'South', 'Turning Right', False, False] or
            sublist == ['West', 'Stopped', 'South', 'Straight', False, False] or
            sublist == ['West', 'Stopped', 'East', 'Turning Left', False, False] or
            sublist == ['West', 'Stopped', 'East', 'Turning Right', False, False] or
            sublist == ['West', 'Stopped', 'East', 'Straight', False, False] or
            sublist == ['West', 'Stopped', 'North', 'Turning Left', False, False] or
            sublist == ['West', 'Stopped', 'North', 'Turning Right', False, False] or
            sublist == ['West', 'Stopped', 'North', 'Straight', False, False] or
            sublist == ['West', 'Stopped', 'West', 'Straight', False, False] or

            sublist == ['West', 'Straight', 'West', 'Straight', False, False]
        ):
            if max_counter[10] < max_count:
                max_counter[10] = max_count
                symbol_list[10]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[10] = data_counter[10] + 1

        if (sublist == ['East', 'Turning Left', 'South', 'Turning Left', False, False] or
            sublist == ['South', 'Turning Left', 'East', 'Turning Left', False, False]
        ):
            if max_counter[11] < max_count:
                max_counter[11] = max_count
                symbol_list[11]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[11] = data_counter[11] + 1

        if (sublist == ['South', 'Straight', 'North', 'Turning Left', False, False]):
            if max_counter[12] < max_count:
                max_counter[12] = max_count
                symbol_list[12]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[12] = data_counter[12] + 1

        if (sublist == ['West', 'Straight', 'South', 'Turning Left', False, False]):
            if max_counter[13] < max_count:
                max_counter[13] = max_count
                symbol_list[13]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[13] = data_counter[13] + 1

        if (sublist == ['East', 'Straight', 'South', 'Turning Right', False, False] or
            
            sublist == ['North', 'Turning Left', 'North', 'Turning Left', True, False]
            ):
            if max_counter[14] < max_count:
                max_counter[14] = max_count
                symbol_list[14]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[14] = data_counter[14] + 1

        if (sublist == ['North', 'Turning Left', 'East', 'Turning Left', False, False] or
            sublist == ['East', 'Turning Left', 'North', 'Turning Left', False, False]
        ):
            if max_counter[15] < max_count:
                max_counter[15] = max_count
                symbol_list[15]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[15] = data_counter[15] + 1

        if (sublist == ['South', 'Turning Left', 'West', 'Turning Left', False, False] or
            sublist == ['West', 'Turning Left', 'South', 'Turning Left', False, False]
        ):
            if max_counter[17] < max_count:
                max_counter[17] = max_count
                symbol_list[17]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[17] = data_counter[17] + 1

        if (sublist == ['East', 'Straight', 'West', 'Straight', False, False] or
            sublist == ['West', 'Straight', 'North', 'Turning Right', False, False] or

            sublist == ['South', 'Turning Left', 'South', 'Turning Left', True, False]
        ):
            if max_counter[18] < max_count:
                max_counter[18] = max_count
                symbol_list[18]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[18] = data_counter[18] + 1

        if (sublist == ['South', 'Straight', 'East', 'Turning Left', False, False]):
            if max_counter[19] < max_count:
                max_counter[19] = max_count
                symbol_list[19]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[19] = data_counter[19] + 1

        if (sublist == ['North', 'Straight', 'South', 'Turning Left', False, False]):
            if max_counter[20] < max_count:
                max_counter[20] = max_count
                symbol_list[20]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[20] = data_counter[20] + 1
        
        if (sublist == ['North', 'Turning Left', 'West', 'Turning Left', False, False] or
            sublist == ['West', 'Turning Left', 'North', 'Turning Left', False, False]
        ):
            if max_counter[21] < max_count:
                max_counter[21] = max_count
                symbol_list[21]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[21] = data_counter[21] + 1

        if (sublist == ['East', 'Stopped', 'South', 'Turning Left', False, False] or
            sublist == ['East', 'Stopped', 'South', 'Turning Right', False, False] or
            sublist == ['East', 'Stopped', 'South', 'Straight', False, False] or
            sublist == ['East', 'Stopped', 'North', 'Turning Left', False, False] or
            sublist == ['East', 'Stopped', 'North', 'Turning Right', False, False] or
            sublist == ['East', 'Stopped', 'North', 'Straight', False, False] or
            sublist == ['East', 'Stopped', 'West', 'Turning Left', False, False] or
            sublist == ['East', 'Stopped', 'West', 'Turning Right', False, False] or
            sublist == ['East', 'Stopped', 'West', 'Straight', False, False] or
            sublist == ['East', 'Stopped', 'East', 'Straight', False, False] or

            sublist == ['East', 'Straight', 'East', 'Straight', False, False]
        ):
            if max_counter[22] < max_count:
                max_counter[22] = max_count
                symbol_list[22]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[22] = data_counter[22] + 1

        if (sublist == ['East', 'Straight', 'South', 'Straight', False, False] or
            sublist == ['South', 'Straight', 'East', 'Straight', False, False]
        ):
            if max_counter[23] < max_count:
                max_counter[23] = max_count
                symbol_list[23]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[23] = data_counter[23] + 1
            
        if (sublist == ['East', 'Straight', 'West', 'Turning Left', False, False]):
            if max_counter[24] < max_count:
                max_counter[24] = max_count
                symbol_list[24]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[24] = data_counter[24] + 1

        if (sublist == ['East', 'Straight', 'North', 'Turning Left', False, False]):
            if max_counter[25] < max_count:
                max_counter[25] = max_count
                symbol_list[25]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[25] = data_counter[25] + 1
            
        if (sublist ==  ['North', 'Straight', 'East', 'Straight', False, False] or
             sublist ==  ['East', 'Straight', 'North', 'Straight', False, False]
        ):
            if max_counter[26] < max_count:
                max_counter[26] = max_count
                symbol_list[26]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[26] = data_counter[26] + 1

        if (sublist == ['East', 'Straight', 'South', 'Turning Left', False, False] or
            sublist == ['East', 'Straight', 'East', 'Straight', True, False]
            ):
            if max_counter[27] < max_count:
                max_counter[27] = max_count
                symbol_list[27]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[27] = data_counter[27] + 1
        
        if (sublist == ['North', 'Turning Right', 'South', 'Turning Left', False, False] or 
            sublist == ['East', 'Straight', 'North', 'Turning Right', False, False]
        ):
            if max_counter[28] < max_count:
                max_counter[28] = max_count
                symbol_list[28]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[28] = data_counter[28] + 1

        if (sublist == ['South', 'Straight', 'West', 'Turning Left', False, False] or
            sublist == ['South', 'Straight', 'South', 'Straight', True, False]
            ):
            if max_counter[29] < max_count:
                max_counter[29] = max_count
                symbol_list[29]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[29] = data_counter[29] + 1

        if (sublist == ['South', 'Straight', 'East', 'Turning Right', False, False] or 
            sublist == ['East', 'Turning Right', 'West', 'Turning Left', False, False]
        ):
            if max_counter[30] < max_count:
                max_counter[30] = max_count
                symbol_list[30]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[30] = data_counter[30] + 1
        
        if (sublist == ['North', 'Straight', 'East', 'Turning Right', False, False] or
            sublist == ['West', 'Turning Left', 'West', 'Turning Left', True, False]
            ):
            if max_counter[31] < max_count:
                max_counter[31] = max_count
                symbol_list[31]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[31] = data_counter[31] + 1

        if (sublist == ['North', 'Stopped', 'South', 'Turning Left', False, False] or
            sublist == ['North', 'Stopped', 'South', 'Turning Right', False, False] or
            sublist == ['North', 'Stopped', 'South', 'Straight', False, False] or
            sublist == ['North', 'Stopped', 'East', 'Turning Left', False, False] or
            sublist == ['North', 'Stopped', 'East', 'Turning Right', False, False] or
            sublist == ['North', 'Stopped', 'East', 'Straight', False, False] or
            sublist == ['North', 'Stopped', 'West', 'Turning Left', False, False] or
            sublist == ['North', 'Stopped', 'West', 'Turning Right', False, False] or
            sublist == ['North', 'Stopped', 'West', 'Straight', False, False] or
            sublist == ['North', 'Stopped', 'North', 'Straight', False, False] or

            sublist == ['North', 'Straight', 'North', 'Straight', False, False]
        ):
            if max_counter[32] < max_count:
                max_counter[32] = max_count
                symbol_list[32]  = Symbol(sublist[0],sublist[1],sublist[2],sublist[3],sublist[4],sublist[5])
            data_counter[32] = data_counter[32] + 1
    total_crashes_plotted = sum(data_counter)

    folder_path = os.path.dirname(os.path.abspath(__file__))

    # Deletes al files in this folder before creating the new symbols.
    fileNum = 1
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".png"):
            file_path = os.path.join(folder_path, file_name)
            os.remove(file_path)
            fileNum = fileNum + 1

    file_list = []
    # Creating and saving all symbols into computer
    symbolCount = 1
    for symbol in symbol_list:
        symbol.plot()
        if symbol.v1direction != "":
            png_string = 'symbol' + str(symbolCount) + '.png'
        else:
            png_string = 'unplottedsymbol' + str(symbolCount) + '.png'
        # print (png_string + " = " + symbol.v1direction + "," + symbol.v1manuever + "," + symbol.v2direction + "," + symbol.v2manuever + "," + str(symbol.side_swipe) + "," + str(symbol.stationary_present))
        plt.savefig(png_string, bbox_inches='tight', transparent=True)
        plt.close()
        file_list.append(png_string)
        symbolCount += 1

    # print (max_counter)
    # print (data_counter)
    
    # print(total_crashes_plotted)
    # print(total_crashes)

