import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def finding1():
    #reading datasets
    cases_malaysia = pd.read_csv('Dataset/cases_malaysia.csv')
    cases_state = pd.read_csv('Dataset/cases_state.csv')

    #data preprocessing
    cases_malaysia['date'] = pd.to_datetime(cases_malaysia['date'])
    cases_state['date'] = pd.to_datetime(cases_state['date'])
    cases_malaysia.fillna(value = 0, inplace = True)
    cases_state.fillna(value = 0, inplace = True)
    f1_cases_malaysia = cases_malaysia[['date','cases_child','cases_adolescent','cases_adult','cases_elderly']]
    f1_cases_state = cases_state[['date','state','cases_child','cases_adolescent','cases_adult','cases_elderly']]

    selectChoice = st.selectbox("Select a location to view", ['Malaysia','Johor','Kedah','Kelantan','Melaka','Negeri Sembilan','Pahang','Pulau Pinang','Perak','Perlis','Selangor','Terengganu','Sabah','Sarawak','W.P. Kuala Lumpur','W.P. Labuan','W.P. Putrajaya'])
    #plotting
    if selectChoice == 'Malaysia':
        plt.figure(figsize=(20,15))
        x = f1_cases_malaysia['date']
        y1 = f1_cases_malaysia['cases_child']
        y2 = f1_cases_malaysia['cases_adolescent']
        y3 = f1_cases_malaysia['cases_adult']
        y4 = f1_cases_malaysia['cases_elderly']
        plt.plot(x, y1, label = "Child(0-11)")
        plt.plot(x, y2, label = "Adolescent(12-17)")
        plt.plot(x, y3, label = "Adult(18-59)")
        plt.plot(x, y4, label = "Elderly(60+)")
        plt.xlabel('Date')
        plt.ylabel('New Daily COVID-19 Cases')
        plt.title('Age Groups against New Daily COVID-19 Cases in Malaysia')
        # show a legend on the plot
        plt.legend()
        # Display a figure.
        st.pyplot(plt)
        st.markdown('Based on the graph above, it can be seen that adults have contributed the highest number of COVID-19 cases, followed by the children. This is because adults have the highest risk being infected by coronavirus as majority of the working adults work in areas at high risk for exposure to the coronavirus. College students who stay in the campus can be affected by campus outbreaks and spread the coronavirus when they return home. Children have contributed the second hghest number of COVID-19 cases. This may be due to the weak immune system of the individuals especially the babies.')

    else:
        f1_cases_state_total = f1_cases_state[f1_cases_state['state'] == selectChoice]
        plt.figure(figsize=(20,15))
        x = f1_cases_state_total['date']
        y1 = f1_cases_state_total['cases_child']
        y2 = f1_cases_state_total['cases_adolescent']
        y3 = f1_cases_state_total['cases_adult']
        y4 = f1_cases_state_total['cases_elderly']
        plt.plot(x, y1, label = "Child(0-11)")
        plt.plot(x, y2, label = "Adolescent(12-17)")
        plt.plot(x, y3, label = "Adult(18-59)")
        plt.plot(x, y4, label = "Elderly(60+)")
        plt.xlabel('Date')
        plt.ylabel('New Daily COVID-19 Cases')
        plt.title('Age Groups against New Daily COVID-19 Cases in ' + selectChoice)
        # show a legend on the plot
        plt.legend()
        # Display a figure.
        st.pyplot(plt)
        st.markdown('Based on the graph above, it can be seen that adults have contributed the highest number of COVID-19 cases, followed by the children. This is because adults have the highest risk being infected by coronavirus as majority of the working adults work in areas at high risk for exposure to the coronavirus. College students who stay in the campus can be affected by campus outbreaks and spread the coronavirus when they return home. Children have contributed the second hghest number of COVID-19 cases. This may be due to the weak immune system of the individuals especially the babies.')