
# coding: utf-8

# # Lecture 16 - Index Objects

# ## Robert Esteves

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from pandas import Series, DataFrame


# In[4]:


my_ser = Series([1,2,3,4], index=['A', 'B', 'C', 'D'])


# In[5]:


my_ser


# In[7]:


my_index = my_ser.index


# In[8]:


my_index


# In[9]:


my_index[2]


# In[10]:


my_index[2:]


# In[12]:


# What happens when you try to change an index
my_index[0]

# Note: indexes don't support mutable operation
# You have to pass an entire index


# In[ ]:




