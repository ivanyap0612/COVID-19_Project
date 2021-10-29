import datetime
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def finding3():
    cases_malaysia = pd.read_csv('Dataset/cases_malaysia.csv')
    cases_state = pd.read_csv('Dataset/cases_state.csv')
    vax_my = pd.read_csv('Dataset/vax_malaysia.csv')
    vax_state = pd.read_csv('Dataset/vax_state.csv')
    cases_state['date'] = pd.to_datetime(cases_state['date'])
    cases_malaysia['date']= pd.to_datetime(cases_malaysia['date'])

    selectAge = st.selectbox("Select an aspect", ['All','Child'])
    selectChoice = st.selectbox("Select a location to view", ['Malaysia','Johor','Kedah','Kelantan','Melaka','Negeri Sembilan','Pahang','Pulau Pinang','Perak','Perlis','Selangor','Terengganu','Sabah','Sarawak','W.P. Kuala Lumpur','W.P. Labuan','W.P. Putrajaya'])

    if selectAge == 'All':
        if selectChoice == 'Malaysia':
            q4_cases = cases_malaysia[cases_malaysia['date'] > '2021-02-23']
            q4_cases_my = q4_cases[['date','cases_new']].copy()
            q4_cases_my = q4_cases_my.reset_index(drop=True)

            q4_vax_my = vax_my[['daily_partial', 'daily_full']].copy()

            q4_my = pd.concat([q4_cases_my,q4_vax_my], axis=1)
            corr_my = q4_my.corr()

            plt.figure(figsize=(5,5))
            sns.heatmap(corr_my),plt.title('Malaysia')
            st.pyplot(plt)
            st.markdown('The cases_new is highly correlated to daily_partial and daily_full. This indicates that the vaccine can affects the number of daily new cases in Malaysia')
        elif selectChoice == 'Perlis':
            q4_cases = cases_state[cases_state['date'] > '2021-02-23']
            q4_cases_daily = q4_cases[['date','state','cases_new']].copy()
            q4_cases_daily = q4_cases_daily.reset_index(drop=True)

            q4_vax_daily = vax_state[['daily_partial', 'daily_full']].copy()

            q4_daily = pd.concat([q4_cases_daily,q4_vax_daily], axis=1)
            q4_temp = q4_daily[q4_daily['state'] == selectChoice]
            q4_temp = q4_temp.corr()

            plt.figure(figsize=(5,5))
            sns.heatmap(q4_temp),plt.title(selectChoice)
            st.pyplot(plt)
            st.markdown('The new cases of COVID - 19 in Perlis does not correlates well with number of vaccination. This may cause by Perlis has a lower number of daily new cases.')
        elif selectChoice == 'Sarawak':
            q4_cases = cases_state[cases_state['date'] > '2021-02-23']
            q4_cases_daily = q4_cases[['date','state','cases_new']].copy()
            q4_cases_daily = q4_cases_daily.reset_index(drop=True)

            q4_vax_daily = vax_state[['daily_partial', 'daily_full']].copy()

            q4_daily = pd.concat([q4_cases_daily,q4_vax_daily], axis=1)
            q4_temp = q4_daily[q4_daily['state'] == selectChoice]
            q4_temp = q4_temp.corr()

            plt.figure(figsize=(5,5))
            sns.heatmap(q4_temp),plt.title(selectChoice)
            st.pyplot(plt)
            st.markdown('The new cases of COVID - 19 in Sarawak does not correlates well with number of vaccination. This may cause by the lower vaccination rate in Sarawak.')
        else:
            q4_cases = cases_state[cases_state['date'] > '2021-02-23']
            q4_cases_daily = q4_cases[['date','state','cases_new']].copy()
            q4_cases_daily = q4_cases_daily.reset_index(drop=True)

            q4_vax_daily = vax_state[['daily_partial', 'daily_full']].copy()

            q4_daily = pd.concat([q4_cases_daily,q4_vax_daily], axis=1)
            q4_temp = q4_daily[q4_daily['state'] == selectChoice]
            q4_temp = q4_temp.corr()

            plt.figure(figsize=(5,5))
            sns.heatmap(q4_temp),plt.title(selectChoice)
            st.pyplot(plt)
            st.markdown('In general, the daily new cases correlates with the number of vaccination')
    else:
        if selectChoice == 'Malaysia':
            q4_cases = cases_malaysia[cases_malaysia['date'] > '2021-02-23']
            q4_cases_my_child = q4_cases[['date','cases_child']].copy()
            q4_cases_my_child['cases_child'] = q4_cases_my_child['cases_child'].fillna(0)
            q4_cases_my_child = q4_cases_my_child.reset_index(drop=True)

            q4_vax_my_child = vax_my[['daily_partial_child', 'daily_full_child']].copy()

            q4_my_child = pd.concat([q4_cases_my_child,q4_vax_my_child], axis=1)
            corr_child = q4_my_child.corr()

            plt.figure(figsize=(10,10))
            sns.heatmap(corr_child),plt.title('Malaysia-Child')
            st.pyplot(plt)
            st.markdown('The cases_child is not highly correlated as shown in the graph above. This may due to the child vaccination just started so there is less child got vaccinated. There are not much data to support the correlation between the daily new case and vaccination of the child.')
        else:
            q4_cases = cases_state[cases_state['date'] > '2021-02-23']
            q4_cases_daily_child = q4_cases[['date','state','cases_child']].copy()
            q4_cases_daily_child['cases_child'] = q4_cases_daily_child['cases_child'].fillna(0)
            q4_cases_daily_child = q4_cases_daily_child.reset_index(drop=True)

            q4_vax_daily_child = vax_state[['daily_partial_child', 'daily_full_child']].copy()

            q4_daily_child = pd.concat([q4_cases_daily_child,q4_vax_daily_child], axis=1)
            q4_temp_child = q4_daily_child[q4_daily_child['state'] == selectChoice]
            q4_temp_child = q4_temp_child.corr()


            plt.figure(figsize=(5,5))
            sns.heatmap(q4_temp_child),plt.title(selectChoice+'-Child')
            st.pyplot(plt)
            st.markdown('In general, new case of children COVID-19 does not correlated in the state level. This shows the same results as the national level as the child vaccination programme just started. Hence, there is not much of data to support the correlation.')

