import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from boruta import BorutaPy
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestClassifier

def ranking(ranks, names, order=1):
    minmax = MinMaxScaler()
    ranks = minmax.fit_transform(order*np.array([ranks]).T).T[0]
    ranks = map(lambda x: round(x,2), ranks)
    return dict(zip(names, ranks))

def boruta():
    final_merged_malaysia = pd.read_csv('Dataset/final_merged_malaysia.csv')
    final_merged_state = pd.read_csv('Dataset/final_merged_state.csv')

    # Cases
    st.markdown('### Cases')
    X_boruta_cases = final_merged_malaysia.drop(columns=['cases_new','date'])
    y_boruta_cases = final_merged_malaysia['cases_new']
    y_boruta_cases = pd.cut(y_boruta_cases, 3, labels=['Low','Medium','High'])
    colnames = X_boruta_cases.columns

    rfc = RandomForestClassifier(max_depth=4)
    feat_selector = BorutaPy(rfc, n_estimators = 'auto',max_iter=10,verbose=2,random_state=1)
    feat_selector.fit(X_boruta_cases.values,y_boruta_cases.values.ravel())#

    boruta_score = ranking(list(map(float, feat_selector.ranking_)), colnames, order=-1)
    boruta_score = pd.DataFrame(list(boruta_score.items()), columns=['Features', 'Score'])
    boruta_score = boruta_score.sort_values("Score", ascending = False)

    sns_boruta_plot = sns.catplot(x="Score", y="Features", data = boruta_score[boruta_score['Score']>0.75], kind = "bar", 
                height=8, aspect=1.5, palette='coolwarm')
    plt.title("Boruta Top Features")
    st.pyplot(sns_boruta_plot)

    # Deaths
    st.markdown('### Deaths')
    X_boruta_deaths = final_merged_malaysia.drop(columns=['deaths_new','date'])
    y_boruta_deaths = final_merged_malaysia['deaths_new']
    y_boruta_deaths = pd.cut(y_boruta_deaths, 3, labels=['Low','Medium','High'])
    colnames = X_boruta_deaths.columns

    rfc = RandomForestClassifier(max_depth=4)
    feat_selector = BorutaPy(rfc, n_estimators = 'auto',max_iter=10,verbose=2,random_state=1)
    feat_selector.fit(X_boruta_deaths.values,y_boruta_deaths.values.ravel())#

    boruta_score = ranking(list(map(float, feat_selector.ranking_)), colnames, order=-1)
    boruta_score = pd.DataFrame(list(boruta_score.items()), columns=['Features', 'Score'])
    boruta_score = boruta_score.sort_values("Score", ascending = False)

    sns_boruta_plot = sns.catplot(x="Score", y="Features", data = boruta_score[boruta_score['Score']>0.75], kind = "bar", 
                height=8, aspect=1.5, palette='coolwarm')
    plt.title("Boruta Top Features")
    st.pyplot(sns_boruta_plot)

    # State
    st.markdown('### State')
    X_boruta_state = final_merged_state.drop(columns=['state','date'])
    y_boruta_state = final_merged_state['state']
    colnames = X_boruta_state.columns

    rfc = RandomForestClassifier(max_depth=4)
    feat_selector = BorutaPy(rfc, n_estimators = 'auto',max_iter=10,verbose=2,random_state=1)
    feat_selector.fit(X_boruta_state.values,y_boruta_state.values.ravel())#

    boruta_score = ranking(list(map(float, feat_selector.ranking_)), colnames, order=-1)
    boruta_score = pd.DataFrame(list(boruta_score.items()), columns=['Features', 'Score'])
    boruta_score = boruta_score.sort_values("Score", ascending = False)

    sns_boruta_plot = sns.catplot(x="Score", y="Features", data = boruta_score[boruta_score['Score']>0.75], kind = "bar", 
                height=8, aspect=1.5, palette='coolwarm')
    plt.title("Boruta Top Features")
    st.pyplot(sns_boruta_plot)
    