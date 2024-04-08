import streamlit as st
import pandas as pd
import altair as alt

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df

stops = load_data('/Users/sophiagucciardi/Desktop/DSBA 5122/CMPD_Stops/data/Officer_Traffic_Stops.csv')

st.header('Stops by Age')

age_bar = alt.Chart(stops).mark_bar().encode(
    alt.X("Driver_Age", bin=alt.Bin(maxbins=30)),
    y="count()",
)

st.altair_chart(age_bar)

