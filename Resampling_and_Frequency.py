
# coding: utf-8

# # Resampling and frequency

# ### Resampling and frequency
# 
# ### Pandas provides methods for resampling time series data. When downsampling or upsampling, the syntax is similar, but the methods called are different. Both use the concept of 'method chaining' - df.method1().method2().method3() - to direct the output from one method call to the input of the next, and so on, as a sequence of operations, one feeding into the next.
# 
# ### For example, if you have hourly data, and just need daily data, pandas will not guess how to throw out the 23 of 24 points. You must specify this in the method. One approach, for instance, could be to take the mean, as in df.resample('D').mean().
# 
# ### In this exercise, a data set containing hourly temperature data has been pre-loaded for you. Your job is to resample the data using a variety of aggregation methods to answer a few questions

# In[1]:

import pandas as pd


# In[2]:

import numpy as np


# In[3]:

dates = pd.date_range(start='2010-01-01', end='2010-12-31', freq='H')


# In[4]:

dates


# In[6]:

len(dates)


# In[15]:

temp = np.random.randint(40, 50, 8737) * 1.03


# In[17]:

dew_point = np.random.randint(30, 40, 8737) * 1.04


# In[21]:

x=pd.Series([1.0])


# In[22]:

x


# In[25]:

pressure = x.repeat(8737)#Pandas repeat function


# In[27]:

df = pd.DataFrame({'Date':dates, 'temperature':temp, 'DewPoint':dew_point, 'Pressure': pressure})


# In[28]:

df.head()


# In[29]:

df.set_index('Date', inplace=True)


# In[30]:

df.head()


# In[37]:

# Downsample to 6 hour data and aggregate by mean: df1
df1 = df['temperature'].resample('6h').mean()


# In[38]:

df1.head()


# In[35]:

# Downsample to daily data and count the number of data points: df2
df2 = df['temperature'].resample('D').count()


# In[36]:

df2.head()


# In[ ]:



