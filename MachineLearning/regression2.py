import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt 
import itertools
import statsmodels
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose 
from statsmodels.tools.eval_measures import rmse
from statsmodels.tsa.stattools import adfuller
from pandas.plotting import autocorrelation_plot
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.arima_model import ARMAResults 
from statsmodels.tsa.stattools import acf
from datetime import timedelta

def regression2():
    cases_malaysia = pd.read_csv("Dataset/cases_malaysia.csv")
    cases_malaysia['date'] = pd.to_datetime(cases_malaysia['date'])
    cases_malaysia.fillna(value = 0, inplace = True)
    filter = ['cluster_import','cluster_religious','cluster_community','cluster_highRisk','cluster_education','cluster_detentionCentre','cluster_workplace']
    cases_malaysia[filter] = cases_malaysia[filter].astype(int)
    df_cases = cases_malaysia[['date','cases_new']]
    df_cases['date'] = pd.to_datetime(df_cases['date'])
    df_cases = df_cases.set_index('date')
