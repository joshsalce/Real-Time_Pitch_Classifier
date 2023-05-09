from requests.exceptions import ConnectionError
from socketIO_client import SocketIO, LoggingNamespace
import logging

import time
from model import build_classifier
from socket_helper import check_storage, clean_socket_data, log_event
from dotenv import load_dotenv
import os

load_dotenv()

# Logs everything with socket connection, receiving and emitting messages (commented out for clarity)

#logging.getLogger('socketIO-client').setLevel(logging.DEBUG) 
logging.basicConfig()

'''
The Magic

Description: Continuously listen to the Pitch Event Channel on Yakkertech cameras,
apply classification model to identify pitches based on current pitcher, past data, and repetoire,
writes predicted pitches to front-end interface
--------------------------------------------------------------------------------
Inputs:
    name: Name of pitcher, selected from dropdown passed from socketio server to client
    local_socket: socketio client initalized in Python, used to showcase front-end data
'''
def main(name, local_socket):
    try:
        '''
        Goal: Listen to real-time pitch data channel derived from Yakkertech cameras,
        filter all incoming data to predict on and write to front-end of application
        for each pitch. 

        Inputs: 
            *args: Pitch data from Yakkertech cameras
        '''
        def receiver(*args):
            # Cleans all incoming socket data instances for variables of interest (see socket helper functions)
            socket_data = clean_socket_data(args)

            '''
            Filtering Scheme, Checkpoint 1
            --------------------------------------------------------------------------------
                - Checks output from helper function, moves on to next data stream if None
            '''
            if type(socket_data) == type(None):
                pass
            else:
                '''
                Filtering Scheme, Checkpoint 2 
                --------------------------------------------------------------------------------
                    - For all outputs not None, the first output associated with a single pitch will be
                    passed through, with all others being ignored.

                    - Note: This is used because a single pitch picked up by Yakkertech will go through several sets
                    of calculations to add more data to each pitch. 
                    
                    However, a single pitch will carry the same event id, with some exceptions.
                    
                    (I hypothesize that balls in play have two different event ids, one for the pitch data ONLY, 
                    and another for the same pitch data PLUS the hit data)
                    
                    For most pitches, more than one instance of data will carry all variables of interest. Therefore,
                    the goal of this checkpoint is to filter out only the first instance of these instances
                    and ignore the rest.
                '''

                # Returns the event ID of the pitch, and checks a separate text file
                # to see if it is already logged. If so, helper function returns None 
                # and filtering scheme data ignore data

                eventID = args[0]['event_uuid']
                data_arr = check_storage(socket_data, eventID)

                if type(data_arr) == type(None):
                    pass
                else: 
                    # Note: Only applies to the first instance of data for a particular pitch carrying all variables of interests
                    
                    # Pitch Velocity and Spin Rate returned to show on front-end
                    velo = str(round(data_arr[0][0], 1)) # rounded to 1 decimal point
                    spin_rate = str(int(round(data_arr[0][1],1))) # rounded to 0 decimal points
                

                    # First: Predict value for scaled data using classifier
                    prediction = dt_classifier.predict(data_arr)

                    # Next: Decode the value of prediction based off encoding
                    classified_pitch = label_encoder.inverse_transform(prediction)[0]

                    # Concatenates all input into a message that is written to front-end with Python client
                    pitch_text = classified_pitch + ' ' + velo + " MPH " + spin_rate + " RPM"

                    print(pitch_text)
                    
                    # Imitates Stadium Screens: Show for a brief amount of time, then go blank before the next pitch
                    local_socket.emit('message', pitch_text)
                    time.sleep(10)
                    local_socket.emit('message','')

                    return pitch_text
        
        '''
        Note: No arguments can be passed to socket function, must be initalized
        as global variables
        '''
        global dt_classifier, label_encoder
        # Builds model, LabelEncoder() and StandardScaler() objects returned as well tp use for prediction
        dt_classifier, label_encoder = build_classifier(name)

        # Sensitive Info
        url = os.getenv('URL') 
        auth_headers= { 
            'Authorization': os.getenv('AUTH') 
            }

        # Initalizes socket connection to Yakkertech cameras
        socket = SocketIO(url, headers = auth_headers, wait_for_connection=False)

        # Performs classification for real-time data, socket connection must be terminated manually in localhost
        socket.on("Pitch Event Channel", receiver)
        socket.wait()
        
    except ConnectionError:
        print('The server is down. Try again later.')
