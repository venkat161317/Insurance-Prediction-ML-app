# Step 1 : Load Important Modules
import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report , confusion_matrix
from sklearn.metrics import accuracy_score
import streamlit as st
# this streamlit is for web based application project

# web page Code
st.title("HEALTH INSURANCE PREDICTION")
img_url = "https://cdn.zeebiz.com/sites/default/files/2026/03/09/401943-health-insurance.png"
st.image(img_url)


#LOAD DATA and ML MODEL PART

#Step 2: 1load Insurance data
url="https://raw.githubusercontent.com/ankitmisk/UIT-data/refs/heads/main/Insurance.csv"
df=pd.read_csv(url)

#Step 3: EDA: Exploratory Data Analysis
df['Previous_Insurance']=df ['Previous_Insurance'].map({'No': 0, "Yes":1})
df['Insurance_Bought']=df['Insurance_Bought'].map({'No': 0, "Yes":1})

#Step 4: Divide dataset into features and target
X=df.iloc[:,:-1]
y = df.iloc[:,-1]

# Step 5: Divide data into Training & testing part
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test train_test_split(X,y, random_state-42, test_size-0.3)

#Step 6: Train Model
model = LogisticRegression()
model.fit(X_train,y_train)

# show data sample
st.write(df.head())
# Create Sidebar for user input form
st.sidebar.title("Fill Customer Details")
st.sidebar.image(img_url)
