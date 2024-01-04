#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set()
import warnings
warnings.filterwarnings('ignore')


# In[4]:


import xlrd


# In[5]:


df=pd.read_excel('Employee_Data.xls')


# In[6]:


df.head()


# In[7]:


df.info()


# In[8]:


df.isnull().sum()


# In[9]:


df['Department'].value_counts()


# In[10]:


df['Department']=df['Department'].fillna('Sales and Marketing')


# In[11]:


sns.boxplot(df,y='Age')


# In[12]:


df['Age']=df['Age'].fillna(df['Age'].mean())


# In[13]:


sns.boxplot(df,y='Experience')


# In[14]:


df['Experience']=df['Experience'].fillna(df['Experience'].mean())


# In[15]:


df.isnull().sum()


# #### APPORACH_1: NORMALISATION

# In[16]:


dataset_1=df.copy()


# In[18]:


dataset_1


# In[19]:


dataset_1.info()


# In[20]:


dataset_1=dataset_1.iloc[:,4:]


# In[21]:


dataset_1


# In[23]:


from sklearn.preprocessing import Normalizer
x_nor=Normalizer()
x_norm=x_nor.fit_transform(dataset_1)


# In[24]:


x_norm


# In[26]:


dataset_nor=pd.DataFrame(x_norm)


# In[27]:


dataset_nor


# #### APPORACH_2:  STANDARDISATION

# In[28]:


dataset_1


# In[30]:


from sklearn.preprocessing import StandardScaler
std_scaler=StandardScaler()
dataset_std=std_scaler.fit_transform(dataset_1)


# In[32]:


std_dataset=pd.DataFrame(dataset_std)


# In[33]:


std_dataset


# In[ ]:




