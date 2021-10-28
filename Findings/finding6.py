import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def finding6():
    population = pd.read_csv('Dataset/population.csv')
    vax_state = pd.read_csv('Dataset/vax_state.csv')

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
    st.markdown('Table below shows the population and the number of vaccination of each state in Malaysia.')
    st.dataframe(population)

    population['adult_partially_vax(%)'] = population['adult_partial'] / population['pop_adult'] * 100
    population['adult_fully_vax(%)'] = population['adult_fully'] / population['pop_adult'] * 100
    population['child_partially_vax(%)'] = population['child_partial'] / population['pop_child'] * 100
    population['child_fully_vax(%)'] = population['child_fully'] / population['pop_child'] * 100
    population['all_partially_vax(%)'] = population['all_partial'] / population['pop'] * 100
    population['all_fully_vax(%)'] = population['all_fully'] / population['pop'] * 100
    #population.sort_values('all_fully_vax(%)', ascending=False)
    fig, ax = plt.subplots(3,figsize=(15,15))

    ax[0].bar(population.index, population['all_fully_vax(%)'])
    ax[0].set_ylabel('Vax rate(%)')
    ax[0].set_title('Vaccination Rate for Each State (All Population)')
    ax[0].xaxis.set_tick_params(rotation=20)

    ax[1].bar(population.index, population['adult_fully_vax(%)'])
    ax[1].set_ylabel('Vax rate(%)')
    ax[1].set_title('Vaccination Rate for Each State (Adult Population)')
    ax[1].xaxis.set_tick_params(rotation=20)

    ax[2].bar(population.index, population['child_fully_vax(%)'])
    ax[2].set_ylabel('Vax rate(%)')
    ax[2].set_title('Vaccination Rate for Each State (Child Population)')
    ax[2].xaxis.set_tick_params(rotation=20)

    st.pyplot(fig)
    st.markdown('From the three graphs above, we can observe that the vaccination rate of Kuala Lumpur and Putrajaya has outperformed other states in all population and adult population. From the first and second graph, we can notice that the vaccination rate of some states has exceed 100%. This is probably because some people originated in other states took their vaccines in another state, or the records of foreign workers are counted in the state where they took their vaccines. For child population, Pulau Pinang has the highest vaccination rate followed by Perak.')



