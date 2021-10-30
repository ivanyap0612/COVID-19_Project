import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt 

def death_my():
    death_my = pd.read_csv('Dataset/deaths_malaysia.csv')

    month = {'2020-03-31 00:00:00':'March', '2020-04-30 00:00:00':'April','2020-05-31 00:00:00':'May','2020-06-30 00:00:00':'June','2020-07-31 00:00:00':'July','2020-08-31 00:00:00':'August','2020-09-30 00:00:00':'September','2020-10-31 00:00:00':'October','2020-11-30 00:00:00':'November','2020-12-31 00:00:00':'December',
            '2021-01-31 00:00:00':'January','2021-02-28 00:00:00':'February','2021-03-31 00:00:00':'March','2021-04-30 00:00:00':'April','2021-05-31 00:00:00':'May','2021-06-30 00:00:00':'June','2021-07-31 00:00:00':'July','2021-08-31 00:00:00':'August','2021-09-30 00:00:00':'September',}

    death_my['date']= pd.to_datetime(death_my['date'])

    selectShow = st.selectbox("Select an aspect to show", ['Outliers Detection','Data Analysis'])

    if selectShow == 'Outliers Detection': 
        left_column, right_column = st.columns(2)
        with left_column:
            boxplot1 = alt.Chart(death_my).mark_boxplot().encode(
                y='deaths_new:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='deaths_new'
                    )

            st.altair_chart(boxplot1)

        with right_column:
            boxplot2 = alt.Chart(death_my).mark_boxplot().encode(
                y='deaths_new_dod:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='deaths_new_dod'
                    )

            st.altair_chart(boxplot2)

        left_column1, right_column1 = st.columns(2)
        with left_column1:
            boxplot3 = alt.Chart(death_my).mark_boxplot().encode(
                y='deaths_bid:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='deaths_bid'
                    )

            st.altair_chart(boxplot3)

        with right_column1:
            boxplot4 = alt.Chart(death_my).mark_boxplot().encode(
                y='deaths_bid_dod:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='deaths_bid_dod'
                    )

            st.altair_chart(boxplot4)
        
        left_column2, right_column2 = st.columns(2)
        with left_column2:
            boxplot5 = alt.Chart(death_my).mark_boxplot().encode(
                y='deaths_pvax:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='deaths_pvax'
                    )

            st.altair_chart(boxplot5)

        with right_column2:
            boxplot6 = alt.Chart(death_my).mark_boxplot().encode(
                y='deaths_fvax:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='deaths_fvax'
                    )

            st.altair_chart(boxplot6)
        
        left_column3, right_column3 = st.columns(2)
        with left_column3:
            boxplot7 = alt.Chart(death_my).mark_boxplot().encode(
                y='deaths_tat:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='deaths_tat'
                    )

            st.altair_chart(boxplot7)

        st.markdown('From the boxplots, above, we can see that deaths_new, deaths_new_dod, deaths_bid and deaths_bid_dod contain many outliers. This is due to the fact that at the early stage of COVID-19 has very less death occurs. The death surge after several waves of COVID-19 attacked Malaysia. We decided to not remove the outliers as they are very crucial to the assignment and training model.')
    
    else:
        selectGroupBy = st.selectbox("View By", ['Day','Month'])

        if selectGroupBy == 'Day':
            chart = alt.Chart(death_my).mark_line().encode(
                alt.X('date', type='temporal'),
                alt.Y('deaths_new', type='quantitative'),
            ).properties(
                width=1200,
                height=800,
                title='Total Deaths By Day'
            )

            id = death_my['deaths_new'].idxmax()
            day = death_my.loc[id].date
            st.altair_chart(chart)
            st.markdown("The total number of deaths is " + str(death_my['deaths_new'].sum()))
            st.markdown("The mean number of deaths is " + str(death_my['deaths_new'].mean()))
            st.markdown("The day with the most number of deaths is " + str(day) +' at ' + str(death_my['deaths_new'].max()))
        else:
            death_month = death_my.groupby(pd.Grouper(key='date', axis=0, freq='M')).sum()
            maxMonth = str(death_month['deaths_new'].idxmax())
            vax_month = death_month.reset_index()
            monthChart = alt.Chart(vax_month).mark_line().encode(
                alt.X('date', type='temporal'),
                alt.Y('deaths_new', type='quantitative'),
            ).properties(
                width=1200,
                height=800,
                title='Total Number of Death Every Month'
            )

            st.altair_chart(monthChart)
            st.markdown("The total number of deaths is " + str(death_my['deaths_new'].sum()))
            st.markdown("The mean number of deaths is " + str(death_my['deaths_new'].mean()))
            st.markdown("The month with the most number of deaths is " + month[maxMonth] + ' at ' + str(death_month['deaths_new'].max()))