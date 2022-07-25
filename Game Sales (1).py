#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data=pd.read_csv(r'C:\Users\HI\Downloads\Compressed\archive_11\vgsales.csv')
data.head()


# In[227]:


data1=data[['Name','Year','Global_Sales']]
data1=data1.sort_values('Year',ascending=False)
data1


# In[47]:


data.info()


# In[49]:


data.isnull().sum()


# In[6]:


twosix=data[data.Year==2006]
twosix=twosix.sort_values('Global_Sales',ascending=False).head(5)
twosix


# In[7]:


twonine=data[data.Year==2009]
twonine=twonine.sort_values('Global_Sales',ascending=False).head(5)
twonine


# In[4]:


figure=px.bar(twosix,x='Name',y='Global_Sales',
             title="Best selling games in 2006")
figure.show()


# In[14]:


figure=px.bar(twonine,x='Name',y='Global_Sales',
             title="Best selling games in 2009")
figure.show()


# In[30]:


#Best performing platforms

platform=data.groupby('Platform').sum()['Global_Sales'].reset_index()
platform=platform.sort_values('Global_Sales',ascending=False).head(5)
platform


# In[31]:


figure2=px.bar(platform,x='Platform',y='Global_Sales',
              title="Platforms with most sales")
figure2.show()


# In[19]:


genre=data.groupby('Genre').sum()['Global_Sales'].reset_index()
genre=genre.sort_values('Global_Sales',ascending=False).head(5)
genre


# In[34]:


figure3=px.bar(genre,x='Genre',y='Global_Sales',
              title="Best performing genre")
figure3.show()


# In[25]:


publisher=data.groupby('Publisher').sum()['Global_Sales'].reset_index()
publisher=publisher.sort_values('Global_Sales',ascending=False).head(5)
publisher


# In[27]:


figure13=px.bar(publisher,x='Publisher',y='Global_Sales',
              title="Best performing publisher")
figure13.show()


# In[28]:


#Top 3 publishers in Japan, Europe, North America & Other parts of the world

pubreg=data.groupby('Publisher').agg({'JP_Sales':'sum','EU_Sales':'sum','NA_Sales':'sum','Other_Sales':'sum'})
pubreg=pubreg.sort_values('NA_Sales',ascending=False).head(3)
pubreg


# In[29]:


pubreg.plot(kind='bar',figsize=(15,8))
plt.xlabel('Publisher')
plt.ylabel('Sales')
plt.title('Video Game Sales Per Region from Publishers')


# In[223]:


#Best performing platforms in all regions

platreg=data.groupby('Platform').agg({'JP_Sales':'sum','EU_Sales':'sum','NA_Sales':'sum','Other_Sales':'sum'})
platreg=platreg.sort_values('NA_Sales',ascending=False).head(5)
platreg


# In[226]:


platreg.plot(kind='bar',figsize=(15,8))
plt.xlabel('Platform')
plt.ylabel('Sales')
plt.title('Best Performing Platforms in Regions')

