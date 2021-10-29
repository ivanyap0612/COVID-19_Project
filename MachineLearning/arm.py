import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

def arm():
    data = pd.read_csv('Dataset/Covid Dataset.csv')
    for i in data.columns:
        data[i] = data[i].map(dict(Yes=True, No=False))

    st.markdown('Table below shows the itemsets and their supports found from the symptoms datasets. Some filterings are performed to get the itemsets contained COVID-19.')

    itemsets = apriori(data, min_support=0.5, use_colnames=True)
    itemsets = itemsets.applymap(lambda x: list(x) if isinstance(x, frozenset) else x )
    df = itemsets[['COVID-19' in i for i in itemsets['itemsets']]].sort_values('support', ascending=False).reset_index(drop=True)
    st.table(df)

    st.markdown('Table below shows the rules and their statistics of the symptoms of COVID-19. The threshold is set to 0.9 so that it filtered out only the COVID-19 as consequents.')

    rules = association_rules(itemsets, min_threshold=0.9)
    rules = rules.applymap(lambda x: list(x) if isinstance(x, frozenset) else x )
    df = rules[['COVID-19' in i for i in rules['consequents']]].sort_values('support', ascending=False).reset_index(drop=True)
    st.dataframe(df)

    st.markdown('From the statistics above, we can see that patients with symptoms of either dry cough, sore throat and breathing problem most likely have infected COVID-19 with respective support and confidence above. ')
