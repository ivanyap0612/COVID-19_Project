import datetime
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def finding8():
    cases_state = pd.read_csv('Dataset/cases_state.csv')
    cases_state['date'] = pd.to_datetime(cases_state['date'])
    q5_cases = cases_state[['date', 'state', 'cases_new']].copy()
    q5_cases = q5_cases[q5_cases['date'] > '2021-06-14']
    q5_kedah = q5_cases[q5_cases['state'] == 'Kedah']
    q5_kedah = q5_kedah.reset_index(drop=True)
    q5_perak = q5_cases[q5_cases['state'] == 'Perak']
    q5_perak = q5_perak.reset_index(drop=True)
    q5_selangor = q5_cases[q5_cases['state'] == 'Selangor']
    q5_selangor = q5_selangor.reset_index(drop=True)
    q5_ns = q5_cases[q5_cases['state'] == 'Negeri Sembilan']
    q5_ns = q5_ns.reset_index(drop=True)

    kedah_phase = []
    p3_kedah = len(q5_kedah) - 124
    for i in range(108):
        kedah_phase.append('Phase 1')
    for i in range(17):
        kedah_phase.append('Phase 2')
    for i in range(p3_kedah):
        kedah_phase.append('Phase 3')
    kedah_phase = pd.DataFrame(kedah_phase, columns=['National Recovery Plan'])

    perak_phase = []
    p3_perak = len(q5_perak) - 124
    for i in range(20):
        perak_phase.append('Phase 1')
    for i in range(105):
        perak_phase.append('Phase 2')
    for i in range(p3_perak):
        perak_phase.append('Phase 3')
    perak_phase = pd.DataFrame(perak_phase, columns=['National Recovery Plan'])

    selangor_phase = []
    p4_selangor = len(q5_selangor) - 124
    for i in range(87):
        selangor_phase.append('Phase 1')
    for i in range(21):
        selangor_phase.append('Phase 2')
    for i in range(17):
        selangor_phase.append('Phase 3')
    for i in range(p4_selangor):
        selangor_phase.append('Phase 4')
    selangor_phase = pd.DataFrame(selangor_phase, columns=['National Recovery Plan'])

    ns_phase = []
    p4_ns = len(q5_ns) - 101
    for i in range(72):
        ns_phase.append('Phase 1')
    for i in range(9):
        ns_phase.append('Phase 2')
    for i in range(20):
        ns_phase.append('Phase 3')
    for i in range(p4_ns):
        ns_phase.append('Phase 4')
    ns_phase = pd.DataFrame(ns_phase, columns=['National Recovery Plan'])

    q5_kedah = pd.concat([q5_kedah,kedah_phase], axis=1)
    q5_perak = pd.concat([q5_perak,perak_phase], axis=1)
    q5_selangor = pd.concat([q5_selangor,selangor_phase], axis=1)
    q5_ns = pd.concat([q5_ns,ns_phase], axis=1)

    st.markdown('Kedah')
    plt.figure(figsize=(20,10))
    sns.lineplot(x="date", y="cases_new", hue="National Recovery Plan", data=q5_kedah)
    plt.title('New Cases during National Recovery Plan in Kedah')
    st.pyplot(plt)

    st.markdown('Perak')
    plt.figure(figsize=(20,10))
    sns.lineplot(x="date", y="cases_new", hue="National Recovery Plan", data=q5_perak)
    plt.title('New Cases during National Recovery Plan in Perak')
    st.pyplot(plt)

    st.markdown('Selangor')
    plt.figure(figsize=(20,10))
    sns.lineplot(x="date", y="cases_new", hue="National Recovery Plan", data=q5_selangor)
    plt.title('New Cases during National Recovery Plan in Selangor')
    st.pyplot(plt)

    st.markdown('Negeri Sembilan')
    plt.figure(figsize=(20,10))
    sns.lineplot(x="date", y="cases_new", hue="National Recovery Plan", data=q5_ns)
    plt.title('New Cases during National Recovery Plan in Negeri Sembilan')
    st.pyplot(plt)

    st.markdown('The NRP does not affects the daily new cases. This can be shown as the phase progresses, the number of daily cases is reduced. This can also prove that the vaccination does help in reducing the total number of daily cases in Malaysia')



    
