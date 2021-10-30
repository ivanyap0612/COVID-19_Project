import streamlit as st 
import numpy as np
import pandas as pd
import statsmodels
import pickle
import matplotlib.pyplot as plt
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.arima_model import ARMAResults 
from statsmodels.tsa.stattools import acf
import fbprophet
import plotly.graph_objects as go
from datetime import date
import datetime

def regression1():
    vax_my = pd.read_csv('Dataset/vax_malaysia.csv')
    vax_my['date']= pd.to_datetime(vax_my['date'])
    pop_ori = pd.read_csv('Dataset/population.csv')
    pop = pop_ori.drop(0).copy()
    reg_q1 = vax_my[['date','daily_full']].copy()
    reg_q1 = reg_q1.set_index('date')
    df_log = np.log(reg_q1)
    df_log = df_log.replace(-np.inf, np.nan)
    df_log = df_log.replace(np.inf, np.nan)
    df_log = df_log.dropna()
    train_regq1 = df_log[:(len(reg_q1)-30)].copy()
    test_regq1 = df_log[(len(reg_q1)-30):].copy()

    selectModel = st.selectbox("Select a model to view", ['Autoregressive integrated moving average(ARIMA)','FBProphet'])

    if selectModel == 'Autoregressive integrated moving average(ARIMA)':
        model_arima_regq1 = pickle.load(open('Model/arima_cases_q1', 'rb'))
        regq1_fc, regq1_conf = model_arima_regq1.predict(25, return_conf_int=True)  # 95% conf

        st.markdown('********Out-of-Time cross-validation********')
        st.markdown('In Out-of-Time cross-validation, few steps back in time and forecast into the future to as many steps you took back. Then you compare the forecast against the actuals.')

        # Make as pandas series
        regq1_fc_series = pd.Series(regq1_fc, index=test_regq1.index)
        regq1_lower_series = pd.Series(regq1_conf[:, 0], index=test_regq1.index)
        regq1_upper_series = pd.Series(regq1_conf[:, 1], index=test_regq1.index)

        # Plot
        plt.figure(figsize=(12,5), dpi=100)
        plt.plot(train_regq1, label='training')
        plt.plot(test_regq1, label='actual')
        plt.plot(regq1_fc_series, label='forecast')
        plt.fill_between(regq1_lower_series.index, regq1_lower_series, regq1_upper_series, 
                        color='k', alpha=.15)
        plt.title('Forecast vs Actuals')
        plt.legend(loc='upper left', fontsize=10)
        st.pyplot(plt)

        def forecast_accuracy(forecast, actual):
            mape = np.mean(np.abs(forecast - actual)/np.abs(actual))  # MAPE
            me = np.mean(forecast - actual)             # ME
            mae = np.mean(np.abs(forecast - actual))    # MAE
            mpe = np.mean((forecast - actual)/actual)   # MPE
            rmse = np.mean((forecast - actual)**2)**.5  # RMSE
            corr = np.corrcoef(forecast, actual)[0,1]   # corr
            mins = np.amin(np.hstack([forecast[:,None], 
                                    actual[:,None]]), axis=1)
            maxs = np.amax(np.hstack([forecast[:,None], 
                                    actual[:,None]]), axis=1)
            minmax = 1 - np.mean(mins/maxs)             # minmax
            acf1 = acf(regq1_fc-test_regq1['daily_full'])[1]   # ACF1
            return (mape,me,mae,mpe,rmse,corr,minmax,acf1)

        (mape,me,mae,mpe,rmse,corr,minmax,acf1) = forecast_accuracy(regq1_fc, test_regq1['daily_full'].values)

        st.text("")
        st.markdown('********ARIMA Evaluation Metrics Score********')
        st.markdown('Evaluation Metrics: \n- Mean Absolute Percentage Error (MAPE)\n- Mean Error (ME)\n- Mean Absolute Error (MAE)\n- Mean Percentage Error (MPE)\n- Root Mean Squared Error (RMSE)\n- Lag 1 Autocorrelation of Error (ACF1)\n- Correlation between the Actual and the Forecast (corr)\n- Min-Max Error (minmax)')
        table1 = go.Figure(data=[go.Table(
        columnwidth=[1, 4],
        header=dict(values=['Metrics', 'Value'],
                    fill=dict(color=['paleturquoise']),
                    align='center',height=30),
        cells=dict(values=[['MAPE','ME','MAE','MPE','RMSE','corr','minmax','ACF1'],
                        [str(mape),str(me), str(mae), str(mpe), str(rmse), str(corr), str(minmax), str(acf1)]],
                fill=dict(color=['lightcyan']),
                align='center',height=30))
        ])
        table1 = table1.update_layout(width=400,height=200, margin=dict(l=0,r=10,t=5,b=0))
        st.write(table1)

        lastday = date(2021,10,25)
        vac_80 = date(2021,11,30)
        daysbetween = vac_80 - lastday

        regq1_forecast = model_arima_regq1.predict(n_periods=25+daysbetween.days)
        regq1_forecast = regq1_forecast[25:]
        my_pop = pop_ori[pop_ori['state'] == 'Malaysia']
        my_pop = my_pop['pop']

        results = np.exp(regq1_forecast)
        x = 0
        for i in results:
            x = x + i
        cumul = vax_my.loc[len(vax_my)-1].cumul_full
        cumul = cumul +x
        herd = (cumul/my_pop[0])*100

        results = pd.Series(results)

        dailyfull = vax_my['daily_full'].copy()
        dailyfull = dailyfull.append(results)
        dailyfull= dailyfull.reset_index()
        dailyfull['cumul'] = dailyfull[0].cumsum()

        percentage_vac = (dailyfull['cumul'] / my_pop[0])*100
        percentage_vac = percentage_vac.to_frame()

        st.text("")
        st.markdown('********Forecasting for the Total Percentage of People Who Receive Full Dose of Vaccine********')
        plt.figure(figsize=(15,10))
        plt.plot(percentage_vac[:len(reg_q1)])
        plt.plot(percentage_vac[len(reg_q1):], color='green',label='Forecast')
        plt.axhline(y=80, color='r', linestyle='-')
        plt.ylim(0,100)
        plt.legend(loc='upper left', fontsize=15)
        plt.title("Cumulative Forecast for the Total Percentage of People Who Receive Full Dose of Vaccine")
        st.pyplot(plt)

        st.markdown('Herd Imunity is not archived at 78.20 %')
    else:
        df_prophet_q1 = vax_my[['date','daily_full']].copy()
        df_prophet_q1.columns = ['ds', 'y']
        df_prophet_q1['ds']= pd.to_datetime(df_prophet_q1['ds'])
        model_prop_q1 = pickle.load(open('Model/prophet_cases_q1', 'rb'))

        train_regq1_2 = df_prophet_q1[:214].copy()
        test_regq1_2 = df_prophet_q1[214:].copy()
        
        test_dates_q1 = model_prop_q1.make_future_dataframe(periods=30)
        test_prediction = model_prop_q1.predict(test_dates_q1)
        test_yhat = test_prediction['yhat']
        test_yhat = test_yhat[214:]

        def forecast_accuracy(forecast, actual):
            mape = np.mean(np.abs(forecast - actual)/np.abs(actual))  # MAPE
            me = np.mean(forecast - actual)             # ME
            mae = np.mean(np.abs(forecast - actual))    # MAE
            mpe = np.mean((forecast - actual)/actual)   # MPE
            rmse = np.mean((forecast - actual)**2)**.5  # RMSE
            corr = np.corrcoef(forecast, actual)[0,1]   # corr
            mins = np.amin(np.hstack([forecast[:,None], 
                                    actual[:,None]]), axis=1)
            maxs = np.amax(np.hstack([forecast[:,None], 
                                    actual[:,None]]), axis=1)
            minmax = 1 - np.mean(mins/maxs)             # minmax
            acf1 = acf(test_yhat-test_regq1_2['y'])[1]   # ACF1
            return (mape,me,mae,mpe,rmse,corr,minmax,acf1)
        
        (mape,me,mae,mpe,rmse,corr,minmax,acf1) = forecast_accuracy(test_yhat, test_regq1_2['y'].values)

        lastday = date(2021,10,25)
        vac_80 = date(2021,11,30)
        daysbetween = vac_80 - lastday
        future_dates_q1 = model_prop_q1.make_future_dataframe(periods=30+daysbetween.days)

        st.markdown('------FBProphet------')
        prediction_prophet = model_prop_q1.predict(future_dates_q1)
        model_prop_q1.plot(prediction_prophet)
        st.pyplot(plt)

        st.text("")
        st.markdown('********FBProphet Evaluation Metrics Score********')
        st.markdown('Evaluation Metrics: \n- Mean Absolute Percentage Error (MAPE)\n- Mean Error (ME)\n- Mean Absolute Error (MAE)\n- Mean Percentage Error (MPE)\n- Root Mean Squared Error (RMSE)\n- Lag 1 Autocorrelation of Error (ACF1)\n- Correlation between the Actual and the Forecast (corr)\n- Min-Max Error (minmax)')
        table1 = go.Figure(data=[go.Table(
        columnwidth=[1, 4],
        header=dict(values=['Metrics', 'Value'],
                    fill=dict(color=['paleturquoise']),
                    align='center',height=30),
        cells=dict(values=[['MAPE','ME','MAE','MPE','RMSE','corr','minmax','ACF1'],
                        [str(mape),str(me), str(mae), str(mpe), str(rmse), str(corr), str(minmax), str(acf1)]],
                fill=dict(color=['lightcyan']),
                align='center',height=30))
        ])
        table1 = table1.update_layout(width=400,height=200, margin=dict(l=0,r=10,t=5,b=0))
        st.write(table1)

        vac_80_q2 = prediction_prophet[prediction_prophet['ds'] > '2021-10-25'].yhat
        my_pop = pop_ori[pop_ori['state'] == 'Malaysia']
        my_pop = my_pop['pop']
        x = 0
        for i in vac_80_q2:
            x = x + i
        cumul = vax_my.loc[len(vax_my)-1].cumul_full
        cumul = cumul +x
        herd = (cumul/my_pop[0])*100

        dailyfull2 = vax_my['daily_full'].copy()
        dailyfull2 = dailyfull2.append(vac_80_q2)
        dailyfull2 = dailyfull2.to_frame()
        dailyfull2['cumul'] = dailyfull2[0].cumsum()

        percentage_vac2 = (dailyfull2['cumul'] / my_pop[0])*100
        percentage_vac2 = percentage_vac2.to_frame()

        st.text("")
        st.markdown('********Forecasting for the Total Percentage of People Who Receive Full Dose of Vaccine********')
        plt.figure(figsize=(15,10))
        plt.plot(percentage_vac2[:len(reg_q1)])
        plt.plot(percentage_vac2[len(reg_q1):], color='green',label='Forecast')
        plt.axhline(y=80, color='r', linestyle='-')
        plt.ylim(0,100)
        plt.legend(loc='upper left', fontsize=15)
        plt.title("Cumulative Forecast for the Total Percentage of People Who Receive Full Dose of Vaccine")
        st.pyplot(plt)

        st.markdown('Herd Imunity is archived at 88.23 %s')




