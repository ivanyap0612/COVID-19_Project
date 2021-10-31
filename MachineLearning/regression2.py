import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt 
import itertools
import statsmodels
import pickle
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose 
from statsmodels.tools.eval_measures import rmse
from statsmodels.tsa.stattools import adfuller
from pandas.plotting import autocorrelation_plot
from matplotlib import pyplot
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.arima_model import ARMAResults 
from statsmodels.tsa.stattools import acf
import fbprophet
from scipy.stats import boxcox
from scipy.special import inv_boxcox
from datetime import timedelta
import plotly.graph_objects as go

def regression2():
    cases_malaysia = pd.read_csv("Dataset/cases_malaysia.csv")
    cases_malaysia['date'] = pd.to_datetime(cases_malaysia['date'])
    cases_malaysia.fillna(value = 0, inplace = True)
    filter = ['cluster_import','cluster_religious','cluster_community','cluster_highRisk','cluster_education','cluster_detentionCentre','cluster_workplace']
    cases_malaysia[filter] = cases_malaysia[filter].astype(int)
    df_cases_reg2 = cases_malaysia[['date','cases_new']]
    df_cases_reg2 = df_cases_reg2[df_cases_reg2['date'] > '2020-12-31']
    df_cases_reg2['date'] = pd.to_datetime(df_cases_reg2['date'])
    df_cases_reg2 = df_cases_reg2.set_index('date')

    selectModel = st.selectbox("Select a model to view", ['Autoregressive integrated moving average(ARIMA)','FBProphet'])
    

    if selectModel == 'Autoregressive integrated moving average(ARIMA)':
        st.markdown('------Autoregressive integrated moving average(ARIMA)------')
        df_arima_reg2 = df_cases_reg2.copy()
        train_arima_reg2 = df_arima_reg2[:293]
        test_arima_reg2 = df_arima_reg2[293:]
        #load arima model
        model_arima_reg2 = pickle.load(open('Model/arima_cases', 'rb'))
        # Forecast
        fc, conf = model_arima_reg2.predict(5, return_conf_int=True)  # 95% conf

        # Make as pandas series
        fc_series = pd.Series(fc, index=test_arima_reg2.index)
        lower_series = pd.Series(conf[:, 0], index=test_arima_reg2.index)
        upper_series = pd.Series(conf[:, 1], index=test_arima_reg2.index)
        
        st.markdown('********Out-of-Time cross-validation********')
        st.markdown('In Out-of-Time cross-validation, few steps back in time and forecast into the future to as many steps you took back. Then you compare the forecast against the actuals.')
        # Plot for Model Validation
        plt.figure(figsize=(12,5), dpi=100)
        plt.plot(train_arima_reg2, label='training')
        plt.plot(test_arima_reg2, label='actual')
        plt.plot(fc_series, label='forecast')
        plt.fill_between(lower_series.index, lower_series, upper_series, 
                        color='k', alpha=.15)
        plt.title('Forecast vs Actuals')
        plt.xlabel('Date')
        plt.ylabel('COVID-19 Cases') 
        plt.legend(loc='upper left', fontsize=10)
        st.pyplot(plt)
        plt.clf()

        #Model Evaluation Metrics
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
            acf1 = acf(fc-test_arima_reg2['cases_new'])[1]   # ACF1
            return (mape,me,mae,mpe,rmse,corr,minmax,acf1)

        (mape,me,mae,mpe,rmse,corr,minmax,acf1) = forecast_accuracy(fc, test_arima_reg2['cases_new'].values)

        ##Printing Table
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
        st.text("")
        st.markdown('********Forecasting for the Total Number of COVID-19 Cases Drop below 1000 Cases per day********')
        #Forecasting the date
        time_steps = 1
        while True:
            forecast_arr = model_arima_reg2.predict(n_periods=time_steps)
            forecast_arr_length = len(forecast_arr)
            forecast = forecast_arr[forecast_arr_length - 1]
            if(forecast < 1000):
                break
            time_steps += 1

        #Forecast
        n_periods = time_steps
        fc, confint = model_arima_reg2.predict(n_periods=n_periods, return_conf_int=True)
        index_of_fc = np.arange(len(train_arima_reg2.values), len(train_arima_reg2.values)+n_periods)

        # make series for plotting purpose
        fc_series = pd.Series(fc, index=index_of_fc)
        lower_series = pd.Series(confint[:, 0], index=index_of_fc)
        upper_series = pd.Series(confint[:, 1], index=index_of_fc)

        # Plot
        plt.figure(figsize=(12,5), dpi=100)
        plt.plot( train_arima_reg2.values)
        plt.plot(fc_series, color='darkgreen',label='Forecast')
        plt.fill_between(lower_series.index, 
                        lower_series, 
                        upper_series, 
                        color='k', alpha=.15)
        plt.legend(loc='upper left', fontsize=15)
        plt.xlabel('Date')
        plt.ylabel('COVID-19 Cases') 
        plt.title("Forecast for the Total Number of COVID-19 Cases Drop below 1000 Cases per day")
        st.pyplot(plt)

        st.markdown('The total number of COVID-19 cases will drop below 1000 cases per day on 2021-11-07.')
        st.text("")

    else:
        st.markdown('------FBProphet------')
        df_prophet_reg2 = cases_malaysia[['date','cases_new']]
        #filter for year 2021
        df_prophet_reg2 = df_prophet_reg2[df_prophet_reg2['date'] > '2020-12-31']
        # prepare expected column names
        df_prophet_reg2.columns = ['ds', 'y']
        df_prophet_reg2['ds']= pd.to_datetime(df_prophet_reg2['ds'])
        #create train and test dataset
        train_regq2_2 = df_prophet_reg2[:293].copy()
        test_regq2_2 = df_prophet_reg2[293:].copy()
        #load prophet model
        model_prophet_reg2 = pickle.load(open('Model/prophet_cases', 'rb'))
        #Test performance
        test_future_dates = model_prophet_reg2.make_future_dataframe(periods=5)
        test_forecast = model_prophet_reg2.predict(test_future_dates)
        test_yhat_q2 = test_forecast['yhat']
        test_yhat_q2 = test_yhat_q2[293:]
        
        def forecast_accuracy2(forecast, actual):
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
            acf1 = acf(test_yhat_q2-test_regq2_2['y'].values)[1]   # ACF1  
            return (mape,me,mae,mpe,rmse,corr,minmax,acf1)
            
        (mape2,me2,mae2,mpe2,rmse2,corr2,minmax2,acf1) = forecast_accuracy2(test_yhat_q2, test_regq2_2['y'].values)
      
        ##Printing Table
        st.text("")
        st.markdown('********FBProphet Evaluation Metrics Score********')
        st.markdown('Evaluation Metrics: \n- Mean Absolute Percentage Error (MAPE)\n- Mean Error (ME)\n- Mean Absolute Error (MAE)\n- Mean Percentage Error (MPE)\n- Root Mean Squared Error (RMSE)\n- Lag 1 Autocorrelation of Error (ACF1)\n- Correlation between the Actual and the Forecast (corr)\n- Min-Max Error (minmax)')
        table2 = go.Figure(data=[go.Table(
        columnwidth=[1, 4],
        header=dict(values=['Metrics', 'Value'],
                    fill=dict(color=['paleturquoise']),
                    align='center',height=30),
        cells=dict(values=[['MAPE','ME','MAE','MPE','RMSE','corr','minmax','ACF1'],
                        [str(mape2),str(me2), str(mae2), str(mpe2), str(rmse2), str(corr2), str(minmax2), str(acf1)]],
                fill=dict(color=['lightcyan']),
                align='center',height=30))
        ])
        table2 = table2.update_layout(width=400,height=200, margin=dict(l=0,r=10,t=5,b=0))
        st.write(table2)
        st.text("")
        st.markdown('********Forecasting for the Total Number of COVID-19 Cases Drop below 1000 Cases per day********')

        future_dates = model_prophet_reg2.make_future_dataframe(periods=365)
        forecast = model_prophet_reg2.predict(future_dates)
        model_prophet_reg2.plot(forecast)
        plt.ylim(0,30000)
        st.pyplot(plt)
        below_1000 = (forecast['yhat']<1000) & (forecast['ds']>'2021-10-20')
        st.markdown('The total number of COVID-19 cases drop below 1000 cases per day on 2021-11-14')