import streamlit as st 
import numpy as np
import pandas as pd
import altair as alt 

def population():

    pop = pd.read_csv( "Dataset/population.csv")
    pop = pop.drop(0)

    popChart = alt.Chart(pop).mark_bar().encode(
        alt.X('state', type='nominal'),
        alt.Y('pop', type='quantitative')
    ).properties(
                width=1200,
                height=800,
                title='Total Population of Each State'
            )

    st.altair_chart(popChart)
    st.markdown('The graph shows the total population of every state in Malaysia. Selangor comes into first place due to it being the main economic center in Malaysia. Johor and Sabah are very similar in terms of the total population. W.P. Labuan and W.P. Putrajaya has the least total population. This is mainly restricted by its land size and proximity to another large state.\n')

    pop18Chart = alt.Chart(pop).mark_bar().encode(
        alt.X('state', type='nominal'),
        alt.Y('pop_18', type='quantitative')
    ).properties(
                width=1200,
                height=800,
                title='Total Population Above 18 Years Old of Each State'
            )

    st.altair_chart(pop18Chart)
    st.markdown('The graph shows the total population of people aged 18 years old and above in Malaysia. We can see that the pattern generally follows the pattern of the total population of every state in Malaysia')

    pop60Chart = alt.Chart(pop).mark_bar().encode(
        alt.X('state', type='nominal'),
        alt.Y('pop_60', type='quantitative')
    ).properties(
                width=1200,
                height=800,
                title='Total Population Above 60 Years Old of Each State'
            )

    st.altair_chart(pop60Chart)
    st.markdown('The graph shows the total population of people aged 60 years old and above in Malaysia. We can see that the pattern generally follows the pattern of the total population of every state in Malaysia except Sabah and Sarawak. Sarawak has more senior citizens but its total population is lesser than Sabah. Similarly, Sabah has fewer senior citizens but the total population is more than Sarawak.\n')