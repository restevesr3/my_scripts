
# coding: utf-8

# # Resample and roll with it
# 
# ### As of pandas version 0.18.0, the interface for applying rolling transformations to time series has become more consistent and flexible, and feels somewhat like a groupby (If you do not know what a groupby is, don't worry, you will learn about it in the next course!).
# 
# ### You can now more flexibly chain together both resampling as well as rolling operations. In this exercise, the same weather data from the previous exercises has been pre-loaded for you. Your job is to extract one month of data, resample to find the daily high temperatures, and then use a rolling and aggregation operation to smooth the data.

# In[1]:

import pandas as pd


# In[2]:

import numpy as np


# In[25]:

import matplotlib.pyplot as plt


# In[4]:

date = pd.date_range(start='2010-01-01', end='2010-12-31', freq='H')


# In[6]:

len(date)


# In[7]:

temp = np.random.randint(40, 100, 8737) * 1.03


# In[8]:

len(temp)


# In[9]:

dew_point = np.random.randint(30, 40, 8737) * 1.04


# In[10]:

x = pd.Series([1.0])


# In[11]:

pressure = x.repeat(8737)


# In[12]:

df = pd.DataFrame({'Date':date, 'Temperature':temp, 'DewPoint':dew_point, 'Pressure':pressure})


# In[13]:

df.head()


# In[14]:

df.set_index('Date', inplace=True)


# In[15]:

df.head()


# In[16]:

df.tail()


# In[17]:

df['Temperature'].describe()


# In[19]:

# Extract the August 2010 data: august
august = df['Temperature']['2010-08']


# In[20]:

august


# In[21]:

# Resample to daily data, aggregating by max: daily_highs
daily_highs = august.resample('D').max()


# In[22]:

daily_highs


# In[27]:

# Use a rolling 7-day window with method chaining to smooth the daily high temperatures in August
daily_highs_smoothed = august.resample('D').max().rolling(window = 7).mean()
daily_highs_smoothed


# In[28]:

# Plot the daily_hights_smoothed
daily_highs_smoothed.plot()
plt.show()


# In[ ]:



