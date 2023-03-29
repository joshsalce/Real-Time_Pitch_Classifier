# UCSD Baseball 2023 Pitch Classifier

## Description
This is a locally run web-application that can classify pitches in real-time based on which pitcher is in a game. Using the socket.io package in JavaScript, a pitcher can be selected from a dropdown-menu. After pressing "Start," an sklearn model is built on the pitcher's Yakkertech pitch data, and a  Python connection to the Yakkertech cameras is established using the socketIO-client pacakge that is continuously parsed to read and predict on incoming pitch data. Each prediction is written from a Python localhost client to the front-end HTML page in the style that an MLB stadium shows pitch data. "Pausing" the application will termiante the socket.io server, with the Python client still running. A working demo of this applciation can be found [here.](https://youtu.be/TTDHuMp5X2I) 

### Motivation
The spark for this project came during my first days interning with the UCSD Baseball Team. While tagging scrimmages initally, I found myself making some errors based on unfamiliarity with each pitcher's unique pitch characteristics (i.e. differences in spin rates for fastballs and sinkers, vertical and horizontal break for LHP curveballs and sliders). At the same time, I had been introduced to the Python package sklearn in my academic work. My inital project with sklearn came with building a pitch classifier using MLB pitch data, which can be found [here.](https://github.com/joshsalce/Pitch-Classifier-MLB-2022). This project aims to increase my familiarity with sklearn and build a tool that can correct for inital tagging errors.


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
3. Load in application via url 'http://127.0.0.1:3000/'
4. Select a pitcher via the dropdown menu, and press 'Start' button
5. To pause classification, click the 'Pause' button. The HTML page will stop writing incoming pitch data.
6. To change to a new pitcher, reload the application and restart the Python client file from the terminal. To kill the Python client, press control+c and re-enter the client command in Step 2

## Credits

Grateful for UCSD President of Baseball Operations Ryan Bobb for granting me access to UCSD pitch data and Yakkertech interface, as well as [Jacob Clark](https://www.linkedin.com/search/results/all/?fetchDeterministicClustersOnly=true&heroEntityKey=urn%3Ali%3Afsd_profile%3AACoAAAOAQXIBsfZfspEOxOsOVB40fxyALB_P_2s&keywords=jacob%20clark&origin=RICH_QUERY_TYPEAHEAD_HISTORY&position=0&searchId=c0553ee4-25b4-4f06-8872-55d0402fce5e&sid=4HI) of Yakkertech for staying in correspondence with me throughout the duration of this project. None of this would have happened without their help.
