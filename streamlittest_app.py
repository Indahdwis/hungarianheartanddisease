import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "hungarian.data"
column_names = ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal", "num"]
df = pd.read_csv(file_path, header=None, names=column_names, sep=' ')

# Streamlit app
st.title("Heart Disease Dataset - Hungarian")

# Show the dataset
st.subheader("Dataset Preview")
st.write(df.head())

# Basic statistics
st.subheader("Basic Statistics")
st.write(df.describe())

# Visualization (use st.pyplot for Matplotlib plots)
st.subheader("Visualization")

# Example: Bar chart of sex distribution
st.bar_chart(df['sex'].value_counts())
