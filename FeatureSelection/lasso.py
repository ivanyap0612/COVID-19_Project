import streamlit as st 
import pandas as pd
import numpy as np
import altair as alt
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import Lasso
import plotly.graph_objects as go

def lasso_kedah():

    final_merged_malaysia = pd.read_csv('Dataset/final_merged_malaysia.csv')
    X = final_merged_malaysia.drop(columns=['cases_new','cases_import','date']).copy()
    y = final_merged_malaysia['cases_new'].copy()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    pipeline = Pipeline([('scaler',StandardScaler()),('model',Lasso())])
    search = GridSearchCV(pipeline,{'model__alpha':np.arange(1,10,1)}, cv = 5, scoring="neg_mean_squared_error",verbose=3)
    search.fit(X_train,y_train)



   
