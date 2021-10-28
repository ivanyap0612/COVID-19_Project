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

def classification1():

    st.markdown('# Daily Cases Classification')

    final_merged_malaysia = pd.read_csv('Dataset/final_merged_malaysia.csv')

    X_RFE_cases = final_merged_malaysia.drop(columns=['cases_new', 'date']).copy()
    y_RFE_cases = final_merged_malaysia['cases_new'].copy()
    y_RFE_cases = pd.cut(y_RFE_cases, 3, labels=['Low','Medium','High'])

    strong_features_cases = ['cases_pvax',
                            'cases_adult',
                            'cases_adolescent',
                            'cases_child',
                            'cases_active',
                            'vent_port',
                            'deaths_bid_dod',
                            'hosp_covid',
                            'hosp_admitted_covid',
                            'beds_covid',
                            'pkrc_covid',
                            'cumul_partial',
                            'pkrc_discharged_total',
                            'deaths_new',
                            'cumul_full_child',
                            'cumul_partial_child',
                            'hosp_admitted_total',
                            'positivity_rate',
                            'icu_covid']
    X_RFE_cases = X_RFE_cases[strong_features_cases].copy()

    st.markdown('## Before SMOTE')

    st.write('Table below shows the number of records for each category of cases (Low, Medium, High).') 
    st.write(y_RFE_cases.value_counts())

    X_train, X_test, y_train, y_test = train_test_split(X_RFE_cases, y_RFE_cases, test_size=0.3, random_state=1)

    st.markdown('** LGBM Classifier **')

    # Confusion Matrix
    lgbm = pickle.load(open('Model/lgbm_cases_1', 'rb'))
    y_pred_lgbm  = lgbm.predict(X_test)
    st.text('Model Report:\n ' + classification_report(y_test, y_pred_lgbm))

    fig1,ax1 = plt.subplots(figsize = (20,10))
    ax1.set_title("Confusion Matrix for LGBM Classifier")
    conf_matrix_lgbm = confusion_matrix(y_test, y_pred_lgbm)
    lgbm_display = ConfusionMatrixDisplay(confusion_matrix=conf_matrix_lgbm,display_labels = lgbm.classes_)
    lgbm_display.plot(cmap = 'Greens',xticks_rotation ='vertical',ax=ax1)
    st.pyplot(fig1)
    
    st.markdown('The first plot above shows the confusion matrix for the LGBM Classifier. This classifier has high accuracy for all labels')

    rfc = pickle.load(open('Model/rfc_cases_1', 'rb'))
    y_pred_rfc = rfc.predict(X_test)
    
    st.markdown('** Random Forest Classifier **')
    st.text('Model Report:\n ' + classification_report(y_test, y_pred_rfc))

    fig2,ax2 = plt.subplots(figsize = (20,10))
    ax2.set_title("Confusion Matrix for Random Forest Classifier")
    conf_matrix_rfc = confusion_matrix(y_test, y_pred_rfc)
    rfc_display = ConfusionMatrixDisplay(confusion_matrix=conf_matrix_rfc,display_labels = rfc.classes_)
    rfc_display.plot(cmap = 'Greens',xticks_rotation ='vertical',ax=ax2)
    st.pyplot(fig2)

    st.markdown('The second plot above shows the confusion matrix for the Random Forest Classifier. This classifier has high accuracy for all three labels as well but with a wrong prediction, where the model predict a "medium" to "low". This classifier has a similar accuracy with the LGBM classifier but the performance of this classifier is slightly worse than LGBM Classifier in overall. ')












    st.markdown('## After SMOTE')
    X_resampled, y_resampled = SMOTE().fit_resample(X_RFE_cases, y_RFE_cases)

    st.write('Table below shows the number of records for each category of cases (Low, Medium, High).') 
    st.write(y_resampled.value_counts())

    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=1)

    st.markdown('** LGBM Classifier **')

    # Confusion Matrix
    lgbm = pickle.load(open('Model/lgbm_cases_2', 'rb'))
    y_pred_lgbm  = lgbm.predict(X_test)
    st.text('Model Report:\n ' + classification_report(y_test, y_pred_lgbm))

    fig1,ax1 = plt.subplots(figsize = (20,10))
    ax1.set_title("Confusion Matrix for LGBM Classifier")
    conf_matrix_lgbm = confusion_matrix(y_test, y_pred_lgbm)
    lgbm_display = ConfusionMatrixDisplay(confusion_matrix=conf_matrix_lgbm,display_labels = lgbm.classes_)
    lgbm_display.plot(cmap = 'Greens',xticks_rotation ='vertical',ax=ax1)
    st.pyplot(fig1)
    
    st.markdown('The third plot above shows the confusion matrix for the LGBM Classifier trained and tested on oversampled dataset. This classifier also has high accuracy for all three labels.')

    rfc = pickle.load(open('Model/rfc_cases_2', 'rb'))
    y_pred_rfc = rfc.predict(X_test)
    
    st.markdown('** Random Forest Classifier **')
    st.text('Model Report:\n ' + classification_report(y_test, y_pred_rfc))

    fig2,ax2 = plt.subplots(figsize = (20,10))
    ax2.set_title("Confusion Matrix for Random Forest Classifier")
    conf_matrix_rfc = confusion_matrix(y_test, y_pred_rfc)
    rfc_display = ConfusionMatrixDisplay(confusion_matrix=conf_matrix_rfc,display_labels = rfc.classes_)
    rfc_display.plot(cmap = 'Greens',xticks_rotation ='vertical',ax=ax2)
    st.pyplot(fig2)

    st.markdown('The fourth plot above shows the confusion matrix for the Random Forest Classifier trained and tested on oversampled dataset. This classifier has high accuracy for all labels as well. This classifier has the same performance with the first and second LGBM classifier and is better than the previous Random Forest Classifier. Hence, performing oversampling on this imbalance cases data does improve the performance of models in overall.')
