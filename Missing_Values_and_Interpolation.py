
# coding: utf-8

# ## Missing values and interpolation
# 
# ### One common application of interpolation in data analysis is to fill in missing data.
# 
# ### In this exercise, noisy measured data that has some dropped or otherwise missing values has been loaded. The goal is to compare two time series, and then look at summary statistics of the differences. The problem is that one of the data sets is missing data at some of the times. The pre-loaded data ts1 has value for all times, yet the data set ts2 does not: it is missing data for the weekends.
# 
# ### Your job is to first interpolate to fill in the data for all days. Then, compute the differences between the two data sets, now that they both have full support for all times. Finally, generate the summary statistics that describe the distribution of differences.

# In[1]:

import pandas as pd


# In[2]:

import numpy as np


# In[4]:

ts_1_dates = pd.date_range(start='2016-07-01', periods=17)


# In[18]:

ds_1 = np.arange(17)


# In[19]:

ds_1


# In[13]:

print(ts_1_dates)


# In[20]:

ts1 = pd.Series(ds_1, index = ts_1_dates)


# In[21]:

ts1


# In[22]:

x = ['2016-07-01', '2016-07-04', '2016-07-05', '2016-07-06', '2016-07-07', '2016-07-08', '2016-07-11', '2016-07-12',
    '2016-07-13', '2016-07-14', '2016-07-15'
    ]


# In[23]:

x


# In[24]:

ds_2 = np.arange(11)


# In[25]:

ds_2


# In[26]:

ts_2_dates = pd.to_datetime(x)


# In[27]:

ts_2_dates


# In[28]:

ts2 = pd.Series(ds_2, index=ts_2_dates)


# In[29]:

ts2


# In[33]:

# Reset the index of ts2 to ts1, and then use linear interpolation to fill the NaNs: ts2_interp
ts2.reindex(ts_1_dates)


# In[39]:

# this example uses the index function of the ts1 series. This is a better alternative, because you don't have to 
# recreate the index as a separate object
ts2.reindex(ts1.index)


# In[40]:

# Reset the index of ts2 to ts1, and then use linear interpolation to fill the NaNs: ts2_interp
ts2_interp = ts2.reindex(ts1.index).interpolate(how='linear')


# In[41]:

ts2_interp


# In[47]:

# Compute the absolute difference of ts1 and ts_2interp: differences
differences = np.abs(ts2_interp - ts1)


# In[48]:

differences


# In[49]:

# Generate and print summary statistics of the differences
differences.describe()


# In[ ]:



