import streamlit as st 
import pandas as pd
import numpy as np
import altair as alt
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import Lasso
import plotly.graph_objects as go

def lasso():

    final_merged_malaysia = pd.read_csv('Dataset/final_merged_malaysia.csv')
    X = final_merged_malaysia.drop(columns=['cases_new','cases_import','date']).copy()
    y = final_merged_malaysia['cases_new'].copy()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
    pipeline = Pipeline([('scaler',StandardScaler()),('model',Lasso())])
    search = GridSearchCV(pipeline,{'model__alpha':np.arange(1,10,1)}, cv = 5, scoring="neg_mean_squared_error",verbose=3)
    search.fit(X_train,y_train)

    coef = search.best_estimator_.named_steps['model'].coef_

    featureCoef = pd.DataFrame(columns = ['Columns', 'Value'])
    featureCoef['Columns'] = X.columns
    featureCoef['Value'] = coef

    st.markdown('### Using LASSO')
    table = go.Figure(data=go.Table(
        header=dict(values=list(featureCoef.columns),
                    fill_color='lightcyan',height=30), 
        cells=dict(values=[featureCoef.Columns, featureCoef.Value],
                    fill_color='lavender',height=30)))

    table = table.update_layout(width=600, height=1500)
    st.write(table)

    st.markdown('The strong features found using LASSO are cases_cluster, cases_pvax, cases_child, cases_adolescent, cases_adult, cases_elderly, pkrc_admitted_pui, pkrc_noncovid, beds_y, beds_covid, beds_noncrit, hosp_admitted_pui, hosp_discharged_covid, beds_icu, icu_pui, vent_port_used, daily_booster, pfizer2')
    st.markdown('There are 18 strong features in final_merged dataframe')
   
