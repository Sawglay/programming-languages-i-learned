import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title("Visualization with streamlit")

FileToOpen = "Dataset.xlsx"
sheetName = "SalesData"
df = pd.read_excel(FileToOpen, sheet_name = sheetName)

st.subheader("Box Plot")
fig_box1 = px.box(df, y = "Sales")  # Using plotly express
st.plotly_chart(fig_box1)

fig_box2 = px.box(df, x="Day",y = "Sales")
st.plotly_chart(fig_box2)

st.subheader("Bar Chart")
st.bar_chart(df, y = "Sales") # Using streamlit
st.bar_chart(df, x = "Date",y = "Sales")

st.subheader("Line Chart")
st.line_chart(df, x = "Date", y = "Sales") # Using Line Chart
st.line_chart(df, x = "Date", y = ["Sales", "Temperature"]) 
st.line_chart(df, x = "Date", y = ["Sales", "Temperature", "Rainfall"]) 

st.subheader("Stacked Bar Chart") # Using Stack Bar Chart
sheetName = "cars"
df_cars = pd.read_excel(FileToOpen, sheet_name = sheetName)

st.bar_chart(df_cars, x = "Year", y = ["EV", "ICE"])
st.bar_chart(df_cars, x = "Year", y = ["EV", "ICE"], stack = False)
st.bar_chart(df_cars, x = "Year", y = ["EV", "ICE"], stack = "normalize")

st.subheader("Histogram") # Histogram
fig_hist = px.histogram(df, y = "Sales")  # Using plotly express
st.plotly_chart(fig_hist)

fig_hist1 = px.histogram(df, y = "Sales", nbins = 8)
st.plotly_chart(fig_hist1)

st.subheader("Scatter Chart") # Scatter Plot
st.scatter_chart(df, x = "Temperature", y = "Sales") # Using Streamlit
st.scatter_chart(df, x = "Temperature", y = "Sales", color = "Rainfall", size = "Rainfall")

st.subheader("Heat Map")
# Using seaborn
df_selected = df[["Sales", "Temperature", "Rainfall"]]
matrix = df_selected.corr()
fig, ax = plt.subplots()
sns.heatmap(matrix, annot = True , cmap = "coolwarm", ax = ax)
st.pyplot(fig)

# Using piechart
st.subheader("Pie Chart")
fig = px.pie(df, values = "Sales", names = "Day")
st.plotly_chart(fig)
