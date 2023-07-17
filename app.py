import streamlit as st
import pandas as pd
import plotly.express as plx

data = pd.readcsv('vehicles_us.csv')

st.header('Welcome to my sprint 4 project!!')

def create_bar():
    fig = px.bar(data, x='model', y='price', title='Car prices by model')
    st.plotly_chart(fig)

def create_hist():
    fig2 = px.histogram(data, x='condition', title='Frequency of conditions')
    st.plotly_chart(fig2)

def create_scatter():
    fig3 = px.scatter(data, x='model_year', y='odometer', title='Comparing odometers by model_year')
    st.plotly_chart(fig3)

show_bar = st.checkbox("Show Bar Plot")
if show_bar:
    create_bar()

create_hist()
create_scatter()

