import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt 

def icu():  
    icu = pd.read_csv('Dataset/icu.csv')

    icu['date']= pd.to_datetime(icu['date'])

    state_icu = icu.groupby(['state']).sum()

    month = {'2020-03-31 00:00:00':'March', '2020-04-30 00:00:00':'April','2020-05-31 00:00:00':'May','2020-06-30 00:00:00':'June','2020-07-31 00:00:00':'July','2020-08-31 00:00:00':'August','2020-09-30 00:00:00':'September','2020-10-31 00:00:00':'October','2020-11-30 00:00:00':'November','2020-12-31 00:00:00':'December',
            '2021-01-31 00:00:00':'January','2021-02-28 00:00:00':'February','2021-03-31 00:00:00':'March','2021-04-30 00:00:00':'April','2021-05-31 00:00:00':'May','2021-06-30 00:00:00':'June','2021-07-31 00:00:00':'July','2021-08-31 00:00:00':'August','2021-09-30 00:00:00':'September',}
    month_icu = icu.groupby([pd.Grouper(key='date', axis=0, freq='M'),"state"]).agg('sum')
    m_icu = icu.groupby(pd.Grouper(key='date', axis=0, freq='M')).sum()
    maxMonth1 = str(m_icu['icu_covid'].idxmax())
    maxMonth2 = str(m_icu['beds_icu_covid'].idxmax())

    selectShow = st.selectbox("Select an aspect to show", ['Outliers Detection','Data Analysis'])

    if selectShow == 'Outliers Detection': 
        c1,c2= st.columns(2)
        with c1:
            boxplot1 = alt.Chart(icu).mark_boxplot().encode(
                y='beds_icu:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Gazetted ICU beds'
                    )

            st.altair_chart(boxplot1)

        with c2:
            boxplot2 = alt.Chart(icu).mark_boxplot().encode(
                y='beds_icu_rep:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='beds_icu_rep'
                    )

            st.altair_chart(boxplot2)
        
        c3,c4= st.columns(2)
        with c3:
            boxplot3 = alt.Chart(icu).mark_boxplot().encode(
                y='beds_icu_total:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Critical Care Beds Available'
                    )

            st.altair_chart(boxplot3)

        with c4:
            boxplot4 = alt.Chart(icu).mark_boxplot().encode(
                y='beds_icu_covid:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Critical Care Beds Dedicated for COVID-19'
                    )

            st.altair_chart(boxplot4)
        
        c5,c6= st.columns(2)
        with c5:
            boxplot5 = alt.Chart(icu).mark_boxplot().encode(
                y='vent'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Available Ventilators'
                    )

            st.altair_chart(boxplot5)

        with c6:
            boxplot6 = alt.Chart(icu).mark_boxplot().encode(
                y='vent_port:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Available Portable Ventilators'
                    )

            st.altair_chart(boxplot6)
        
        c7,c8= st.columns(2)
        with c7:
            boxplot7 = alt.Chart(icu).mark_boxplot().encode(
                y='icu_covid:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Number of COVID-19 Patients under Intensive Care'
                    )

            st.altair_chart(boxplot7)

        with c8:
            boxplot8 = alt.Chart(icu).mark_boxplot().encode(
                y='icu_pui:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Number of Individuals(PUI) under Intensive Care'
                    )

            st.altair_chart(boxplot8)
        
        c9,c10= st.columns(2)
        with c9:
            boxplot9 = alt.Chart(icu).mark_boxplot().encode(
                y='icu_noncovid:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Number of Non-COVID-19 Patients under Intensive Care'
                    )

            st.altair_chart(boxplot9)

        with c10:
            boxplot10 = alt.Chart(icu).mark_boxplot().encode(
                y='vent_covid:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Number of COVID-19 Patients in icus'
                    )

            st.altair_chart(boxplot10)
        
        c11,c12= st.columns(2)
        with c11:
            boxplot11 = alt.Chart(icu).mark_boxplot().encode(
                y='vent_pui:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Number of Individuals in Category PUI on Mechanical Ventilation'
                    )

            st.altair_chart(boxplot11)

        with c12:
            boxplot12 = alt.Chart(icu).mark_boxplot().encode(
                y='vent_noncovid:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Number of Non-COVID-19 Patients on Mechanical Ventilation'
                    )

            st.altair_chart(boxplot12)
        
        c13,c14= st.columns(2)
        with c13:
            boxplot13 = alt.Chart(icu).mark_boxplot().encode(
                y='vent_pui:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Used Ventilators'
                    )

            st.altair_chart(boxplot13)

        with c14:
            boxplot14 = alt.Chart(icu).mark_boxplot().encode(
                y='vent_port_used:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='Total Used Portable Ventilators'
                    )

            st.altair_chart(boxplot14)
        st.markdown('Based on the boxplots above, we can see that every column in the icu.csv dataset contains a lot of outliers. All of the boxplots showed that the data is positively skewed. This may be due to the slow start of the COVID-19 pandemic which contains a low number of COVID-19 cases, followed by a sudden increase of high number COVID-19 cases that caused a high number of patients admitted to the ICU. However, we decided to not remove these outliers as the data are crucial to this assignment and training model.')
        
    else:
        left_column2, right_column2 = st.columns(2)
        with left_column2:
            selectGroupBy = st.selectbox("View By", ['Day','Month'])

        with right_column2:
            selectState = st.selectbox("Select a state to view", ['All','Johor','Kedah','Kelantan','Melaka','Negeri Sembilan','Pahang','Pulau Pinang','Perak','Perlis','Selangor','Terengganu','Sabah','Sarawak','W.P. Kuala Lumpur','W.P. Labuan','W.P. Putrajaya'])

        if selectGroupBy == 'Day':
            if selectState == 'All':
                dayAllAChart = alt.Chart(icu).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('icu_covid', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=800,
                    height=600,
                    title='Total Number of COVID-19 Patient under Intensive Care by Day'
                )
               
                id = icu['icu_covid'].idxmax()
                day = icu.loc[id].date
                state = icu.loc[id].state
                st.altair_chart(dayAllAChart)
                st.markdown("The total number of COVID-19 patient under Intensive Care of Malaysia is " + str(state_icu['icu_covid'].sum()))
                st.markdown("The mean number of COVID-19 patient under Intensive Care of Malaysia is " + str(state_icu['icu_covid'].mean()))
                st.markdown("The state with the most number of COVID-19 patient under Intensive Care is " + str(state_icu['icu_covid'].idxmax()) + ' at ' + str(state_icu['icu_covid'].max()))
                st.markdown("The day with the most number of COVID-19 patient under Intensive Care is " + str(day) + ' in ' + state +' at ' + str(icu['icu_covid'].max()))

                dayAllDChart = alt.Chart(icu).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('beds_icu_covid', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=800,
                    height=600,
                    title='Total Critical Care Beds Dedicated for COVID-19 '
                )
               
                id_dAll = icu['beds_icu_covid'].idxmax()
                day_dAll = icu.loc[id_dAll].date
                state_dAll = icu.loc[id_dAll].state
                st.altair_chart(dayAllDChart)
                st.markdown("The total critical care beds dedicated for COVID-19 of Malaysia is " + str(state_icu['beds_icu_covid'].sum()))
                st.markdown("The mean critical care beds dedicated for COVID-19 of Malaysia is " + str(state_icu['beds_icu_covid'].mean()))
                st.markdown("The state with the most critical care beds dedicated for COVID-19 is " + str(state_icu['beds_icu_covid'].idxmax()) + ' at ' + str(state_icu['beds_icu_covid'].max()))
                st.markdown("The day with the most critical care beds dedicated for COVID-19 is " + str(day_dAll) + ' in ' + state_dAll +' at ' + str(icu['beds_icu_covid'].max()))
                st.markdown('Based on the line graphs above,  the graph on the top showed that Selangor recorded the highest number of COVID-19 patients under iIntensive care for every month while the graph on the bottom showed that Selangor recorded the highest total number of critical care beds dedicated for COVID-19 in the ICU. The total number of COVID-19 patients under intensive care for every month was low at the early stages but the total number of COVID-19 patients rocketed rapidly starting from May 2021 to around September 2021,especially Selangor.')
                st.markdown('One of the important insights that can be obtained from this chart is that the total critical care beds in the icu are still sufficient for the COVID-19 patients, even though the number of COVID-19 cases are getting higher as the total number of critical care beds dedicated for COVID-19 is always higher than the total number of patients for every month. ')         
            else:
                state_day_total1 = icu[icu['state'] == selectState]
                state_day_chart1 = alt.Chart(state_day_total1).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('icu_covid', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=800,
                    height=600,
                    title='Total Number of COVID-19 Patient under Intensive Care for ' + selectState + ' by Day'
                )
                day_ad_all = state_day_total1['icu_covid'].idxmax()
                day_ad_all = state_day_total1.loc[day_ad_all].date

                st.altair_chart(state_day_chart1)
                st.markdown("Total Number of COVID-19 patient under Intensive Care for " + selectState + ' is ' + str(state_day_total1['icu_covid'].sum()))        
                st.markdown("The mean total number of COVID-19 patient under Intensive Care for " + selectState + ' is ' + str(state_day_total1['icu_covid'].mean()))     
                st.markdown("The day with the most number of COVID-19 patient under Intensive Care for " + str(day_ad_all) + ' at ' + str(state_day_total1['icu_covid'].max()))

                state_day_total2 = icu[icu['state'] == selectState]
                state_day_chart2 = alt.Chart(state_day_total2).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('beds_icu_covid', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=800,
                    height=600,
                    title='Total Critical Care Beds Dedicated for COVID-19 for ' + selectState + ' by Day'
                )
                day_dc_all = state_day_total1['beds_icu_covid'].idxmax()
                day_dc_all = state_day_total1.loc[day_dc_all].date

                st.altair_chart(state_day_chart2)
                st.markdown("The total critical care beds dedicated for COVID-19 in " + selectState + ' is ' + str(state_day_total2['beds_icu_covid'].sum()))        
                st.markdown("The mean number of critical care beds dedicated for COVID-19 for " + selectState + ' is ' + str(state_day_total2['beds_icu_covid'].mean()))     
                st.markdown("The day with the most critical care beds dedicated for COVID-19 is " + str(day_dc_all) + ' at ' + str(state_day_total2['beds_icu_covid'].max()))
                st.markdown('Based on the line graphs above,  the graph on the top showed that Selangor recorded the highest number of COVID-19 patients under iIntensive care for every month while the graph on the bottom showed that Selangor recorded the highest total number of critical care beds dedicated for COVID-19 in the ICU. The total number of COVID-19 patients under intensive care for every month was low at the early stages but the total number of COVID-19 patients rocketed rapidly starting from May 2021 to around September 2021,especially Selangor.')
                st.markdown('One of the important insights that can be obtained from this chart is that the total critical care beds in the icu are still sufficient for the COVID-19 patients, even though the number of COVID-19 cases are getting higher as the total number of critical care beds dedicated for COVID-19 is always higher than the total number of patients for every month. ')         
        else:
            if selectState == 'All':
                month_icu = month_icu.reset_index()
                monthChart1 = alt.Chart(month_icu).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('icu_covid', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=800,
                    height=600,
                    title='Total Number of COVID-19 Patient under Intensive Care for every Month'
                )
                
                st.altair_chart(monthChart1)
                st.markdown("The total number of COVID-19 patient under Intensive Care of Malaysia is " + str(state_icu['icu_covid'].sum()))
                st.markdown("The mean number of COVID-19 patient under Intensive Care of Malaysia is " + str(state_icu['icu_covid'].mean()))
                st.markdown("The state with the most number of COVID-19 patient under Intensive Care is " + str(state_icu['icu_covid'].idxmax()) + ' at ' + str(state_icu['icu_covid'].max()))
                st.markdown("The month with the most number of COVID-19 patient under Intensive Care is " +  month[maxMonth1] + ' at ' + str(m_icu['icu_covid'].max()))

                monthChart2 = alt.Chart(month_icu).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('beds_icu_covid', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=800,
                    height=600,
                    title='Total Critical Care Beds Dedicated for COVID-19 for every Month'
                )
                
                st.altair_chart(monthChart2)
                st.markdown("The total critical care beds dedicated for COVID-19 of Malaysia is " + str(state_icu['beds_icu_covid'].sum()))
                st.markdown("The mean number of total critical care beds dedicated for COVID-19 for every Monthof Malaysia is " + str(state_icu['beds_icu_covid'].mean()))
                st.markdown("The state with the most number of critical care beds dedicated for COVID-19 is " + str(state_icu['beds_icu_covid'].idxmax()) + ' at ' + str(state_icu['beds_icu_covid'].max()))
                st.markdown("The month with the most number of critical care beds dedicated for COVID-19(from 2020-2021) is " +  month[maxMonth2] + ' at ' + str(m_icu['beds_icu_covid'].max()))
                st.markdown('Based on the line graphs above,  the graph on the top showed that Selangor recorded the highest number of COVID-19 patients under iIntensive care for every month while the graph on the bottom showed that Selangor recorded the highest total number of critical care beds dedicated for COVID-19 in the ICU. The total number of COVID-19 patients under intensive care for every month was low at the early stages but the total number of COVID-19 patients rocketed rapidly starting from May 2021 to around September 2021,especially Selangor.')
                st.markdown('One of the important insights that can be obtained from this chart is that the total critical care beds in the icu are still sufficient for the COVID-19 patients, even though the number of COVID-19 cases are getting higher as the total number of critical care beds dedicated for COVID-19 is always higher than the total number of patients for every month. ')         
            else:
                month_icu = month_icu.reset_index()
                state_month_total1 = month_icu[month_icu['state'] == selectState]
                stateMonthChart1 = alt.Chart(state_month_total1).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('icu_covid', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=800,
                    height=600,
                    title='Total Number of COVID-19 Patient under Intensive Care for' + selectState + ' by Month'            
                )
                st.altair_chart(stateMonthChart1)
                st.markdown("The total number of COVID-19 patient under Intensive Care for " + selectState + ' is ' + str(state_month_total1['icu_covid'].sum()))        
                st.markdown("The mean number of COVID-19 patient under Intensive Care for " + selectState + ' is ' + str(state_month_total1['icu_covid'].mean()))     
                st.markdown("The highest number of COVID-19 patient under Intensive Care for " + selectState + ' is ' + str(state_month_total1['icu_covid'].max()))

                state_month_total2 = month_icu[month_icu['state'] == selectState]
                stateMonthChart2 = alt.Chart(state_month_total2).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('beds_icu_covid', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=800,
                    height=600,
                    title='Total Critical Care Beds Dedicated for COVID-19 in' + selectState + ' by Month'            
                )
                st.altair_chart(stateMonthChart2)
                st.markdown("The total critical care beds dedicated for COVID-19 for " + selectState + ' is ' + str(state_month_total2['beds_icu_covid'].sum()))        
                st.markdown("The mean number of critical care beds dedicated for COVID-19 for " + selectState + ' is ' + str(state_month_total2['beds_icu_covid'].mean()))     
                st.markdown("The highest number of critical care beds dedicated for COVID-19 for " + selectState + ' is ' + str(state_month_total2['beds_icu_covid'].max()))
                st.markdown('Based on the line graphs above,  the graph on the top showed that Selangor recorded the highest number of COVID-19 patients under iIntensive care for every month while the graph on the bottom showed that Selangor recorded the highest total number of critical care beds dedicated for COVID-19 in the ICU. The total number of COVID-19 patients under intensive care for every month was low at the early stages but the total number of COVID-19 patients rocketed rapidly starting from May 2021 to around September 2021,especially Selangor.')
                st.markdown('One of the important insights that can be obtained from this chart is that the total critical care beds in the icu are still sufficient for the COVID-19 patients, even though the number of COVID-19 cases are getting higher as the total number of critical care beds dedicated for COVID-19 is always higher than the total number of patients for every month. ')         