#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# Load the data

df = pd.read_csv("C:/Users/Ijaz khan/OneDrive/Desktop/Medical Inventory Optimaization Dataset.csv")



# In[4]:


# Understanding data structure

df.head()


# In[5]:


df.shape


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df.isnull().sum()


# In[9]:


#df_del = ['Formulation','DrugName','SubCat','SubCat1']


# In[10]:


#df.drop(df_del,inplace = True, axis = 1)
#df.head()

df = df.fillna(method = 'ffill')
df.isnull().sum()
df.head(50)


# In[11]:


df.hist(bins=20,figsize=(10,6))
plt.show()


# In[12]:


plt.figure(figsize=(10,6))
sns.boxplot(data=df)
plt.show()


# In[13]:


sns.pairplot(df)
plt.show()


# In[14]:


plt.figure(figsize=(12,10))
sns.heatmap(df.corr(),annot = True, cmap = "coolwarm")
plt.show()


# In[15]:


plt.figure(figsize=(10,6))
sns.histplot(df['Final_Cost'],kde = True)
plt.show()


# In[16]:


plt.figure(figsize=(10,6))
sns.boxplot(x = 'Formulation', y = 'Quantity', data = df)
plt.show()


# In[17]:


plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot = True, cmap = 'viridis')
plt.show()


# In[20]:


sns.countplot(x = df['Formulation'])
plt.show()


# In[22]:


sns.countplot(x = df['Typeofsales'])
plt.show()


# In[ ]:




