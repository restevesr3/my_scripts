
# coding: utf-8

# ## Separating and resampling
# 
# ### With pandas, you can resample in different ways on different subsets of your data. For example, resampling different months of data with different aggregations. In this exercise, the data set containing hourly temperature data from the last exercise has been pre-loaded.
# 
# ### Your job is to resample the data using a variety of aggregation methods. The DataFrame is available in the workspace as df. You will be working with the 'Temperature' column

# In[1]:

import pandas as pd


# In[2]:

import numpy as np


# In[3]:

date = pd.date_range(start='2010-01-01', end='2010-12-31', freq='H')


# In[4]:

len(date)


# In[5]:

temp = np.random.randint(40, 50, 8737) * 1.03


# In[6]:

len(temp)


# In[7]:

dew_point = np.random.randint(30, 40, 8737) * 1.04


# In[9]:

x = pd.Series([1.0])


# In[11]:

pressure = x.repeat(8737)


# In[13]:

df = pd.DataFrame({'Date':date, 'Temperature':temp, 'DewPoint':dew_point, 'Pressure':pressure})


# In[14]:

df.set_index('Date', inplace=True)


# In[15]:

df.head()


# In[16]:

df.tail()


# In[30]:

# Extract temperature data for August: august
august = df['Temperature'].loc['2010-08']


# In[31]:

august.head()


# In[32]:

# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('D').max()


# In[33]:

august_highs.head()


# In[34]:

# Extract temperature data for February: february
february = df['Temperature'].loc['2010-02']


# In[35]:

# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('D').min()


# In[36]:

february.head()


# In[ ]:



