
# coding: utf-8

# ## Rolling mean and frequency
# 
# ### In this exercise, some hourly weather data is pre-loaded for you. You will continue to practice resampling, this time using rolling means.
# 
# ### Rolling means (or moving averages) are generally used to smooth out short-term fluctuations in time series data and highlight long-term trends. You can read more about them here.
# 
# ### To use the .rolling() method, you must always use method chaining, first calling .rolling() and then chaining an aggregation method after it. For example, with a Series hourly_data, hourly_data.rolling(window=24).mean() would compute new values for each hourly point, based on a 24-hour window stretching out behind each point. The frequency of the output data is the same: it is still hourly. Such an operation is useful for smoothing time series data.
# 
# ### Your job is to resample the data using the combination of .rolling() and .mean(). You will work with the same DataFrame df from the previous exercise.

# In[1]:

import pandas as pd


# In[2]:

import numpy as np


# In[33]:

import matplotlib.pyplot as plt


# In[4]:

dates = pd.date_range(start='2010-01-01', end='2010-12-31', freq='H')


# In[5]:

len(dates)


# In[6]:

temp = np.random.randint(40, 100, 8737)* 1.03


# In[7]:

temp.min()


# In[8]:

temp.max()


# In[10]:

dew_point = np.random.randint(30, 40, 8737) * 1.04


# In[11]:

dew_point.min()


# In[12]:

dew_point.max()


# In[14]:

x = pd.Series([1.0])


# In[16]:

pressure = x.repeat(8737)


# In[18]:

len(pressure)


# In[20]:

df = pd.DataFrame({'Date':dates, 'Temperature':temp, 'DewPoint':dew_point, 'Pressure':pressure})


# In[22]:

df.head()


# In[24]:

df.set_index('Date', inplace=True)


# In[25]:

df.head()


# In[26]:

df.tail()


# In[28]:

# Extract data from 2010-Aug-01 to 2010-Aug-15: unsmoothed
unsmoothed = df['Temperature']['2010-08-01': '2010-08-15']


# In[29]:

unsmoothed.head()


# In[30]:

# Apply a rolling mean with a 24 hour window: smoothed
smoothed = unsmoothed.rolling(window=24).mean()


# In[31]:

smoothed


# In[32]:

# Create a new DataFrame with columns smoothed and unsmoothed: august
august = pd.DataFrame({'smoothed':smoothed, 'unsmoothed':unsmoothed})


# In[34]:

# Plot both smoothed and unsmoothed data using august.plot()
august.plot()
plt.show()


# In[ ]:



