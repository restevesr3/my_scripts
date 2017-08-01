
# coding: utf-8

# # Lecture 24 - Index Hierarchy

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


ser = Series(randn(6), index=[[1,1,1,2,2,2],['a', 'b', 'c', 'a', 'b', 'c']])


# In[6]:


ser


# In[7]:


# Check multiple levels
ser.index


# In[8]:


ser[1]


# In[9]:


ser[2]


# In[10]:


# internal level
ser[:,'a']


# In[11]:


# Unstack Method
dframe = ser.unstack()


# In[12]:


dframe


# In[13]:


dframe2 = DataFrame(np.arange(16).reshape(4,4), index=[['a', 'a', 'b', 'b'],[1,2,1,2]],
                   columns=[['NY', 'NY','LA', 'SF'],['cold', 'hot','hot', 'cold']]
                   )


# In[14]:


dframe2


# In[15]:


# naming index levels
dframe2.index.names=['INDEX_1', 'INDEX_2']


# In[18]:


# naming the columns
dframe2.columns.names = ['Cities', 'Temp']


# In[19]:


dframe2


# In[20]:


# Interchange the index orders
dframe2.swaplevel('Cities', 'Temp', axis=1)


# In[21]:


# Sort Levels
dframe2.sortlevel(1)


# In[22]:


# perform operation on a level
dframe2.sum(level='Temp', axis=1)


# In[ ]:




