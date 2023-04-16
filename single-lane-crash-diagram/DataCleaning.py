#!/usr/bin/env python
# coding: utf-8

# Data Filter and Cleaning
# 
# This portion of code will take a CSV file of crash data, filter and clean data for range of coordinates surrounding intersection.
# Data will be prepared to be passed into relevant portions of following code.
# 
# Inputs - CSV file name, geographical coordinate of center point of intersection
# 
# (LATER WILL TAKE IN COORDS OF BOUNDING SQUARE THAT USER CLICKS INSTEAD OF CENTER POINT)
# 
# Tester CSV file name: CollisionsDataset5000ft.csv
# 
# This file contains data for 49,229 crashes in an area with radius 5000ft in downtown Atlanta

# In[25]:


#Importing Modules
import pandas as pd
import numpy as np
import re
from pprint import pprint


# In[88]:


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
    print(formatted_df)
    return formatted_df
    #return pd.concat([for_symbology, formatted_df], axis = 1)


# In[89]:
file = "CollisionsDataset5000ft.csv"
center = (33.75713, -84.38610)
#Intersection of Peachtree Center Ave NE & John Wesley Dobbs Ave NE

data_cleaner(file, center)



