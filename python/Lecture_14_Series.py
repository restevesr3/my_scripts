
# coding: utf-8

# # Lecture 14 - Series

# ## Robert Esteves

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from pandas import Series, DataFrame


# In[4]:


obj = Series([3,6,9,12])


# In[5]:


obj


# In[6]:


obj.values


# In[7]:


obj.index


# In[12]:


ww2_cas = Series([8700000, 4300000, 3000000, 2100000, 400000], index=['USSR','Germany', 'China', 'Japan', 'USA'])


# In[13]:


ww2_cas


# In[14]:


ww2_cas['USA']


# In[15]:


# Check which countries had casualties greater than 4 million
ww2_cas[ww2_cas > 4000000]


# In[16]:


# We can treat a series like an ordered dictionary
'USSR' in ww2_cas


# In[17]:


# How to convert a series into a dictionary
ww2_dict = ww2_cas.to_dict()


# In[18]:


ww2_dict


# In[19]:


# how to convert back to a series
ww2_series = Series(ww2_dict)


# In[20]:


ww2_series


# In[24]:


countries = ['China', 'Germany', 'Japan', 'USA', 'USSR', 'Argentina']


# In[25]:


# Set the index to come from the list
obj2 = Series(ww2_dict, index = countries)


# In[26]:


obj2


# In[27]:


pd.isnull(obj2)


# In[28]:


pd.notnull(obj2)


# In[30]:


ww2_series


# In[31]:


# Add series to a series
obj2


# In[32]:


ww2_series + obj2


# In[33]:


# How to name a series
obj2.name = 'World War 2 Casualties'


# In[34]:


obj2


# In[35]:


# How to name the index
obj2.index.name = 'Countries'


# In[36]:


obj2


# In[ ]:




