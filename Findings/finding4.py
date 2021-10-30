import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def finding4():
    #reading datasets
    vax_my = pd.read_csv('Dataset/vax_malaysia.csv')
    vax_state = pd.read_csv('Dataset/vax_state.csv')
    cases_malaysia = pd.read_csv('Dataset/cases_malaysia.csv')
    cases_state = pd.read_csv('Dataset/cases_state.csv')

    #data preprocessing
    vax_my['date']= pd.to_datetime(vax_my['date'])
    vax_state['date']= pd.to_datetime(vax_state['date'])
    cases_malaysia['date'] = pd.to_datetime(cases_malaysia['date'])
    cases_state['date'] = pd.to_datetime(cases_state['date'])
    cases_malaysia.fillna(value = 0, inplace = True)
    cases_state.fillna(value = 0, inplace = True)

    #Malaysia
    f4_vax_my = vax_my[['date','daily_partial', 'daily_full','daily','cumul_partial','cumul_full']]
    f4_cases_malaysia = cases_malaysia[['date','cases_new']]
    f4_merge_my = f4_cases_malaysia.merge(f4_vax_my, on=['date'], how='inner')

    #States
    f4_cases_states = cases_state[['date','state','cases_new']]
    f4_vax_states = vax_state[['date','state','daily_partial', 'daily_full','daily','cumul_partial','cumul_full']]
    f4_merge_state = f4_cases_states.merge(f4_vax_states, on=['date','state'], how='inner')

    selectChoice = st.selectbox("Select a location to view", ['Malaysia','Johor','Kedah','Kelantan','Melaka','Negeri Sembilan','Pahang','Pulau Pinang','Perak','Perlis','Selangor','Terengganu','Sabah','Sarawak','W.P. Kuala Lumpur','W.P. Labuan','W.P. Putrajaya'])
    #plotting
    if selectChoice == 'Malaysia':
        plt.figure(figsize=(20,15))
        sns.lineplot(x="cumul_full", y="cases_new",data=f4_merge_my)
        plt.title('Effect of Number of Fully Vaccinated on New COVID-19 Cases in Malaysia')
        plt.xlabel('Cumulative Number of Fully Vaccinated')
        plt.ylabel('Number of New COVID-19 Cases')
        st.pyplot(plt)

        st.markdown('Based on the graph above, it can be seen that total number of new COVID-19 cases have started to reduce after a certain number of vaccinated people has been reached. This has proven that vaccine is effective against COVID-19 and helps to reduce the number of COVID-19 cases. Besides, individuals may not have the best protection until 7–14 days after their second dose of the vaccine. Therefore, the total number of new COVID-19 cases does not drop immediately.')

    else:
        f4_merge_state_total = f4_merge_state[f4_merge_state['state'] == selectChoice]
        plt.figure(figsize=(20,15))
        sns.lineplot(x="cumul_full", y="cases_new",data=f4_merge_state_total)
        plt.title('Effect of Number of Fully Vaccinated on New COVID-19 Cases in '+ selectChoice)
        plt.xlabel('Cumulative Number of Fully Vaccinated')
        plt.ylabel('Number of New COVID-19 Cases')
        st.pyplot(plt)
        
        st.markdown('Based on the graph above, it can be seen that total number of new COVID-19 cases for every state has started to drop after a certain number of vaccinated people has been reached. Besides, every state has shown that vaccination has helped to reduce the daily cases after some times. This has proven that vaccine is effective against COVID-19.')