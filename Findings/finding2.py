import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


def finding2():
    vax_my = pd.read_csv('Dataset/vax_malaysia.csv')
    vax = vax_my[['pfizer1', 'pfizer2', 'sinovac1', 'sinovac2', 'astra1', 'astra2', 'cansino']]
    fig1,ax1 = plt.subplots(figsize = (20,10))
    vax.cumsum().iloc[-1].plot(kind='bar')
    ax1.set_title("Number of vaccines taken used (First/Second dose)")
    ax1.bar_label(ax1.containers[0])
    st.pyplot(fig1)

    st.markdown('Based on the graph above, it is obvious that Pfizer is the most widely used vaccine in Malaysia, followed by Sinovac.')