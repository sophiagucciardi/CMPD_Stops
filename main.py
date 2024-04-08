import streamlit as st
import pandas as pd 

st.write('CMPD Traffic Stops')

@st.cache_data
def load_data(csv):
    df = pd.read_csv(csv)
    return df

stops = pd.read_csv('/Users/sophiagucciardi/Desktop/DSBA 5122/CMPD_Stops/data/Officer_Traffic_Stops.csv')

st.dataframe(stops) 



