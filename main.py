import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt 
from DatasetAnalysis import cases_my,cases_state,tests_my,tests_state,death_state,population,pkrc,hospital,icu,vaccination
from Findings import finding1, finding2, finding3, finding4, finding5, finding6, finding7, finding8
from FeatureSelection import boruta, rfe, lasso
from MachineLearning import regression2, classification1, classification2, classification3, arm, clustering

selectType = st.sidebar.radio('Select a Question to View', ('Datasets','Project Findings','Feature Selection','Machine Learning Approaches'))
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
    
    selectDatasets = st.selectbox("Select Datasets", ['Cases-Malaysia','Cases-States','Tests-Malaysia','Tests-State','Deaths','Population','PKRC','Hospital','ICU','Vaccination'])
   
    if selectDatasets == 'Cases-Malaysia':
        cases_my.cases_my()
    elif selectDatasets == 'Cases-States':
        cases_state.cases_state()
    elif selectDatasets == 'Tests-Malaysia':
        tests_my.tests_my()
    elif selectDatasets == 'Tests-State':
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

elif selectType == 'Project Findings':

    selectFindings = st.selectbox("Select Findings", ['Finding 1','Finding 2','Finding 3','Finding 4','Finding 5','Finding 6', 'Finding 7', 'Finding 8'])
    if selectFindings == 'Finding 1':
        st.markdown('## Which age group contributes the highest number of COVID-19 cases?')
        finding1.finding1()
    elif selectFindings == 'Finding 2':
        st.markdown('## Which vaccine is the most widely used in Malaysia?')
        finding2.finding2()
    elif selectFindings == 'Finding 3':
        st.markdown('## Is there any correlation between vaccination and daily cases for Selangor, Sabah, Sarawak, and many more?')
        finding3.finding3()
    elif selectFindings == 'Finding 4':
        st.markdown('## Has vaccination helped reduce the daily cases? What states have shown the effect of vaccination? ')
        finding4.finding4()
    elif selectFindings == 'Finding 5':
        st.markdown('## Does the child vaccination rate have any effects on the daily cases of Malaysia?')
        finding5.finding5()
    elif selectFindings == 'Finding 6':
        st.markdown('## Which states have the highest vaccination rate?')
        finding6.finding6()
    elif selectFindings == 'Finding 7':
        st.markdown('## What state(s) require attention now?')
        finding7.finding7()
    else:
        st.markdown('## Does the National Recovery Plan have any effects on the daily cases for Kedah, Perak, Selangor and Negeri Sembilan?')
        finding8.finding8()
  
elif selectType == 'Feature Selection':
    selectFeature = st.selectbox("Feature Selection", ['Boruta','Lasso','Recursive feature elimination (RFE)'])

    if selectFeature == 'Boruta':
        boruta.boruta()
    elif selectFeature == 'Lasso':
        lasso.lasso()
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
        regression2.regression2()
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
        clustering.clustering()