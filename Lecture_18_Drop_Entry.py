
# coding: utf-8

# # Lecture 18 - Drop Entry

# ## Robert Esteves

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from pandas import Series, DataFrame


# In[5]:


ser1 = Series(np.arange(3), index=['a', 'b', 'c'])


# In[6]:


ser1


# In[7]:


# how to drop an index
ser1.drop('b')


# In[11]:


# how it works with a dataframe

dframe1 = DataFrame(np.arange(9).reshape((3,3)), index=['SF','LA','NY'], columns=['pop', 'size', 'year'])


# In[12]:


dframe1


# In[14]:


# drop a row
dframe1.drop('LA')


# In[16]:


# To make it permanent save it into another datafram
dframe2 = dframe1.drop('LA')


# In[17]:


dframe2


# In[19]:


# Drop a column
dframe1.drop('year', axis=1)


# In[ ]:




