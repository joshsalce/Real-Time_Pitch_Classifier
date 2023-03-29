'''
Description: Cleans all incoming socket data based on variables of interest
--------------------------------------------------------------------------------
Inputs:
    socket_arg: *args from listening on socket channel

Returns: None if some variables of interest have no data, else list of pitch data
         where all variables have data within the socket argument
'''
def clean_socket_data(socket_arg):
    data = socket_arg[0]['pitch_data'] # Type dictionary, variables of interest will be dict keys
    ''' 
    Features:
        - yt_RelSpeedMPH
        - SpinRateRPM
        - SpinAxisDegrees
        - VertBreakInches
        - HorzBreakInches
    '''
    
    # Defines list of features to look for
    feature_list  = ['yt_RelSpeedMPH', 'SpinRateRPM', 'SpinAxisDegrees', 'VertBreakInches', 'HorzBreakInches']
    features = []

    # Iterates through defined variables of interest, finds data within socket argument or else None if variable
    # is not a key in the socket data dict
    for i in feature_list:
        if i in data.keys():
            features.append(data[i]) # Adds to list that is returned if pitch data exists for variable
        else:
            features.append(None) # Adds None to list
    
    # If any of the variables had no pitch data, None gets returned
    if (len(features) == 5) and (None not in features):
        return features
    else:
        return None

'''
Description: Writes event ID corresponding to a single pitch to a separate text file
------------------------------------------------------------------------------------
Inputs:
    event: long string signifying an event ID from incoming socket channel data

    Note: A single event ID only gets written once, so any socket data for the same
          event ID is ignored

Returns: 
    event: same as input
'''
def log_event(event):
    with open("events.txt","a") as file:
        file.write(event)
        file.write("\n")
        file.close()
    return event

'''
Description: Checks events.txt file to see if event ID is present, writes
             eventID if not in text file, else does not
--------------------------------------------------------------------------------
Inputs:
    metrics: cleaned socket data
    event: event ID of corresponding socket data

Returns: 
    ret_arr: None if event ID is already in text file, else
             nested list of cleaned socket data for event ID's just written to text file
'''
def check_storage(metrics, event):
    f = open("events.txt","r")
    lines = f.readlines()
            
    ret_arr = None
    # Checks for eventID in lines of text file
    if event + '\n' in lines:
        pass
    else:
        event = log_event(event)
        ret_arr = [metrics]

    return ret_arr