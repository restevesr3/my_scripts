
# coding: utf-8

# ## Time zones and conversion
# 
# ### Time zone handling with pandas typically assumes that you are handling the Index of the Series. In this exercise, you will learn how to handle timezones that are associated with datetimes in the column data, and not just the Index.
# 
# ### You will work with the flight departure dataset again, and this time you will select Los Angeles ('LAX') as the destination airport.
# 
# ### Here we will use a mask to ensure that we only compute on data we actually want. To learn more about Boolean masks, click here!

# In[1]:

import pandas as pd


# In[2]:

import numpy as np


# In[7]:

df = pd.read_csv('F:/Datasets/austin_airport_departure_data_2015_july.csv',
                sep=',',
                # nrows = 10,
                skiprows = 15
                )


# In[8]:

df.shape


# In[9]:

df.columns


# In[10]:

df.columns.str.strip()


# In[11]:

df.columns


# In[12]:

df.columns = df.columns.str.strip()


# In[13]:

df.columns


# In[14]:

df.head()


# In[18]:

# Buid a Boolean mask to filter out all the 'LAX' departure flights: mask
mask = df['Destination Airport']=='LAX'


# In[19]:

# Use the mask to subset the data: la
la = df[mask]


# In[20]:

la


# In[22]:

# Combine two columns of data to create a datetime series: times_tz_none
times_tz_none = pd.to_datetime(df['Date (MM/DD/YYYY)'] + ' '+ df['Wheels-off Time'])


# In[23]:

times_tz_none


# In[25]:

# Localize the time to US/Central: times_tz_central
times_tz_central = times_tz_none.dt.tz_localize('US/Central')


# In[26]:

times_tz_central


# In[28]:

# Convert the datetimes from US/Central to US/Pacific
times_tz_pacific = times_tz_central.dt.tz_convert('US/Pacific')


# In[29]:

time_zones_df = pd.DataFrame({'no_time_zone':times_tz_none,
                             'times_tz_central': times_tz_central,
                              'times_tz_pacific': times_tz_pacific
                             })


# In[30]:

time_zones_df.head()


# In[ ]:



