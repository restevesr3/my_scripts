
# coding: utf-8

# # Lecture 20 - Data Alignment

# ## Robert Esteves

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# In[3]:


from pandas import Series, DataFrame


# In[4]:


ser1 = Series([0,1,2], index=['A', 'B', 'C'])


# In[5]:


ser1


# In[7]:


ser2 = Series([3,4,5,6], index=['A', 'B', 'C', 'D'])


# In[8]:


ser2


# In[9]:


# Add the two series together
ser1 + ser2


# In[12]:


# Let's try it with DataFrames
dframe1 = DataFrame(np.arange(4).reshape((2,2)), columns=list('AB'), index=['NYC', 'LA'])


# In[13]:


dframe1


# In[17]:


dframe2 = DataFrame(np.arange(9).reshape((3,3,)), columns=list('ADC'), index=['NYC', 'SF', 'LA'])


# In[18]:


dframe2


# In[19]:


dframe1 + dframe2


# In[20]:


# Replace the NULL FLAGS
dframe1.add(dframe2,fill_value=0)


# In[21]:


dframe2


# In[22]:


ser3 = dframe2.ix[0]


# In[23]:


ser3


# In[25]:


dframe2 - ser3


# In[ ]:




