from numpy import double
import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Titanic Dashboard",page_icon="🚢",
layout="wide")

@st.cache_data
def read_data():
    df = pd.read_csv("titanic.csv")
    return df
df = read_data()
st.title("🚢 Titanic Dashboard")
st.markdown("##")

pie_chart = px.pie(names = df["Embarked"].unique(),values=df.groupby("Embarked")["Embarked"].count(),hole=0.5)
box_plot = px.box(df, y="Age",x="Pclass")
group_plot = px.histogram(df, x="Survived", color="Pclass",barmode='group') 
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader(f" Fist class Passenger Deaths: {len(df.loc[(df['Pclass'] == 1) & (df['Survived'] == 0)])}")
    st.subheader(f"Second class Passenger Deaths: {len(df.loc[(df['Pclass'] == 2) & (df['Survived'] == 0)])}")
    st.subheader(f"Third class Passenger Deaths: {len(df.loc[(df['Pclass'] == 3) & (df['Survived'] == 0)])}")

with middle_column:
    st.subheader(f"First class Passenger Survived : {len(df.loc[(df['Pclass'] == 1) & (df['Survived'] == 1)])}")
    st.subheader(f"Second class Passenger Survived: {len(df.loc[(df['Pclass'] == 2) & (df['Survived'] == 1)])}")
    st.subheader(f"Third class Passenger Survived: {len(df.loc[(df['Pclass'] == 3) & (df['Survived'] == 1)])}")

with right_column:
    st.subheader(f"Average Fare Value: {int(df['Fare'].mean())}")
    st.subheader(f"Average Fare Tax : {int(df['Fare_Tax'].mean())}")
    st.subheader(f"Average Luggage Charges Value: {int(df['Luggage Charges'].mean())}")
    
    
st.markdown('---')
def create_plot(df, gender):
    filtered_df = df[df['Sex'] == gender.lower()]
    fig = px.histogram(filtered_df, x='Age', color='Survived')
    return fig
st.sidebar.header('Filters')
gender_filter = st.sidebar.selectbox('Select Gender', ['Male', 'Female'])

st.header('Survival Histogram based on Age')
st.plotly_chart(create_plot(df, gender_filter))
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Passenger belonging to Embarked % (Pie Chart)")
with middle_column:
    st.subheader("Survival Histogram based on Pclass")
with right_column:
    st.subheader("Box plot Based on Pclass vs age")

st.markdown("---")
left_column.plotly_chart(pie_chart,use_container_width=True)
right_column.plotly_chart(box_plot,use_container_width=True)
middle_column.plotly_chart(group_plot,use_container_width=True)

line_plot = px.line(df,x="Fare",y=["Fare_Tax","Luggage Charges","Food Charges"])
group_plot1 = px.histogram(df, x="Survived", color="Sex",barmode='group') 
pie_chart1 = px.pie(names = df["Survived"].unique(),values=df.groupby("Survived")["Survived"].count(),hole=0.5)

left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader("Line plot for Fare_Tax,Luggage Charges,Food Charges")
with middle_column:
    st.subheader("Survival Histogram Based on Sex")
with right_column:
    st.subheader(" Survival Rate %(Pie Chart)")


st.markdown("---")
left_column.plotly_chart(line_plot,use_container_width=True)
middle_column.plotly_chart(group_plot1,use_container_width=True)
right_column.plotly_chart(pie_chart1,use_container_width=True)


plot = px.histogram(df, x="SibSp",color="Sex",barmode='group') 
left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Histogram of Sibsp")

left_column.plotly_chart(plot,use_container_width=True)

selected_Pclass = [1, 2, 3]
filtered_data = df[df['Pclass'].isin(selected_Pclass)]
survived_counts = df.groupby('Survived').size()

plot_type = st.sidebar.selectbox('Select Plot Type', ('Pie', 'Bar'))
if plot_type == 'Pie':
    fig = px.pie(filtered_data, values='Pclass', names='Sex')
elif plot_type == 'Bar':
    fig = px.bar(filtered_data,  x='Pclass', y=["Fare_Tax","Luggage Charges","Food Charges"])
st.plotly_chart(fig)
