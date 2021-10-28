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

def classification3():

    st.markdown('# State prediction')

    final_merged_state = pd.read_csv('Dataset/final_merged_state.csv')

    X_RFE_state = final_merged_state.drop(columns=['state', 'date']).copy()
    y_RFE_state = final_merged_state['state'].copy()

    strong_features_state = ['cases_new',
                            'beds_icu_covid',
                            'beds_covid',
                            'beds_noncrit',
                            'hosp_admitted_pui',
                            'hosp_admitted_covid',
                            'hosp_admitted_total',
                            'hosp_discharged_pui',
                            'hosp_discharged_total',
                            'hosp_covid',
                            'hosp_pui',
                            'hosp_noncovid',
                            'beds_icu',
                            'beds_icu_rep',
                            'beds_icu_total',
                            'vent',
                            'pkrc_noncovid',
                            'vent_port',
                            'icu_covid',
                            'icu_pui',
                            'icu_noncovid',
                            'vent_covid',
                            'vent_noncovid',
                            'vent_used',
                            'daily_full',
                            'daily',
                            'cumul_partial',
                            'cumul_full',
                            'cumul',
                            'cumul_partial_child',
                            'beds_y',
                            'hosp_discharged_covid',
                            'pkrc_pui',
                            'pkrc_discharged_total',
                            'pkrc_discharged_covid',
                            'pkrc_discharged_pui',
                            'pkrc_admitted_total',
                            'pkrc_admitted_covid',
                            'rtk-ag',
                            'pkrc_admitted_pui',
                            'beds_x',
                            'pkrc_covid',
                            'deaths_pvax',
                            'deaths_new_dod',
                            'cases_cluster',
                            'positivity_rate',
                            'daily_partial_child',
                            'pfizer2',
                            'cumul_full_child',
                            'cases_active',
                            'cases_adolescent',
                            'vent_port_used',
                            'daily_partial']

    X_RFE_state = X_RFE_state[strong_features_state].copy()

    st.write('Table below shows the number of records for each state. The dataset is balanced, hence SMOTE is not performed.')
    st.write(y_RFE_state.value_counts())

    X_train, X_test, y_train, y_test = train_test_split(X_RFE_state, y_RFE_state, test_size=0.3, random_state=1)

    st.markdown('** LGBM Classifier **')

    # Confusion Matrix
    lgbm = pickle.load(open('Model/lgbm_state_1', 'rb'))
    y_pred_lgbm  = lgbm.predict(X_test)
    st.text('Model Report:\n ' + classification_report(y_test, y_pred_lgbm))

    fig1,ax1 = plt.subplots(figsize = (20,10))
    ax1.set_title("Confusion Matrix for LGBM Classifier")
    conf_matrix_lgbm = confusion_matrix(y_test, y_pred_lgbm)
    lgbm_display = ConfusionMatrixDisplay(confusion_matrix=conf_matrix_lgbm,display_labels = lgbm.classes_)
    lgbm_display.plot(cmap = 'Greens',xticks_rotation ='vertical',ax=ax1)
    st.pyplot(fig1)
    
    st.markdown('The first plot above shows the confusion matrix for the LGBM Classifier. This classifier has high accuracy of classifying state based on Covid data.')

    rfc = pickle.load(open('Model/rfc_state_1', 'rb'))
    y_pred_rfc = rfc.predict(X_test)
    
    st.markdown('** Random Forest Classifier **')
    st.text('Model Report:\n ' + classification_report(y_test, y_pred_rfc))

    fig2,ax2 = plt.subplots(figsize = (20,10))
    ax2.set_title("Confusion Matrix for Random Forest Classifier")
    conf_matrix_rfc = confusion_matrix(y_test, y_pred_rfc)
    rfc_display = ConfusionMatrixDisplay(confusion_matrix=conf_matrix_rfc,display_labels = rfc.classes_)
    rfc_display.plot(cmap = 'Greens',xticks_rotation ='vertical',ax=ax2)
    st.pyplot(fig2)

    st.markdown('The second plot above shows the confusion matrix for the Random Forest Classifier. This classifier also has high accuracy of classifying state based on Covid data. This classifier has a similar accuracy with the LGBM Classifier. ')

