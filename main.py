import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt 
from DatasetAnalysis import cases_state 
from DatasetAnalysis import tests_state
from DatasetAnalysis import death_state
from DatasetAnalysis import population
from DatasetAnalysis import pkrc
from DatasetAnalysis import hospital
from DatasetAnalysis import icu
from DatasetAnalysis import vaccination
from Findings import finding1, finding2, finding6, finding7
from FeatureSelection import boruta, rfe
from MachineLearning import classification1, classification2, classification3, arm

selectType = st.sidebar.radio('Select a Question to View', ('Datasets','Critical Findings','Feature Selection','Machine Learning Approaches'))
st.sidebar.markdown('# ')
st.sidebar.markdown('# ')
st.sidebar.markdown('# ')
st.sidebar.markdown('** TDS 3301 Data Mining **')
st.sidebar.markdown('** Group Assignment **')
st.sidebar.markdown('Prepared by: ')
st.sidebar.markdown('Yap Mou En - 1191301106')
st.sidebar.markdown('Lim Ying Shen - 1191301089')
st.sidebar.markdown('Aw Yew Lim - 1171103827')

if selectType == 'Datasets':
    
    selectDatasets = st.selectbox("Select Datasets", ['Cases','Tests','Deaths','Population','PKRC','Hospital','ICU','Vaccination'])
   
    if selectDatasets == 'Cases':
        cases_state.cases_state()
    elif selectDatasets == 'Tests':
        tests_state.tests_state()
    elif selectDatasets == 'Deaths':
        death_state.death_state()
    elif selectDatasets == 'Population':
        population.population()
    elif selectDatasets == 'PKRC':
        pkrc.pkrc()
    elif selectDatasets == 'Hospital':
        hospital.hospital()
    elif selectDatasets == 'ICU':
        icu.icu()
    else:
        vaccination.vax()

elif selectType == 'Critical Findings':

    selectFindings = st.selectbox("Select Findings", ['Finding 1','Finding 2','Finding 3','Finding 4','Finding 5','Finding 6', 'Finding 7', 'Finding 8'])
    if selectFindings == 'Finding 1':
        st.markdown('## Which age group contributes the highest number of COVID-19 cases?')
        finding1.finding1()
    elif selectFindings == 'Finding 2':
        st.markdown('## Which vaccine is the most widely used in Malaysia?')
        finding2.finding2()
    elif selectFindings == 'Finding 3':
        st.markdown('## Is there any correlation between vaccination and daily cases for Selangor, Sabah, Sarawak, and many more?')
    elif selectFindings == 'Finding 4':
        st.markdown('## Has vaccination helped reduce the daily cases? What states have shown the effect of vaccination? ')
    elif selectFindings == 'Finding 5':
        st.markdown('## Does the child vaccination rate have any effects on the daily cases of Malaysia?')
    elif selectFindings == 'Finding 6':
        st.markdown('## Which states have the highest vaccination rate?')
        finding6.finding6()
    elif selectFindings == 'Finding 7':
        st.markdown('## What state(s) require attention now?')
        finding7.finding7()
    else:
        st.markdown('## Does the National Recovery Plan have any effects on the daily cases for Selangor, Kuala Lumpur, Melaka?')
  
elif selectType == 'Feature Selection':
    selectFeature = st.selectbox("Feature Selection", ['Boruta','Lasso','Recursive feature elimination (RFE)'])

    if selectFeature == 'Boruta':
        boruta.boruta()
    elif selectFeature == 'Lasso':
        st.markdown('##')
    elif selectFeature == 'Recursive feature elimination (RFE)':
        rfe.rfe()
    else:
        st.markdown('##')
else:
    st.markdown('## Machine Learning Techniques')
    selectML = st.selectbox("Select Machine Learning Techniques", ['Regression 1', 'Regression 2', 'Classification 1', 'Classification 2', 'Classification 3', 'Association Rule Mining', 'Clustering'])

    if selectML == 'Regression 1':
        st.markdown('## Does the current vaccination rate allow herd immunity to be achieved by 30 November 2021? Assumed that herd immunity can be achieved with 80% of population has been vaccinated')
    elif selectML == 'Regression 2':
        st.markdown('## When will the total number of COVID-19 cases drop below 1000 cases per day?')
    elif selectML == 'Classification 1':
        st.markdown('##')
        classification1.classification1()
    elif selectML == 'Classification 2':
        st.markdown('##')
        classification2.classification2()
    elif selectML == 'Classification 3':
        st.markdown('##')
        classification3.classification3()
    elif selectML == 'Association Rule Mining':
        st.markdown('##')
        arm.arm()
    else:
        st.markdown('##')