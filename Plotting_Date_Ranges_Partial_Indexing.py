
# coding: utf-8

# ## Plotting date ranges, partial indexing
# 
# 
# ### Now that you have set the DatetimeIndex in your DataFrame, you have a much more powerful and flexible set of tools to use when plotting your time series data. Of these, one of the most convenient is partial string indexing and slicing. In this exercise, we've pre-loaded a full year of Austin 2010 weather data, with the index set to be the datetime parsed 'Date' column as shown in the previous exercise.
# 
# ### Your job is to use partial string indexing of the dates, in a variety of datetime string formats, to plot all the summer data and just one week of data together. After you are done, you can cycle between the two plots by clicking on the 'Previous Plot' and 'Next Plot' buttons.
# 
# ### First, remind yourself how to extract one month of temperature data using 'May 2010' as a key into df.Temperature[], and call head() to inspect the result: df.Temperature['May 2010'].head()

# In[1]:

import pandas as pd


# In[2]:

import numpy as np


# In[3]:

from matplotlib import pyplot as plt


# In[4]:

Date = pd.date_range(start='2010-01-01', end='2010-12-31', freq='H')


# In[5]:

Date


# In[6]:

temp = np.random.randint(40, 50, 8737) * 1.03


# In[7]:

dew_point = np.random.randint(30, 40, 8737) * 1.04


# In[8]:

x = pd.Series([1.0])


# In[9]:

pressure = x.repeat(8737)


# In[13]:

df = pd.DataFrame({'Date':Date, 'DewPoint':dew_point, 'Temperature':temp, 'Pressure':pressure})


# In[14]:

df.head()


# In[17]:

df['Date'] = pd.to_datetime(df['Date'])


# In[18]:

df.head()


# In[19]:

df.set_index('Date', inplace=True)


# In[20]:

df.head()


# In[33]:

# Plot the Summer data
df.Temperature['2010-06':'2010-08'].plot()
plt.show()
plt.clf()


# In[36]:

df.Temperature['2010-06-10':'2010-06-17'].plot()
plt.show()
plt.clf()


# In[ ]:



