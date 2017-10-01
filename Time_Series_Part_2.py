
# coding: utf-8

# # Time Series Part 2

# In[1]:

import pandas as pd


# In[2]:

import numpy as np


# In[10]:

import datetime


# # Reindexing the Index
# 
# #### Reindexing is useful in preparation for adding or otherwise combining two time series data sets. To reindex the data, we provide a new index and ask pandas to try and match the old data to the new index. If data is unavailable for one of the new index dates or times, you must tell pandas how to fill it in. Otherwise, pandas will fill with NaN by default.
# 
# #### In this exercise, two time series data sets containing daily data have been pre-loaded for you, each indexed by dates. The first, ts1, includes weekends, but the second, ts2, does not. The goal is to combine the two data sets in a sensible way. Your job is to reindex the second data set so that it has weekends as well, and then add it to the first. When you are done, it would be informative to inspect your results.

# In[3]:

dates = pd.date_range(start = '2017-01-01', end = '2017-01-31')


# In[4]:

dates


# In[5]:

type(dates)


# In[6]:

dates_df = pd.DataFrame({'dates':dates}) #Create date variable using a dictionary


# In[8]:

dates_df.head()


# In[14]:

dates_df['week_day_name']= dates_df['dates'].dt.weekday_name


# In[15]:

dates_df.head()


# ### https://stackoverflow.com/questions/17071871/select-rows-from-a-dataframe-based-on-values-in-a-column-in-pandas

# In[24]:

dates_df.loc[dates_df['week_day_name'].isin(['Sunday', 'Saturday']) ]


# In[28]:

dates_df['temp'] = np.random.randint(50, 60, 31)


# In[30]:

dates_df.head()


# In[34]:

dates_df.set_index('dates', inplace = True)


# In[36]:

dates_df.head()


# In[38]:

dates_df.loc[dates_df['week_day_name'].isin(['Saturday', 'Sunday'])]


# In[39]:

ts_1 = dates_df.loc[dates_df['week_day_name'].isin(['Saturday', 'Sunday'])]


# In[40]:

ts_1


# #### https://stackoverflow.com/questions/19960077/how-to-implement-in-and-not-in-for-pandas-dataframe

# In[44]:

ts_2 = dates_df.loc[dates_df['week_day_name'].isin(['Saturday', 'Sunday'])==False]


# In[45]:

ts_2


# In[ ]:



