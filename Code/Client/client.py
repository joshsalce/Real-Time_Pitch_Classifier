from socketIO_client import SocketIO, LoggingNamespace
import logging
import sys

# Import main() function from higher directory
sys.path.append(".")
from connect import main


#logging.getLogger('socketIO-client').setLevel(logging.DEBUG)
#logging.basicConfig()

# Builds localhost socket, client must be started and ended manually from terminal
socketIO = SocketIO('127.0.0.1', 3000, LoggingNamespace)

# Connection and Disconnection Sanity Check Functions 
def on_connect():
    print('Connected.')

def on_disconnect():
    print('He Disconnected.')
    
'''
Description:  Receives socket message including selected pitcher from front-end, 
applies to main() function
'''
def writer(*args):
    # Filters out unnecessary messages emited from socket to client (i.e. initialization)
    if str(args[0]).startswith("b'"):
        pass
    else:
        print('Received:', str(args[0]))

        '''
        Calls main() function for pitcher to build model, 
        predict on incoming data, and write to front end
        '''
        main(str(args[0]), socketIO)

socketIO.on('connect', on_connect)

socketIO.on('message', writer)

socketIO.on('disconnect', on_disconnect)

socketIO.wait()
