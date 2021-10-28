import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt 
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, plot_confusion_matrix, plot_roc_curve, plot_precision_recall_curve
from sklearn.metrics import mean_squared_error as mse, mean_absolute_error, roc_curve, accuracy_score, classification_report, roc_auc_score, precision_recall_curve

def classification2():

    st.markdown('# Daily Deaths Classification')

    final_merged_malaysia = pd.read_csv('Dataset/final_merged_malaysia.csv')

    X_RFE_deaths = final_merged_malaysia.drop(columns=['deaths_new', 'date']).copy()
    y_RFE_deaths = final_merged_malaysia['deaths_new'].copy()
    y_RFE_deaths = pd.cut(y_RFE_deaths, 3, labels=['Low','Medium','High'])

    strong_features_deaths = ['cases_new',
                            'vent',
                            'vent_pui',
                            'vent_covid',
                            'icu_noncovid',
                            'icu_pui',
                            'icu_covid',
                            'vent_port',
                            'beds_icu_covid',
                            'vent_port_used',
                            'beds_icu_total',
                            'beds_icu_rep',
                            'hosp_noncovid',
                            'hosp_pui',
                            'hosp_covid',
                            'hosp_discharged_pui',
                            'vent_used',
                            'daily_partial',
                            'hosp_admitted_covid',
                            'pfizer1',
                            'cansino',
                            'astra2',
                            'astra1',
                            'sinovac2',
                            'sinovac1',
                            'pfizer2',
                            'cumul_full_child',
                            'daily_full',
                            'cumul_partial_child',
                            'cumul',
                            'cumul_full',
                            'cumul_partial',
                            'daily_full_child',
                            'daily',
                            'hosp_admitted_total',
                            'hosp_discharged_covid',
                            'hosp_admitted_pui',
                            'deaths_tat',
                            'cases_recovered',
                            'cases_active',
                            'cases_pvax',
                            'cases_fvax',
                            'cases_child',
                            'cases_elderly',
                            'pcr',
                            'total_tests',
                            'positivity_rate',
                            'deaths_bid',
                            'deaths_new_dod',
                            'deaths_bid_dod',
                            'beds_noncrit',
                            'deaths_fvax',
                            'deaths_pvax',
                            'beds_x',
                            'pkrc_admitted_covid',
                            'pkrc_admitted_total',
                            'pkrc_discharged_pui',
                            'pkrc_discharged_covid',
                            'pkrc_discharged_total',
                            'beds_covid',
                            'pkrc_covid',
                            'pkrc_pui',
                            'beds_y',
                            'pkrc_noncovid',
                            'cases_adolescent',
                            'daily_partial_child',
                            'hosp_discharged_total']

    X_RFE_deaths = X_RFE_deaths[strong_features_deaths].copy()

    st.markdown('## Before SMOTE')

    st.write('Table below shows the number of records for each category of deaths (Low, Medium, High).')
    st.write(y_RFE_deaths.value_counts())

    X_train, X_test, y_train, y_test = train_test_split(X_RFE_deaths, y_RFE_deaths, test_size=0.3, random_state=1)

    st.markdown('** LGBM Classifier **')

    # Confusion Matrix
    lgbm = pickle.load(open('Model/lgbm_deaths_1', 'rb'))
    y_pred_lgbm  = lgbm.predict(X_test)
    st.text('Model Report:\n ' + classification_report(y_test, y_pred_lgbm))

    fig1,ax1 = plt.subplots(figsize = (20,10))
    ax1.set_title("Confusion Matrix for LGBM Classifier")
    conf_matrix_lgbm = confusion_matrix(y_test, y_pred_lgbm)
    lgbm_display = ConfusionMatrixDisplay(confusion_matrix=conf_matrix_lgbm,display_labels = lgbm.classes_)
    lgbm_display.plot(cmap = 'Greens',xticks_rotation ='vertical',ax=ax1)
    st.pyplot(fig1)
    
    st.markdown('The first plot above shows the confusion matrix for the LGBM Classifier. This classifier has high accuracy for “low” and “medium” labels but has low accuracy for “high” label because of the imbalanced deaths data.')

    rfc = pickle.load(open('Model/rfc_deaths_1', 'rb'))
    y_pred_rfc = rfc.predict(X_test)
    
    st.markdown('** Random Forest Classifier **')
    st.text('Model Report:\n ' + classification_report(y_test, y_pred_rfc))

    fig2,ax2 = plt.subplots(figsize = (20,10))
    ax2.set_title("Confusion Matrix for Random Forest Classifier")
    conf_matrix_rfc = confusion_matrix(y_test, y_pred_rfc)
    rfc_display = ConfusionMatrixDisplay(confusion_matrix=conf_matrix_rfc,display_labels = rfc.classes_)
    rfc_display.plot(cmap = 'Greens',xticks_rotation ='vertical',ax=ax2)
    st.pyplot(fig2)

    st.markdown('The second plot above shows the confusion matrix for the Random Forest Classifier. This classifier has high accuracy for “low” and “medium” labels but has low accuracy for “high” label because of the imbalanced deaths data. This classifier has a similar accuracy with the LGBM classifier but the f1-score of this classifier is worse than LGBM Classifier in "High" label. ')
 










    st.markdown('## After SMOTE')
    X_resampled, y_resampled = SMOTE(k_neighbors=4).fit_resample(X_RFE_deaths, y_RFE_deaths)

    st.write('Table below shows the number of records for each category of deaths (Low, Medium, High).')
    st.write(y_resampled.value_counts())

    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=1)

    st.markdown('** LGBM Classifier **')

    # Confusion Matrix
    lgbm = pickle.load(open('Model/lgbm_deaths_2', 'rb'))
    y_pred_lgbm  = lgbm.predict(X_test)
    st.text('Model Report:\n ' + classification_report(y_test, y_pred_lgbm))

    fig1,ax1 = plt.subplots(figsize = (20,10))
    ax1.set_title("Confusion Matrix for LGBM Classifier")
    conf_matrix_lgbm = confusion_matrix(y_test, y_pred_lgbm)
    lgbm_display = ConfusionMatrixDisplay(confusion_matrix=conf_matrix_lgbm,display_labels = lgbm.classes_)
    lgbm_display.plot(cmap = 'Greens',xticks_rotation ='vertical',ax=ax1)
    st.pyplot(fig1)
    
    st.markdown('The first plot above shows the confusion matrix for the LGBM Classifier trained and tested on oversampled dataset. This classifier has high accuracy for all three labels but with few wrong predictions.')

    rfc = pickle.load(open('Model/rfc_deaths_2', 'rb'))
    y_pred_rfc = rfc.predict(X_test)
    
    st.markdown('** Random Forest Classifier **')
    st.text('Model Report:\n ' + classification_report(y_test, y_pred_rfc))

    fig2,ax2 = plt.subplots(figsize = (20,10))
    ax2.set_title("Confusion Matrix for Random Forest Classifier")
    conf_matrix_rfc = confusion_matrix(y_test, y_pred_rfc)
    rfc_display = ConfusionMatrixDisplay(confusion_matrix=conf_matrix_rfc,display_labels = rfc.classes_)
    rfc_display.plot(cmap = 'Greens',xticks_rotation ='vertical',ax=ax2)
    st.pyplot(fig2)

    st.markdown('The second plot above shows the confusion matrix for the Random Forest Classifier trained and tested on oversampled dataset. This classifier has high accuracy for all three labels but with few wrong predictions. This classifier has a similar accuracy with the LGBM classifier but the f1-score of this classifier is worse than LGBM Classifier in overall. In overall, the performance of the models trained and tested on oversampled dataset are better than the previous models. Hence, performing oversampling on this imbalance deaths data does improve the performance of models in overall.')
 