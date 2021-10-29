 
import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt 

def tests_my():  
    raw_tests = pd.read_csv('Dataset/tests_malaysia.csv')

    month = {'2020-03-31 00:00:00':'March', '2020-04-30 00:00:00':'April','2020-05-31 00:00:00':'May','2020-06-30 00:00:00':'June','2020-07-31 00:00:00':'July','2020-08-31 00:00:00':'August','2020-09-30 00:00:00':'September','2020-10-31 00:00:00':'October','2020-11-30 00:00:00':'November','2020-12-31 00:00:00':'December',
            '2021-01-31 00:00:00':'January','2021-02-28 00:00:00':'February','2021-03-31 00:00:00':'March','2021-04-30 00:00:00':'April','2021-05-31 00:00:00':'May','2021-06-30 00:00:00':'June','2021-07-31 00:00:00':'July','2021-08-31 00:00:00':'August','2021-09-30 00:00:00':'September',}

    m_state = {'Johor','Kedah','Kelantan','Melaka','Negeri Sembilan','Pahang','Pulau Pinang','Perak','Perlis','Selangor','Terengganu','Sabah','Sarawak','W.P. Kuala Lumpur','W.P. Labuan','W.P. Putrajaya'}
    raw_tests['total_tests'] = raw_tests['rtk-ag'] + raw_tests['pcr']
    raw_tests['date']= pd.to_datetime(raw_tests['date'])
    final_tests = raw_tests.copy()

    group_tests = final_tests.groupby([pd.Grouper(key='date', axis=0, freq='M')]).agg('sum')
    tests_month = final_tests.groupby(pd.Grouper(key='date', axis=0, freq='M')).sum()
    maxMonth = str(tests_month['total_tests'].idxmax())

    selectShow = st.selectbox("Select an aspect to show", ['Outliers Detection','Data Analysis'])

    if selectShow == 'Outliers Detection': 
        left_column, right_column = st.columns(2)
        with left_column:
            boxplot1 = alt.Chart(final_tests).mark_boxplot().encode(
                y='rtk-ag:Q'
            ).properties(
                        width=250,
                        height=200,
                        title='rtk-ag'
                    )

            st.altair_chart(boxplot1)

        with right_column:
            boxplot2 = alt.Chart(final_tests).mark_boxplot().encode(
                y='pcr:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='pcr'
                    )

            st.altair_chart(boxplot2)
        
        left_column1, right_column1 = st.columns(2)
        with left_column1:
            boxplot3 = alt.Chart(final_tests).mark_boxplot().encode(
                y='total_tests:Q'
            ).properties(
                        width=250,
                        height=200,
                        title='total_tests'
                    )

            st.altair_chart(boxplot3)
       
        st.markdown('From the boxplots above, we can see that there are quite a lot of outliers in both rtk-ag and pcr. This is because the distribution of the number of tests done in each state is not normal. Some states with more populations will conduct more tests while states with less population like Perlis conduct only a few tests in each month. Therefore, some states with extremely less tests and more tests will be treated as outliers. However, we did not remove these outliers as the nation level data are not used in this assignment and training model.')
    else:
        selectGroupBy = st.selectbox("View By", ['Day','Month'])

        if selectGroupBy == 'Day':
            chart = alt.Chart(final_tests).mark_line().encode(
                alt.X('date', type='temporal'),
                alt.Y('total_tests', type='quantitative'),
            ).properties(
                width=1200,
                height=800,
                title='Total tests of Malaysia by Day'
            )

            id = final_tests['total_tests'].idxmax()
            day = final_tests.loc[id].date
            st.altair_chart(chart)
            st.markdown("The total tests of Malaysia is " + str(final_tests['total_tests'].sum()))
            st.markdown("The mean tests of Malaysia is " + str(final_tests['total_tests'].mean()))
            st.markdown("The day with the most tests is " + str(day) + ' at ' + str(final_tests['total_tests'].max()))
        else:
            group_tests = group_tests.reset_index()
            monthChart = alt.Chart(group_tests).mark_line().encode(
                alt.X('date', type='temporal'),
                alt.Y('total_tests', type='quantitative'),
            ).properties(
                width=1200,
                height=800,
                title='Total tests of Malaysia by Month'
            )

            st.altair_chart(monthChart)
            st.markdown("The total tests of Malaysia is " + str(final_tests['total_tests'].sum()))
            st.markdown("The mean tests of Malaysia is " + str(final_tests['total_tests'].mean()))
            st.markdown("The month with the most tests is " + month[maxMonth] + ' at ' + str(tests_month['total_tests'].max()))