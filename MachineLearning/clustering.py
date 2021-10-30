from sklearn.cluster import KMeans
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 

def clustering():
    cases_malaysia = pd.read_csv('Dataset/cases_malaysia.csv')
    raw_death_my = pd.read_csv("Dataset/deaths_malaysia.csv")
    cases_malaysia['date'] = pd.to_datetime(cases_malaysia['date'])
    raw_death_my['date']= pd.to_datetime(raw_death_my['date'])
    final_death_my = raw_death_my.copy()

    cases_clustering = cases_malaysia[['date','cases_new']].copy()
    death_clustering = final_death_my[['date','deaths_new']].copy()
    clustering = cases_clustering.merge(death_clustering, how='inner', on=['date'])

    st.markdown('Before Clustering: ')
    plt.figure(figsize=(25,15))
    sns.scatterplot(x='cases_new', y='deaths_new', data=clustering)
    st.pyplot(plt)

    clustering_X = clustering.drop(['date'], axis=1)
    km = KMeans(n_clusters=6, random_state=1).fit(clustering_X)
    clustering_new = clustering.copy()
    clustering_new['cluster']=km.labels_

    st.markdown('After Clustering: ')
    plt.figure(figsize=(15,10))
    sns.scatterplot(x='cases_new', y='deaths_new', hue='cluster', data=clustering_new, palette="hls")
    st.pyplot(plt)

    st.markdown('From the graph above, we can know there are 5 different clusters of COVID-19 cases in Malaysia. This shows that there are 5 different levels of COVID-19 in Malaysia from the least serious to most serious day.')
