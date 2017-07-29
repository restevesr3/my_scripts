
# coding: utf-8

# # Lecture 17 - Reindexing

# ## Robert Esteves

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from pandas import Series, DataFrame


# In[4]:


from numpy.random import randn


# In[5]:


ser1 = Series([1, 2, 3, 4], index = ['A', 'B', 'C', 'D'])


# In[6]:


ser1


# In[7]:


# How to reindex

ser3 = Series(['USA', 'Mexico', 'Canada'], index=[0,5, 10])


# In[8]:


ser3


# In[9]:


ranger = range(15)


# In[11]:


list(ranger)


# In[13]:


ser3.reindex(ranger, method='ffill') 
#ffill = forward fill


# In[15]:


dframe = DataFrame(randn(25).reshape(5,5), index=['A', 'B', 'D', 'E', 'F'], 
                   columns=['col1', 'col2', 'col3', 'col4', 'col5'])


# In[16]:


dframe


# In[17]:


# Let's reindex

dframe2 = dframe.reindex(['A', 'B', 'C', 'D', 'E', 'F'])


# In[18]:


dframe2


# In[19]:


new_columns = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6']


# In[20]:


dframe2.reindex(columns=new_columns)


# In[21]:


# Reindex with the .ix

dframe


# In[22]:


dframe.ix[['A', 'B', 'C', 'D', 'E', 'F'], new_columns]


# In[ ]:




