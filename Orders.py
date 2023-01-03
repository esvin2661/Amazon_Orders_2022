#!/usr/bin/env python
# coding: utf-8

# In[7]:


import plotly.express as px
import pandas as pd

df = pd.read_csv('/Users/esvin/Desktop/Python Project /01-Jan-2022_to_31-Dec-2022.csv')
df = df.fillna(0)
df["Item Total"] = df["Item Total"].str.replace('$','',regex=False).astype(float)
df["Item Subtotal"] = df["Item Subtotal"].str.replace('$','',regex=False).astype(float)
df["Item Subtotal Tax"] = df["Item Subtotal Tax"].str.replace('$','',regex=False).astype(float)
df['Order Date'] = pd.to_datetime(df['Order Date']).dt.date 

fig = px.bar(df, x="Order Date", y="Item Total")
fig.show()


# In[ ]:




