import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import plotly.express as px
from PIL import Image
img=Image.open("01.jpg")
st.image(img,width=900)


st.title("Data Presenter")

choices = st.sidebar.selectbox(
    'What would you like to perform?',
    ('Show Data','Analysis', 'Visualize')
)

df = pd.read_csv("Mall_Customers.csv")
if choices == 'Show Data':
    st.subheader("Data")
    if df is not None:
        st.dataframe(df.head())
        all_col = df.columns.to_list()
        sub_task = st.sidebar.selectbox("select",("Select","Describe Data"))
        if sub_task == "Describe Data":
            st.write("Data Description:",df.describe())
            

elif choices == 'Analysis':
    st.subheader("Analysis")
    
    all_col = df.columns.to_list()
    #select = st.multiselect("Select",all_col)
    
    if st.sidebar.checkbox("View Shape"):
        st.write("Shape is ",df.shape)
    
    if st.sidebar.checkbox("View Columns"):
        select = st.multiselect("Select",all_col)
        new_df = df[select]
        st.dataframe(new_df)  
        
    if st.sidebar.checkbox("View correlation"):
        st.write("Shape is ",df.corr(method ='pearson')) 
        
    if st.sidebar.checkbox("Drop Missing Value"):
        df = df.dropna()
        st.write("Dropped Missing Values ",df)     
        
elif choices == 'Visualize':
    st.subheader("Visualize")
    
    all_col = df.columns.to_list()
    all_coll = df.columns.to_list()
    
    if st.sidebar.checkbox("Bar Chart"):
        bar = st.multiselect("Select Features ",all_col,key = 'a')
        new_df = df[bar]
        st.bar_chart(df[bar])
            
    if st.sidebar.checkbox("Area_chart"):        
        
        area = st.multiselect("Select Features",all_col)
        new_dff = df[area]
        st.area_chart(df[area])
        
    if st.sidebar.checkbox("Line Chart"):
        st.line_chart(df)
        
    if st.sidebar.checkbox("Pie chart"):        
        
    
        fig = px.pie(df,values='Age', names='Gender',title='Pie chart')
        fig.show()
       
    if st.sidebar.checkbox("Horizontal Bar Chart"):
        fig = px.bar(df, x="Annual Income (k$)", y="Spending Score (1-100)", orientation='h')
        fig.show()     
        
    if st.sidebar.checkbox("Dot plots"):
        fig = px.scatter(df, x="Annual Income (k$)", y="Gender", color="Gender",
                 title="Gender Earnings Disparity",
                 labels={"salary":"Annual Salary (in thousands)"} # customize axis label
                )

        fig.show()
