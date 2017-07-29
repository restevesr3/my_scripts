
# coding: utf-8

# # Lecture 19 - Selecting Entries

# ## Robert Esteves

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from pandas import Series, DataFrame


# In[4]:


ser1 = Series(np.arange(3), index=['a', 'b', 'c'])


# In[5]:


ser1


# In[6]:


ser1 = 2 * ser1


# In[7]:


ser1


# In[8]:


# grab entries by the index
ser1['b']


# In[10]:


# grab index by the numerical index of the entry
ser1[1]


# In[11]:


#grab by a range
ser1[0:3]


# In[13]:


# grab data by index range
ser1[['a', 'b']]


# In[14]:


# Grab by logic
ser1[ser1 > 3]


# In[15]:


# set values
ser1[ser1>3]=10


# In[16]:


ser1


# In[17]:


# How it works in a dataframe
dframe = DataFrame(np.arange(25).reshape(5,5), index=['NYC', 'LA','SF', 'DC', 'CHI'],
                  columns=['A', 'B', 'C', 'D', 'E']
                  )


# In[18]:


dframe


# In[19]:


# Select by column name
dframe['B']


# In[20]:


dframe[['B', 'E']]


# In[21]:


# Boolean logic
dframe[dframe['C']>8]


# In[22]:


# Show a boolean dataframe
dframe > 10


# In[23]:


# use ix to lable and index
dframe.ix['LA']


# In[24]:


dframe.ix[1]


# In[ ]:




