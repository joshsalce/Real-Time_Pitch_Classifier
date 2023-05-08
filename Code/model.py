import pandas as pd
import numpy as np
import os
import difflib

from sklearn.model_selection import train_test_split, cross_val_predict, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, f1_score, recall_score, precision_score

from model_helper import clean, combine_data, fix_typos, filter_pitcher, pair_pitcher_names

'''
Description: Builds Classifier model for Pitcher selected in Front-End dropdown menu
------------------------------------------------------------------------------------
Inputs:
    pitcher_name: Name of pitcher included in socket message

Returns: 
    DecisionTreeClassifier() model fit to pitcher's dataset
    LabelEncoder() object that encodes and decodes pitches (i.e. 1 for "Fastball," 2 for "Changeup")
    StandardScaler() object fitted to transform incoming socket data and scale it 
                     appropriately to be used for prediction
'''
def build_classifier(pitcher_name):
    directory = 'UCSD_Data/'

    pitchers = ['Izaak Martinez', 'Sam Hasegawa', 'Ryan Rissas', 'Spencer Seid',
                'Zachary Ernisse','Chris Gilmartin','Joel Tornero','Cole Dale','Seth Sumner',
                'Nolan Mccracken','Joseph Soberon','Donovan Chriss','Ryan Forcucci','Anthony Eyanson',
                'Ethan Holt','Aren Alvarez','Niccolas Gregson','Michael Mitchell','Matthew Dalquist','Xavier Franco','Ryan Farmer']  
    
    # Applies helper functions to combine all tagged pitch data, 
    # filter out to include only pitch data from selected pitcher
    df = combine_data(directory, pitchers)     
    pitcher_df = filter_pitcher(df, pitcher_name)
        
    if pitcher_df.shape[0] == 0:
        raise Exception("No data for:", pitcher_name)
    else:
        print("Creating Model for:", pitcher_name, '\n')

        # Sort into predictor variables (X) and output variable (y)
        x_df = pitcher_df.drop(['TaggedPitchType'], axis=1)
        y_df = pitcher_df['TaggedPitchType']

        # Encode pitches into numerical categories
        label_encoder = LabelEncoder()
        y_df = label_encoder.fit_transform(y_df)

        # Creates cheat-sheet of  pitches and corresponding value after being encoded
        repetoire = pd.DataFrame()
        repetoire['Pitch'] = label_encoder.inverse_transform(list(set(y_df)))
        repetoire['Encoded'] = list(set(y_df))

        print(repetoire, '\n')

        # Split into training and test data
        X_train, X_test, y_train, y_test = train_test_split(x_df, y_df, test_size = 0.2, random_state=0, stratify = y_df) 

        # Scale training and test data for predictor variables
        scaler = StandardScaler()  

        X_train = scaler.fit_transform(X_train)  
        X_test = scaler.transform(X_test)

        # Initialize a model (RandomForest used for prediction accuracy)
        model = DecisionTreeClassifier()
            
        # Fit model and predict
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
            
        # Provides scores for testing and training sets
        test_score = model.score(X_test, y_test)
        train_score = model.score(X_train, y_train)

        print(f"Testing set accuracy: ", test_score, '\n')
        print(f"Training set accuracy: ", train_score, '\n')

        #print(classification_report(y_test, y_pred), '\n')

        # Cross-valdiates created model, outputs F1 scpre
        y_cv_pred = cross_val_predict(model, X_train, y_train, cv=5)
        model_f1 = f1_score(y_train, y_cv_pred, average="macro")
        print(f"F1 Score", model_f1, '\n')
            
        # Runs several iterations of cross-validated model, 
        # returns average of model's perforancescores
        scores = cross_val_score(model, x_df, y_df, cv = 3)
        model_accuracy = np.mean(scores)
        print('Model (average) accuracy: ', model_accuracy, '\n')
        print('Model Successfully Created.')

        return model, label_encoder, scaler