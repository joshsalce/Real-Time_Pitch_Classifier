arg1 = ({'pitch_data': 'Pitch data over multiple parameters...'},) 
data_dict = {}

def clean_socket_data(socket_arg):
    data = socket_arg['pitch_data']
    # event_id = socket_arg['event_uuid'] Could use this in the future

    ''' 
    Features:
        - yt_RelSpeedMPH
        - SpinRateRPM
        - SpinAxisDegrees
        - VertBreakInches
        - HorzBreakInches
    '''
    feature_list  = ['yt_RelSpeedMPH', 'SpinRateRPM', 'SpinAxisDegrees', 'VertBreakInches', 'HorzBreakInches']
    features = []

    for i in feature_list:
        if i in data.keys():
            features.append(data[i])
        else:
            features.append(None)
    #print(len(features) == 5 and None not in features)
    
    if (len(features) == 5) and (None not in features):
        #print(socket_arg['event_uuid'])
        return features
    else:
        pass

clean_socket_data(arg1)
print(data_dict)