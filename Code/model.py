import pandas as pd
import numpy as np
import os
import difflib

from sklearn.model_selection import train_test_split, cross_val_predict, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder, MinMaxScaler
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score, classification_report, f1_score, recall_score, precision_score

from model_helper import fix_typos


class PitcherModel:    
    def __init__(self, pitcher, model = DecisionTreeClassifier()):
        self.pitcher = pitcher
        self.model = model
        self.x_df = None
        self.y_df = None
        self.lab_enc = LabelEncoder()
        self.repetoire = pd.DataFrame()
        self.test_score = None
        self.f1 = None
        self.precision = None
        self.recall = None

        #self.normalizer = StandardScaler()
        #self.minmax = MinMaxScaler()

    '''
    Description: Filters all concatted data to only include 
                recorded data for a particular pitcher
    --------------------------------------------------------------------------------
    Inputs:
    df: Mass DataFrame of all Pitch Data
    pitcher_name: Name of selected pitcher (comes from front-end passed through socket)

    Returns: DataFrame only including data for one pitcher
    '''
    def get_pitcher_data(self, df): #def filter_pitcher(df, pitcher_name):
        # Filters out only instances for a partiuclar pitcher, drop "Pitcher" column
        df_pitcher = df[df['Pitcher'] == self.pitcher]
        df_pitcher.drop(['Pitcher'], axis = 1, inplace=True)

        '''  
        Runs  separate conditions to corrects for tagging errors in tagging
            i.e. Ethan Holt is a sinker-baller, so all Fastballs should be Sinkers
        '''
        if self.pitcher in ['Donovan Chriss', 'Cole Dale', 'Zachary Ernisse', 'Chris Gilmartin', 'Izaak Martinez', 'Michael Mitchell']:
            df_pitcher = df_pitcher.replace("Curveball","Slider")
        if self.pitcher in ['Niccolas Gregson','Sam Hasegawa','Izaak Martinez']:
            df_pitcher = df_pitcher.replace("Splitter","Changeup")
        if self.pitcher == 'Anthony Eyanson':
            df_pitcher = df_pitcher.replace("Changeup","Splitter")
        if self.pitcher == 'Xavier Franco' or self.pitcher == 'Ethan Holt':
            df_pitcher = df_pitcher.replace("Fastball","Sinker")

        # Sort into predictor variables (X) and output variable (y)
        self.x_df = df_pitcher.drop(['TaggedPitchType'], axis=1)
        self.y_df = df_pitcher['TaggedPitchType']
   
    '''
    Description: Checks for labels of pticher, transforms to numerical values
    --------------------------------------------------------------------------------
    Inputs: self

    Returns: None
        Changes y-labels to transformed versions
    '''
    def encode(self):
        if len(self.y_df) == 0:
            raise Exception('No Y Data to encode. Call method to get pitch data first.')
        else:
            self.y_df = self.lab_enc.fit_transform(self.y_df)
       
    '''
    Description: Create "cheat-sheet" of pitch and corresponding numerical value
    --------------------------------------------------------------------------------
    Inputs: self

    Returns: None
        Fills pitch-label dataframe with pitches and encoded labels 
    ''' 
    def get_repetoire(self):
        self.repetoire['Pitch'] = self.lab_enc.inverse_transform(list(set(self.y_df)))
        self.repetoire['Encoded'] = list(set(self.y_df))
        print(self.repetoire, '\n')

    '''
    Description: Creates train-test sets, trains model and returns evaluation metrics
    --------------------------------------------------------------------------------
    Inputs: self

    Returns: None

    Current metrics: Accuracy, class-weighted precision, recall, and F1-Score 
    ''' 
    def train_model(self):
        # Split into training and test data, make sure to stratify based on pitch frequency
        X_train, X_valid, y_train, y_valid = train_test_split(self.x_df, self.y_df, 
            test_size = 0.2, random_state=0, stratify = self.y_df)   
        
        # Fit model, predict
        self.model.fit(X_train, y_train)
        
        # Predict, score for test set
        y_pred = self.model.predict(X_valid)
        self.test_score = accuracy_score(y_valid, y_pred)

        # Calculates weighted precision, recall metrics
        self.recall = recall_score(y_valid, y_pred, average='weighted')
        self.precision = precision_score(y_valid, y_pred, average='weighted')

        # Cross-valdiates created model, outputs F1 scpre
        y_cv_pred = cross_val_predict(self.model, X_train, y_train, cv=5)
        self.f1 = f1_score(y_train, y_cv_pred, average="weighted")

        # Print metrics in console before predicting with live socket data
        print("Metrics")
        print("-----------------")
        print("Accuracy:", self.test_score)
        print("Precision:", self.precision)
        print("Recall:", self.precision)
        print("F1 Score:", self.f1)