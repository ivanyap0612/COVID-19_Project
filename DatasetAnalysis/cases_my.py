 
import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt 

def cases_my():  
    raw_cases = pd.read_csv('Dataset/cases_malaysia.csv')

    month = {'2020-03-31 00:00:00':'March', '2020-04-30 00:00:00':'April','2020-05-31 00:00:00':'May','2020-06-30 00:00:00':'June','2020-07-31 00:00:00':'July','2020-08-31 00:00:00':'August','2020-09-30 00:00:00':'September','2020-10-31 00:00:00':'October','2020-11-30 00:00:00':'November','2020-12-31 00:00:00':'December',
            '2021-01-31 00:00:00':'January','2021-02-28 00:00:00':'February','2021-03-31 00:00:00':'March','2021-04-30 00:00:00':'April','2021-05-31 00:00:00':'May','2021-06-30 00:00:00':'June','2021-07-31 00:00:00':'July','2021-08-31 00:00:00':'August','2021-09-30 00:00:00':'September',}

    m_state = {'Johor','Kedah','Kelantan','Melaka','Negeri Sembilan','Pahang','Pulau Pinang','Perak','Perlis','Selangor','Terengganu','Sabah','Sarawak','W.P. Kuala Lumpur','W.P. Labuan','W.P. Putrajaya'}

    raw_cases['date']= pd.to_datetime(raw_cases['date'])
    
    final_cases = raw_cases.copy()
    final_cases.fillna(value = 0, inplace = True)

    selectShow = st.selectbox("Select an aspect to show", ['Outliers Detection','Data Analysis'])

    if selectShow == 'Outliers Detection': 
        left_column1, right_column2 = st.columns(2)
        with left_column1:
            boxplot1 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cases_new:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cases_new'
                    )

            st.altair_chart(boxplot1)

        with right_column2:
            boxplot2 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cases_import:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cases_import'
                    )

            st.altair_chart(boxplot2)
        
        left_column3, right_column4 = st.columns(2)
        with left_column3:
            boxplot3 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cases_recovered:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cases_recovered'
                    )

            st.altair_chart(boxplot3)

        with right_column4:
            boxplot4 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cases_active:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cases_active'
                    )

            st.altair_chart(boxplot4)
        
        left_column5, right_column6 = st.columns(2)
        with left_column5:
            boxplot5 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cases_cluster:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cases_cluster'
                    )

            st.altair_chart(boxplot5)

        with right_column6:
            boxplot6 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cases_pvax:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cases_pvax'
                    )

            st.altair_chart(boxplot6)
        
        left_column7, right_column8 = st.columns(2)
        with left_column7:
            boxplot7 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cases_fvax:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cases_fvax'
                    )

            st.altair_chart(boxplot7)

        with right_column8:
            boxplot8 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cases_child:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cases_child'
                    )

            st.altair_chart(boxplot8)
        
        left_column9, right_column10 = st.columns(2)
        with left_column9:
            boxplot9 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cases_adolescent:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cases_adolescent'
                    )

            st.altair_chart(boxplot9)

        with right_column10:
            boxplot10 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cases_adult:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cases_adult'
                    )

            st.altair_chart(boxplot10)
        
        left_column11, right_column12= st.columns(2)
        with left_column11:
            boxplot11 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cases_elderly:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cases_elderly'
                    )

            st.altair_chart(boxplot11)
        with right_column12:
            boxplot12 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cluster_import:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cluster_import'
                    )

            st.altair_chart(boxplot12)

        left_column13, right_column14= st.columns(2)
        with left_column13:
            boxplot13 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cluster_religious:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cluster_religious'
                    )

            st.altair_chart(boxplot13)

        with right_column14:
            boxplot14 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cluster_community:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cluster_community'
                    )

            st.altair_chart(boxplot14)
        
        left_column15, right_column16= st.columns(2)
        with left_column15:
            boxplot15 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cluster_highRisk:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cluster_highRisk'
                    )

            st.altair_chart(boxplot15)

        with right_column16:
            boxplot16 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cluster_education:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cluster_education'
                    )

            st.altair_chart(boxplot16)

        left_column17, right_column18= st.columns(2)
        with left_column17:
            boxplot17 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cluster_detentionCentre:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cluster_detentionCentre'
                    )

            st.altair_chart(boxplot17)

        with right_column18:
            boxplot18 = alt.Chart(final_cases).mark_boxplot().encode(
                y='cluster_workplace:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cluster_workplace'
                    )

            st.altair_chart(boxplot18)
        
        st.markdown('From the boxplots above, we can observe that there are a lot of outliers in cases_new and cases_recovered while there are fewer outliers in cases_import. It is similar to the reason mentioned in the boxplots of the nation level dataset. However, we decided to not remove these outliers as the data are crucial to this assignment and training model.')    
    else:
        selectGroupBy = st.selectbox("View By", ['Day','Month'])

        if selectGroupBy == 'Day':
            chart = alt.Chart(final_cases).mark_line().encode(
                alt.X('date', type='temporal'),
                alt.Y('cases_new', type='quantitative'),
            ).properties(
                width=1200,
                height=800,
                title='Total cases of Malaysia by Day'
            )

            id = final_cases['cases_new'].idxmax()
            day = final_cases.loc[id].date
            st.altair_chart(chart)
            st.markdown("The total cases of Malaysia is " + str(final_cases['cases_new'].sum()))
            st.markdown("The mean cases of Malaysia is " + str(final_cases['cases_new'].mean()))
            st.markdown("The state with the most cases is " + str(final_cases['cases_new'].idxmax()) + ' at ' + str(final_cases['cases_new'].max()))
            st.markdown("The day with the most cases is " + str(day) +' at ' + str(final_cases['cases_new'].max()))
        else:
            cases_month = final_cases.groupby(pd.Grouper(key='date', axis=0, freq='M')).sum()
            maxMonth = str(cases_month['cases_new'].idxmax())
            cases_month = cases_month.reset_index()
            monthChart = alt.Chart(cases_month).mark_line().encode(
                alt.X('date', type='temporal'),
                alt.Y('cases_new', type='quantitative'),
            ).properties(
                width=1200,
                height=800,
                title='Total cases of Malaysia by Month'
            )

            st.altair_chart(monthChart)
            st.markdown("The total cases of Malaysia is " + str(final_cases['cases_new'].sum()))
            st.markdown("The mean cases of Malaysia is " + str(final_cases['cases_new'].mean()))
            st.markdown("The month with the most cases is " + month[maxMonth] + ' at ' + str(cases_month['cases_new'].max()))
