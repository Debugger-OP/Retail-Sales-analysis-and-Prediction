import streamlit as st
import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

st.title("📊 Retail Sales Analysis & Forecasting")

conn = sqlite3.connect('retail_sales.db')
df = pd.read_sql_query("SELECT * FROM sales", conn)
conn.close()

df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M').astype(str)

# Sidebar filters
category = st.sidebar.selectbox("Select Category", ["All"] + list(df['category'].unique()))
if category != "All":
    df = df[df['category'] == category]

st.subheader("Revenue by Category")
fig, ax = plt.subplots()
sns.barplot(x='category', y='revenue', data=df, estimator=sum, errorbar=None, ax=ax)
st.pyplot(fig)

st.subheader("Monthly Revenue Trend")
monthly = df.groupby('month')['revenue'].sum().reset_index()
fig, ax = plt.subplots()
sns.lineplot(x='month', y='revenue', data=monthly, marker='o', ax=ax)
plt.xticks(rotation=45)
st.pyplot(fig)

model = LinearRegression()
monthly['month_num'] = np.arange(len(monthly))
model.fit(monthly[['month_num']], monthly['revenue'])
next_month = pd.DataFrame({'month_num':[len(monthly)]})
pred = model.predict(next_month)[0]
st.metric("Predicted Revenue Next Month", f"₹{pred:,.2f}")
