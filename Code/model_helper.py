import difflib
import os
import pandas as pd
import numpy as np

'''
Description: Sub-function used in clean() function to correct for misspelled
             or errors in names found in dataset

Goal: Given errors in naming during tagging (i.e. Zachary Ernisse can be Zack Ernisse),
      we want to correct these to include as much data in models as we can and make the data
      that goes into a model uniform with respect to any given pitcher
--------------------------------------------------------------------------------
Inputs:
    df: Dataset of all pitch data
    df_names: List of all unique names found under "Pitcher" column (includes errors)
    pitcher_names:  List of all names of pitchers (does not include errors)

Returns: Dataframe with incorrect names corrected for
'''
def pair_pitcher_names(df, df_names, pitcher_names):
    # Loops through all pitcher names, check for matches in the current table's field names
    df_names = [x for x in df_names if str(x) != 'nan']
    
    for i in df_names:
        if i not in pitcher_names:
            closest_match = difflib.get_close_matches(i, pitcher_names) # List of values

            # Finds the closest match to the pitcher name NOT in the list, replaces value in dataset
            if len(closest_match) == 0:
                pass
            else:
                df.replace(i, closest_match[0])
            
    return df

'''
Description: Cleans mass dataset using pandas package and one sub-function
--------------------------------------------------------------------------------
Inputs:
    concatted_csv: Mass dataset of csvs concatenated together
    pitcher_names: List of pitcher names (w/o errors)

Returns: Dataframe, cleaned with only variables of interest and no NA values
    Note: This dataframe will be used to create and fit our classifier on.

Note: Our variables of interest for a classification model are:
    - Velocity (yt_RelSpeed)
    - Spin Rate (SpinRate)
    - Spin Axis (SpinAxis)
    - Induced Vertical Break (InducedVertBreak)
    - Horizontal Break (HorzBreak)

'''
def clean(concatted_csv, pitcher_names):
    # Returns all unique values in "Pitcher" of mass dataset, inputs to sub-function
    input_names = concatted_csv['Pitcher'].unique()
    df = pair_pitcher_names(concatted_csv, input_names, pitcher_names)

    # After correcting for errors, include only instances with valid name in "Pitcher" column
    df = df[df['Pitcher'].isin(pitcher_names)]

    # Drops NA values, returns only values of interest, drops any row with NA to include no NA values in dataset
    df = df.dropna(subset=['Pitcher','TaggedPitchType','SpinRate'])
    pitch_df = df[['Pitcher', 'TaggedPitchType', 'yt_RelSpeed', 'SpinRate', 'SpinAxis', 'InducedVertBreak', 'HorzBreak']]
    pitch_df = pitch_df.dropna(axis=0, how='any')

    return pitch_df

'''
Description: Combines all separate csv files together to form a mass DataFrame
--------------------------------------------------------------------------------
Inputs:
    dir: local directory storing all csv files
    pitcher_names: names of all pitchers as appear in Yakkertech data

Returns: Dataframe
'''
def combine_data(dir, pitcher_names):
    csv_li = []

    # Loops through directory, adds all csv files to list 
    for file in os.listdir(dir):
        if file.endswith(".csv"):
            csv = pd.read_csv(dir + file)
            csv_li.append(csv) 
  
    # Concatenates all csvs in list to one big DataFrame
    big_csv = pd.concat(csv_li)

    # Cleans dataset using pitcher name correction sub-function
    cleaned_df = clean(big_csv, pitcher_names)

    return cleaned_df


'''
Note: This sub-function isused to correct for any typos.
'''
def fix_typos(df):
    ret_df = df.replace("Slider ","Slider")
    ret_df = ret_df.replace("Sldier","Slider")

    ret_df = ret_df.replace("Fastball ", "Fastball")
    return ret_df
