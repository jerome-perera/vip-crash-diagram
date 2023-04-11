# Data Filter and Cleaning

# This portion of code will take a CSV file of crash data, filter and clean data for range of coordinates surrounding intersection. Data will be prepared to be passed into relevant portions of following code.

# Inputs - CSV file name, geographical coordinate of center point of intersection

# (LATER WILL TAKE IN COORDS OF BOUNDING SQUARE THAT USER CLICKS INSTEAD OF CENTER POINT)

# Tester CSV file name: CollisionsDataset5000ft.csv

# This file contains data for 49,229 crashes in an area with radius 5000ft in downtown Atlanta



#Importing Modules
import pandas as pd
# import numpy as np
# import re
from pprint import pprint

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
    
    pprint(final_list) #final_list is what will be passed onto other parts of code for plotting
    #return for_symbology
    return final_list
    #return pd.concat([for_symbology, formatted_df], axis = 1)


file = "CollisionsDataset5000ft.csv"
center = (33.75713, -84.38610)
#Intersection of Peachtree Center Ave NE & John Wesley Dobbs Ave NE

data_cleaner(file, center)

    # symbol_list.extend((
    #     Symbol("South", "Turning Right", "South", "Turning Right", "Parked Vehicle", "", False), #1
    #     Symbol("South", "Turning Left", "South", "Turning Left", "Parked Vehicle", "", False), #2
    #     Symbol("North", "Turning Right", "North", "Turning Right", "Parked Vehicle", "", False), #3
    #     Symbol("North", "Turning Left", "North", "Turning Left", "Parked Vehicle", "", False), #4
    #     Symbol("West", "Turning Right", "West", "Turning Right", "Parked Vehicle", "", False) #5
        # Symbol("West", "Turning Left", "West", "Turning Left", "Parked Vehicle", "", False), #6
        # Symbol("East", "Turning Right", "East", "Turning Right", "Parked Vehicle", "", False), #7
        # Symbol("East", "Turning Left", "East", "Turning Left", "Parked Vehicle", "", False), #8
        # Symbol("South", "Turning Right", "South", "Turning Right", "Parked Vehicle", "", False), #9
        # Symbol("South", "Turning Left", "South", "Turning Left", "Parked Vehicle", "", False), #10
        # Symbol("North", "Turning Right", "North", "Turning Right", "Parked Vehicle", "", False), #11
        # Symbol("North", "Turning Left", "North", "Turning Left", "Parked Vehicle", "", False), #12
        # Symbol("West", "Turning Right", "West", "Turning Right", "Parked Vehicle", "", False), #13
        # Symbol("West", "Turning Left", "West", "Turning Left", "Parked Vehicle", "", False), #14
        # Symbol("East", "Turning Right", "East", "Turning Right", "Parked Vehicle", "", False), #15
        # Symbol("East", "Turning Left", "East", "Turning Left", "Parked Vehicle", "", False), #16
        # Symbol("South", "Turning Right", "South", "Turning Right", "Parked Vehicle", "", False), #17
        # Symbol("South", "Turning Left", "South", "Turning Left", "Parked Vehicle", "", False), #18
        # Symbol("North", "Turning Right", "North", "Turning Right", "Parked Vehicle", "", False), #19
        # Symbol("North", "Turning Left", "North", "Turning Left", "Parked Vehicle", "", False), #20
        # Symbol("West", "Turning Right", "West", "Turning Right", "Parked Vehicle", "", False), #21
        # Symbol("West", "Turning Left", "West", "Turning Left", "Parked Vehicle", "", False), #22
        # Symbol("East", "Turning Right", "East", "Turning Right", "Parked Vehicle", "", False), #23
        # Symbol("East", "Turning Left", "East", "Turning Left", "Parked Vehicle", "", False), #24
        # Symbol("South", "Turning Right", "South", "Turning Right", "Parked Vehicle", "", False), #25
        # Symbol("South", "Turning Left", "South", "Turning Left", "Parked Vehicle", "", False), #26
        # Symbol("North", "Turning Right", "North", "Turning Right", "Parked Vehicle", "", False), #27
        # Symbol("North", "Turning Left", "North", "Turning Left", "Parked Vehicle", "", False), #28
        # Symbol("West", "Turning Right", "West", "Turning Right", "Parked Vehicle", "", False), #29
        # Symbol("West", "Turning Left", "West", "Turning Left", "Parked Vehicle", "", False), #30
        # Symbol("East", "Turning Right", "East", "Turning Right", "Parked Vehicle", "", False), #31
        # Symbol("East", "Turning Left", "East", "Turning Left", "Parked Vehicle", "", False), #32
        # Symbol("East", "Turning Left", "East", "Turning Left", "Parked Vehicle", "", False) #33
    # ))