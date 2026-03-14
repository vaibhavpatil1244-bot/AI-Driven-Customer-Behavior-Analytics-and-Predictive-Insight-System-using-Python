import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# Title
st.title("Customer Analytics Dashboard")

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

st.subheader("Dataset Preview")
st.write(df.head())

# -----------------------------
# Customer Segmentation Graph
# -----------------------------

st.subheader("Customer Segmentation")

plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Distribution")

st.pyplot(plt)

# -----------------------------
# Prediction Section
# -----------------------------

st.subheader("Customer Prediction")

income = st.slider("Annual Income", 10, 150)
score = st.slider("Spending Score", 1, 100)

if st.button("Predict Customer Type"):

    # Example rule (replace with model later)
    if score > 60:
        st.success("High Value Customer")
    elif score > 30:
        st.warning("Medium Value Customer")
    else:
        st.error("Low Value Customer")

import streamlit as st

st.title("Customer Analytics Dashboard")

age = st.number_input("Enter Age")
income = st.number_input("Annual Income")
score = st.number_input("Spending Score")

if st.button("Predict Customer Type", key="predict_customer"):
    st.success(prediction[0])

if prediction[0] == 0:
    st.success("Low Value Customer")

elif prediction[0] == 1:
    st.success("Medium Value Customer")

else:
    st.success("High Value Customer")

