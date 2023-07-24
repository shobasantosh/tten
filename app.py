import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv('vehicles_us.csv')

median_year = data.groupby('model')['model_year'].transform('median')
data['model_year'].fillna(median_year, inplace=True)

median_cylinders = data.groupby('model')['cylinders'].transform('median')
data['cylinders'].fillna(median_cylinders, inplace=True)

median_odometer = data.groupby('model_year')['odometer'].transform('median')
data['odometer'].fillna(median_odometer, inplace=True)

data["paint_color"] = data["paint_color"].fillna("unknown")
data["is_4wd"] = data["is_4wd"].fillna(0)

st.header('Welcome to my sprint 4 project!!')

def create_bar():
    fig = px.bar(data, x='model', y='price', title='Car prices by model')
    st.plotly_chart(fig)

def create_hist():
    fig2 = px.histogram(data, x='days_listed', title='Frequency by Days Listed')
    st.plotly_chart(fig2)

def create_scatter():
    fig3 = px.scatter(data, x='model_year', y='odometer', title='Comparing odometers by model_year')
    st.plotly_chart(fig3)

show_bar = st.checkbox("Show Bar Plot")
if show_bar:
    create_bar()

create_hist()
create_scatter()

