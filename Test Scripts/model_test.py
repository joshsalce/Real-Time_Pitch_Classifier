def clean_data(socket_arg):
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

def test_out():
    test_arg = ({'pitch_data': 'Pitch data over multiple parameters...'},) 
    
    socket_data = clean_data(test_arg[0])
    #event = test_arg[0]['event_uuid']
    
    print(socket_data)
    return socket_data

test_out()