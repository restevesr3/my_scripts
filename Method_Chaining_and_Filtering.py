
# coding: utf-8

# ## Method chaining and filtering
# 
# ### We've seen that pandas supports method chaining. This technique can be very powerful when cleaning and filtering data.
# 
# ### In this exercise, a DataFrame containing flight departure data for a single airline and a single airport for the month of July 2015 has been pre-loaded. Your job is to use .str() filtering and method chaining to generate summary statistics on flight delays each day to Dallas.

# In[1]:

import pandas as pd


# In[57]:

df = pd.read_table('F:/Datasets/flight_departures.txt'
                   , sep=','
                   # , nrows = 10
                   , skiprows = 15
                  ,date_parser = True)


# In[58]:

df.head()


# In[59]:

df.shape


# In[60]:

df.columns


# In[61]:

# Stript extra whitespace from the column names: df.columns
df.columns = df.columns.str.strip()


# In[62]:

df.columns


# In[63]:

df.info()


# In[66]:

df['Date (MM/DD/YYYY)'] = pd.to_datetime(df['Date (MM/DD/YYYY)'])


# In[67]:

df.info()


# In[68]:

df.set_index('Date (MM/DD/YYYY)', inplace=True)


# In[69]:

df.head()


# In[70]:

# Extract data for which the destination airport is Dallas: dallas
dallas = df['Destination Airport'].str.contains('DAL')


# In[71]:

dallas.head()


# In[72]:

# Compute the total number of Dallas departures each day: daily_departures
daily_departures = dallas.resample('D').sum()


# In[73]:

# Generate the summary statistics for daily Dallas Departures: stats
stats = daily_departures.describe()


# In[74]:

stats


# In[ ]:



