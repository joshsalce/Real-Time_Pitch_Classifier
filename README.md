# UCSD Baseball 2023 Pitch Classifier

## Description
This is a locally run web-application that can classify pitches in real-time based on which pitcher is in a game. Using the socket.io package in JavaScript, a pitcher can be selected from a dropdown-menu. After pressing "Start," an sklearn model is built on the pitcher's Yakkertech pitch data, and a  Python connection to the Yakkertech cameras is established using the socketIO-client pacakge that is continuously parsed to read and predict on incoming pitch data. Each prediction is written from a Python localhost client to the front-end HTML page in the style that an MLB stadium shows pitch data. "Pausing" the application will termiante the socket.io server, with the Python client still running. 

### Motivation


### Packages and Tech Used
- HTML
- [socket.io (version 1.7.4)](https://socket.io/)
- NodeJS, v12.19.0 
- [socketIO-client (Python)](https://pypi.org/project/socketIO-client/)
- Python Packages: [pandas](https://pandas.pydata.org/docs/), [numpy](https://numpy.org/doc/), [difflib](https://docs.python.org/3.10/library/difflib.html), [os](https://docs.python.org/3/library/os.html), [time](https://docs.python.org/3/library/time.html), [sklearn](https://scikit-learn.org/stable/index.html)

## Table of Contents

| Component | Description |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [File Schematic](https://github.com/joshsalce/Real-Time_Pitch_Classifier/blob/main/File_Schematic.pdf)| Layout of file organization and relationships | 
| [Code](https://github.com/joshsalce/Real-Time_Pitch_Classifier/tree/main/Code) | Code section including all coding files except for datasets, node, venv, and Python server files |
| [Miscellaneous](https://github.com/joshsalce/Real-Time_Pitch_Classifier/tree/main/Misc.) | Miscellaneous section including diagrams documenting thought process of project, proof of concepts, and test scripts|


## Directions
1. Install all necessary packages via terminal commands.
2. cd to directory of classifier project, and initialize a split terminal, running the following functions separately in VSCode:
```
nodemon server.js
```
```
python3 Client/client.py
```
2. 
To change to a new pitcher, reload the application and restart the Python client file from the terminal.

## Credits



While working with the UCSD Baseball Team for the 2023 season, I initally found 
A pet project pitch classifier built during my time working for the UCSD baseball team
