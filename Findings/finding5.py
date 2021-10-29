import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def finding5():

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
    f5_vax_my = vax_my[['date','daily_partial_child','daily_full_child','cumul_partial_child','cumul_full_child']]
    f5_cases_malaysia = cases_malaysia[['date','cases_child','cases_adolescent','cases_adult','cases_elderly']]
    f5_merge_my = f5_cases_malaysia.merge(f5_vax_my, on=['date'], how='inner')

    #States
    f5_cases_states = vax_state[['date','state','daily_partial_child','daily_full_child','cumul_partial_child','cumul_full_child']]
    f5_vax_states = cases_state[['date','state','cases_child','cases_adolescent','cases_adult','cases_elderly']]
    f5_merge_state = f5_cases_states.merge(f5_vax_states, on=['date','state'], how='inner')

    selectChoice = st.selectbox("Select a location to view", ['Malaysia','Johor','Kedah','Kelantan','Melaka','Negeri Sembilan','Pahang','Pulau Pinang','Perak','Perlis','Selangor','Terengganu','Sabah','Sarawak','W.P. Kuala Lumpur','W.P. Labuan','W.P. Putrajaya'])

    if selectChoice == 'Malaysia':
        plt.figure(figsize=(20,15))
        sns.lineplot(x="cumul_full_child", y="cases_child",data=f5_merge_my)
        plt.title('Effect of Number of Fully Vaccinated (children < 18yo) on New COVID-19 Cases in Malaysia')
        plt.xlabel('Cumulative Number of Children (< 18yo) who is Fully Vaccinated')
        plt.ylabel('Number of New COVID-19 Cases')
        st.pyplot(plt)

        st.markdown('Based on the graph above, it can be seen that total number of new COVID-19 cases have started to reduce after a certain number of vaccinated people has been reached. This has proven that vaccine is effective against COVID-19 for children under 18 years old.')
    
    else:
        f5_merge_state_total = f5_merge_state[f5_merge_state['state'] == selectChoice]
        plt.figure(figsize=(20,15))
        sns.lineplot(x="cumul_full_child", y="cases_child",data=f5_merge_state_total)
        plt.title('Effect of Number of Fully Vaccinated (children < 18yo) on New COVID-19 Cases in '+ selectChoice)
        plt.xlabel('Cumulative Number of Children (< 18yo) who is Fully Vaccinated')
        plt.ylabel('Number of New COVID-19 Cases')
        st.pyplot(plt)

        st.markdown('Based on the graph above, it can be seen that total number of new COVID-19 cases have started to reduce after a certain number of vaccinated people has been reached. This has proven that vaccine is effective against COVID-19 for children under 18 years old.')