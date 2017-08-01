
# coding: utf-8

# # Lecture 23 - Missing Data

# ## Robert Esteves

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from pandas import Series, DataFrame


# In[4]:


data = Series(['one', 'two', np.nan, 'four'])


# In[5]:


data


# In[6]:


data.isnull()


# In[7]:


data.dropna()


# In[15]:


dframe = DataFrame([[1,2,3],[np.nan,5,6],[7,np.nan,9], [np.nan, np.nan, np.nan]    ])


# In[16]:


dframe


# In[17]:


# This command will drop all rows with any missing data
clean_dframe = dframe.dropna()


# In[18]:


clean_dframe


# In[19]:


# drops all rows where all the cells are missing data
dframe.dropna(how='all')


# In[20]:


#drop columns
dframe.dropna(axis=1)


# In[25]:


npn = np.nan

dframe2 = DataFrame([[1,2,3,npn], [2,npn,5,6],[npn,7,npn,9],[1,npn,npn,npn]])


# In[26]:


dframe2


# In[27]:


# Set the threshold for requested data
dframe2.dropna(thresh=2)


# In[28]:


dframe2.dropna(thresh=3)


# In[29]:


dframe2


# In[30]:


# fill the null values
# use the fillna method

dframe2.fillna(1)


# In[31]:


# fill nulls with different values
dframe2.fillna({0:0, 1:1, 2:2, 3:3})


# In[33]:


# modify the existing object
#dframe2 = dfram2.fillna()
#or
# modify in place
dframe2.fillna(0, inplace=True)


# In[34]:


dframe2


# In[ ]:




