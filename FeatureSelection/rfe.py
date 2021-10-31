import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import RFECV
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier

def ranking(ranks, names, order=1):
    minmax = MinMaxScaler()
    ranks = minmax.fit_transform(order*np.array([ranks]).T).T[0]
    ranks = map(lambda x: round(x,2), ranks)
    return dict(zip(names, ranks))

def rfe():
    final_merged_malaysia = pd.read_csv('Dataset/final_merged_malaysia.csv')
    final_merged_state = pd.read_csv('Dataset/final_merged_state.csv')

    # Cases
    st.markdown('### Cases')
    X_RFE_cases = final_merged_malaysia.drop(columns=['cases_new', 'date']).copy()
    y_RFE_cases = final_merged_malaysia['cases_new'].copy()
    y_RFE_cases = pd.cut(y_RFE_cases, 3, labels=['Low','Medium','High'])

    colnames = X_RFE_cases.columns

    rf = RandomForestClassifier(n_jobs=-1, class_weight="balanced", max_depth=6, n_estimators=50)

    rfe = RFECV(rf, min_features_to_select = 1, cv=3, verbose=1)
    rfe.fit(X_RFE_cases,y_RFE_cases)

    rfe_score = ranking(list(map(float, rfe.ranking_)), colnames, order=-1)
    rfe_score = pd.DataFrame(list(rfe_score.items()), columns=['Features', 'Score'])
    rfe_score = rfe_score.sort_values("Score", ascending = False)
    strong_features_cases = rfe_score[rfe_score['Score']>0.75].Features.values.tolist()
    
    sns_rfe_plot = sns.catplot(x="Score", y="Features", data = rfe_score[rfe_score['Score']>0.75], kind = "bar", 
               height=14, aspect=1.9, palette='coolwarm')
    plt.title("RFE Cases Top Features")
    st.pyplot(sns_rfe_plot)

    # Deaths
    st.markdown('### Deaths')
    X_RFE_deaths = final_merged_malaysia.drop(columns=['deaths_new', 'date']).copy()
    y_RFE_deaths = final_merged_malaysia['deaths_new'].copy()
    y_RFE_deaths = pd.cut(y_RFE_deaths, 3, labels=['Low','Medium','High'])

    colnames = X_RFE_deaths.columns

    rf = RandomForestClassifier(n_jobs=-1, class_weight="balanced", max_depth=6, n_estimators=50)

    rfe = RFECV(rf, min_features_to_select = 1, cv=3, verbose=1)
    rfe.fit(X_RFE_deaths,y_RFE_deaths)

    rfe_score = ranking(list(map(float, rfe.ranking_)), colnames, order=-1)
    rfe_score = pd.DataFrame(list(rfe_score.items()), columns=['Features', 'Score'])
    rfe_score = rfe_score.sort_values("Score", ascending = False)
    strong_features_deaths = rfe_score[rfe_score['Score']>0.75].Features.values.tolist()

    sns_rfe_plot = sns.catplot(x="Score", y="Features", data = rfe_score[rfe_score['Score']>0.75], kind = "bar", 
               height=14, aspect=1.9, palette='coolwarm')
    plt.title("RFE Deaths Top Features")
    st.pyplot(sns_rfe_plot)

    # State
    st.markdown('### State')
    X_RFE_state = final_merged_state.drop(columns=['state', 'date']).copy()
    y_RFE_state = final_merged_state['state'].copy()

    colnames = X_RFE_state.columns

    rf = RandomForestClassifier(n_jobs=-1, class_weight="balanced", max_depth=6, n_estimators=50)

    rfe = RFECV(rf, min_features_to_select = 1, cv=3, verbose=1)
    rfe.fit(X_RFE_state,y_RFE_state)

    rfe_score = ranking(list(map(float, rfe.ranking_)), colnames, order=-1)
    rfe_score = pd.DataFrame(list(rfe_score.items()), columns=['Features', 'Score'])
    rfe_score = rfe_score.sort_values("Score", ascending = False)
    strong_features_state = rfe_score[rfe_score['Score']>0.75].Features.values.tolist()

    sns_rfe_plot = sns.catplot(x="Score", y="Features", data = rfe_score[rfe_score['Score']>0.75], kind = "bar", 
               height=14, aspect=1.9, palette='coolwarm')
    plt.title("RFE Deaths Top Features")
    st.pyplot(sns_rfe_plot)

    return strong_features_cases, strong_features_deaths, strong_features_state
