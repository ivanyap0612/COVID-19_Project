import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt 

def vax_state():
    vax_state = pd.read_csv('Dataset/vax_state.csv')
    vax_state['date']= pd.to_datetime(vax_state['date'])
    
    month = {'2020-03-31 00:00:00':'March', '2020-04-30 00:00:00':'April','2020-05-31 00:00:00':'May','2020-06-30 00:00:00':'June','2020-07-31 00:00:00':'July','2020-08-31 00:00:00':'August','2020-09-30 00:00:00':'September','2020-10-31 00:00:00':'October','2020-11-30 00:00:00':'November','2020-12-31 00:00:00':'December',
            '2021-01-31 00:00:00':'January','2021-02-28 00:00:00':'February','2021-03-31 00:00:00':'March','2021-04-30 00:00:00':'April','2021-05-31 00:00:00':'May','2021-06-30 00:00:00':'June','2021-07-31 00:00:00':'July','2021-08-31 00:00:00':'August','2021-09-30 00:00:00':'September','2021-10-31 00:00:00':'October'}

    group_vax = vax_state.groupby([pd.Grouper(key='date', axis=0, freq='M'),"state"]).agg('sum')
    vacc_state = vax_state.groupby(['state']).sum()
    vax_month = vax_state.groupby(pd.Grouper(key='date', axis=0, freq='M')).sum()
    maxMonth = str(vax_month['daily_full'].idxmax())
    
    selectShow = st.selectbox("Select an aspect to show", ['Outliers Detection','Data Analysis'])

    if selectShow == 'Outliers Detection': 
        c1,c2= st.columns(2)
        with c1:
            boxplot1 = alt.Chart(vax_state).mark_boxplot().encode(
                y='daily_partial:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='daily_partial'
                    )

            st.altair_chart(boxplot1)

        with c2:
            boxplot2 = alt.Chart(vax_state).mark_boxplot().encode(
                y='daily_full:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='daily_full'
                    )

            st.altair_chart(boxplot2)

        c3,c4= st.columns(2)
        with c3:
            boxplot3 = alt.Chart(vax_state).mark_boxplot().encode(
                y='daily:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='daily'
                    )

            st.altair_chart(boxplot3)

        with c4:
            boxplot4 = alt.Chart(vax_state).mark_boxplot().encode(
                y='daily_partial_child:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='daily_partial_child'
                    )

            st.altair_chart(boxplot4)
        
        c5,c6= st.columns(2)
        with c5:
            boxplot5 = alt.Chart(vax_state).mark_boxplot().encode(
                y='daily_full_child:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='daily_full_child'
                    )

            st.altair_chart(boxplot5)

        with c6:
            boxplot6 = alt.Chart(vax_state).mark_boxplot().encode(
                y='cumul_partial:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cumul_partial'
                    )

            st.altair_chart(boxplot6)
        
        c7,c8= st.columns(2)
        with c7:
            boxplot7 = alt.Chart(vax_state).mark_boxplot().encode(
                y='cumul_full:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cumul_full'
                    )

            st.altair_chart(boxplot7)

        with c8:
            boxplot8 = alt.Chart(vax_state).mark_boxplot().encode(
                y='cumul:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cumul'
                    )

            st.altair_chart(boxplot8)
        
        c9,c10= st.columns(2)
        with c9:
            boxplot9 = alt.Chart(vax_state).mark_boxplot().encode(
                y='cumul_partial_child:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cumul_partial_child'
                    )

            st.altair_chart(boxplot9)

        with c10:
            boxplot10 = alt.Chart(vax_state).mark_boxplot().encode(
                y='cumul_full_child:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cumul_full_child'
                    )

            st.altair_chart(boxplot10)

        c11,c12= st.columns(2)
        with c11:
            boxplot11 = alt.Chart(vax_state).mark_boxplot().encode(
                y='pfizer1:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='pfizer1'
                    )

            st.altair_chart(boxplot11)

        with c12:
            boxplot12 = alt.Chart(vax_state).mark_boxplot().encode(
                y='pfizer2:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='pfizer2'
                    )

            st.altair_chart(boxplot12)
        
        c13,c14= st.columns(2)
        with c13:
            boxplot13 = alt.Chart(vax_state).mark_boxplot().encode(
                y='sinovac1:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='sinovac1'
                    )

            st.altair_chart(boxplot13)

        with c14:
            boxplot14 = alt.Chart(vax_state).mark_boxplot().encode(
                y='sinovac2:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='sinovac2'
                    )

            st.altair_chart(boxplot14)
        
        c15,c16= st.columns(2)
        with c15:
            boxplot15 = alt.Chart(vax_state).mark_boxplot().encode(
                y='astra1:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='astra1'
                    )

            st.altair_chart(boxplot15)

        with c16:
            boxplot16 = alt.Chart(vax_state).mark_boxplot().encode(
                y='astra2:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='astra2'
                    )

            st.altair_chart(boxplot16)
        
        c17,c18= st.columns(2)
        with c17:
            boxplot17 = alt.Chart(vax_state).mark_boxplot().encode(
                y='cansino:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='cansino'
                    )

            st.altair_chart(boxplot17)

        with c18:
            boxplot18 = alt.Chart(vax_state).mark_boxplot().encode(
                y='pending:Q'
            ).properties(
                        width=350,
                        height=200,
                        title='pending'
                    )

            st.altair_chart(boxplot18)
        
        st.markdown('Based on the boxplot above, we can see that every column in this dataset contains a lot of outliers. All of the boxplots showed that the data is positively skewed. This may be due to the slow start of the COVID-19 vaccine supply, followed by a sudden increase of high number vaccine supply. However, we decided to not remove these outliers as the data are crucial for further analysis and training model.')
    
    else:
        left_column2, right_column2 = st.columns(2)
        with left_column2:
            selectGroupBy = st.selectbox("View By", ['Day','Month'])

        with right_column2:
            selectState = st.selectbox("Select a state to view", ['All','Johor','Kedah','Kelantan','Melaka','Negeri Sembilan','Pahang','Pulau Pinang','Perak','Perlis','Selangor','Terengganu','Sabah','Sarawak','W.P. Kuala Lumpur','W.P. Labuan','W.P. Putrajaya'])

        if selectGroupBy == 'Day':
            if selectState == 'All':
                chart = alt.Chart(vax_state).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('daily_full', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=1200,
                    height=800,
                    title='Total Number of People Who is Fully Vaccinated of Each State by Day'
                )

                id = vax_state['daily_full'].idxmax()
                day = vax_state.loc[id].date
                state = vax_state.loc[id].state
                st.altair_chart(chart)
                st.markdown("The total number of people Who is fully vaccinated " + str(vacc_state['daily_full'].sum()))
                st.markdown("The mean number of people Who is fully vaccinated is " + str(vacc_state['daily_full'].mean()))
                st.markdown("The state with the most number of people Who is fully vaccinated is " + str(vacc_state['daily_full'].idxmax()) + ' at ' + str(vacc_state['daily_full'].max()))
                st.markdown("The day with the most number of people Who is fully vaccinated is " + str(day) + ' in ' + state +' at ' + str(vacc_state['daily_full'].max()))
                
            else:
                state_total = vax_state[vax_state['state'] == selectState]
                state_chart = alt.Chart(state_total).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('daily_full', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=1200,
                    height=800,
                    title='Total Number of People Who is Fully Vaccinated of ' + selectState + ' by Day'
                )
                day = state_total['daily_full'].idxmax()
                day = state_total.loc[day].date

                st.altair_chart(state_chart)
                st.markdown("The total number of people who is fully vaccinated " + selectState + ' is ' + str(state_total['daily_full'].sum()))        
                st.markdown("The mean number of people who is fully vaccinated is " + selectState + ' is ' + str(state_total['daily_full'].mean()))     
                st.markdown("The day with the most number of people Who is fully vaccinated is " + str(day) + ' at ' + str(state_total['daily_full'].max()))
        else:
            if selectState == 'All':
                group_vax = group_vax.reset_index()
                monthChart = alt.Chart(group_vax).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('daily_full', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=1200,
                    height=800,
                    title='Total Number of People Who is Fully Vaccinated of Each State by Month'
                )

                st.altair_chart(monthChart)
                st.markdown("The total number of people who is fully vaccinated is " + str(vacc_state['daily_full'].sum()))
                st.markdown("The mean number of people who is fully vaccinated is " + str(vacc_state['daily_full'].mean()))
                st.markdown("The state with the most number of people Who is fully vaccinated is " + str(vacc_state['daily_full'].idxmax()) + ' at ' + str(vacc_state['daily_full'].max()))
                st.markdown("The month with the most number of people Who is fully vaccinated is " + month[maxMonth] + ' at ' + str(vacc_state['daily_full'].max()))
                
            else:
                group_vax = group_vax.reset_index()
                state_month_total = group_vax[group_vax['state'] == selectState]
                stateMonthChart = alt.Chart(state_month_total).mark_line().encode(
                    alt.X('date', type='temporal'),
                    alt.Y('daily_full', type='quantitative'),
                    alt.Color('state', type='nominal')
                ).properties(
                    width=1200,
                    height=800,
                    title='Total Number of People Who is Fully Vaccinated of ' + selectState + ' by Month'            
                )

                st.altair_chart(stateMonthChart)
                st.markdown("The total number of people who is fully vaccinated of " + selectState + ' is ' + str(state_month_total['daily_full'].sum()))        
                st.markdown("The mean number of people who is fully vaccinated of " + selectState + ' is ' + str(state_month_total['daily_full'].mean()))     
                st.markdown("The month with the most number of people Who is fully vaccinated is " + month[maxMonth] + ' at ' + str(state_month_total['daily_full'].max()))
               

