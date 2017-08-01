
# coding: utf-8

# # Lecture 21 - Rank and Sort

# ## Robert Esteves

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


from pandas import Series, DataFrame


# In[4]:


ser1 = Series(range(3), index=['C', 'A', 'B'])


# In[5]:


ser1


# In[6]:


ser1.sort_index()


# In[7]:


# Order series by its values
ser1.order()


# In[8]:


ser1.sort_values()


# In[9]:


# Ranking


# In[10]:


from numpy.random import randn


# In[12]:


ser2 = Series(randn(10))


# In[13]:


ser2


# In[14]:


ser1.sort()


# In[16]:


ser2.sort_values()


# In[17]:


# Find the rank of each value
ser2.rank()


# In[18]:


ser3 = Series(randn(10))


# In[19]:


ser3


# In[20]:


ser3.rank()


# In[21]:


ser3.sort_values()


# In[22]:


ser3.rank()


# In[ ]:




