# UCSD Baseball 2023 Pitch Classifier

## Description
This is a locally run web-application that can classify pitches in real-time based on which pitcher is in a game. Using the socket.io package in JavaScript, a pitcher can be selected from a dropdown-menu. After pressing "Start," an sklearn model is built on the pitcher's Yakkertech pitch data, and a  Python connection to the Yakkertech cameras is established using the socketIO-client pacakge that is continuously parsed to read and predict on incoming pitch data. Each prediction is written from a Python localhost client to the front-end HTML page in the style that an MLB stadium shows pitch data.

### Motivation


### Packages and Tech Used


## Table of Contents

| Component | Description |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| [File Schematic](https://github.com/joshsalce/Real-Time_Pitch_Classifier/blob/main/File_Schematic.pdf)| Layout of file organization and relationships | 
| [Code](https://github.com/joshsalce/Real-Time_Pitch_Classifier/tree/main/Code) | Code section including all coding files except for datasets, node, venv, and Python server files |
| [Miscellaneous](https://github.com/joshsalce/Real-Time_Pitch_Classifier/tree/main/Misc.) | Miscellaneous section including diagrams documenting thought process of project, proof of concepts, and test scripts|


## Directions


## Credits



While working with the UCSD Baseball Team for the 2023 season, I initally found 
A pet project pitch classifier built during my time working for the UCSD baseball team
