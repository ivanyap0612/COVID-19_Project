import datetime
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def finding7():
    end_date = pd.to_datetime('2021-10-25').date()
    days = datetime.timedelta(30)
    start_date = end_date-days

    population = pd.read_csv('Dataset/population.csv')
    vax_state = pd.read_csv('Dataset/vax_state.csv')
    cases_state = pd.read_csv('Dataset/cases_state.csv')

    population.drop(['idxs'], axis=1, inplace=True)
    population = population.drop(0).set_index('state')
    population['pop_adult'] = population['pop_18'] + population['pop_60']
    population['pop_child'] = population['pop'] - population['pop_adult']

    population['adult_partial'] = vax_state.groupby('state').sum()['daily_partial']
    population['adult_fully'] = vax_state.groupby('state').sum()['daily_full']
    population['child_partial'] = vax_state.groupby('state').sum()['daily_partial_child']
    population['child_fully'] = vax_state.groupby('state').sum()['daily_full_child']
    population['all_partial'] = population['adult_partial'] + population['child_partial']
    population['all_fully'] = population['adult_fully'] + population['child_fully']

    population['adult_partially_vax(%)'] = population['adult_partial'] / population['pop_adult'] * 100
    population['adult_fully_vax(%)'] = population['adult_fully'] / population['pop_adult'] * 100
    population['child_partially_vax(%)'] = population['child_partial'] / population['pop_child'] * 100
    population['child_fully_vax(%)'] = population['child_fully'] / population['pop_child'] * 100
    population['all_partially_vax(%)'] = population['all_partial'] / population['pop'] * 100
    population['all_fully_vax(%)'] = population['all_fully'] / population['pop'] * 100

    population['average_cases'] = cases_state.set_index('date').loc[str(start_date):str(end_date)].groupby('state').mean()['cases_new']
    st.dataframe(population.sort_values('average_cases', ascending=False))
    st.markdown('In our opinion, we think that the states with low vaccination rate but higher amount of cases or the states with high vaccination rate but still with higher amount of cases require attentions. From the data above, we can see that Selangor with 1257 cases per day in average has only 68.51% of population (lowest rate) has been fully vaccinated. Hence, Selangor should speed up the vaccination process to increase the vaccination rate so that the amount of new cases can be reduced. On the other hand, Sarawak has 80.43% of vaccination rate but also having the highest amount of new cases in average in the past month. Hence, Sarawak is also required more attentions to take necessary actions to lower the amount of new cases.')