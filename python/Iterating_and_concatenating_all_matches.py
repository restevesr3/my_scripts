
# coding: utf-8

# # Iterating and concatenating all matches

# In[1]:

import pandas as pd


# In[2]:

import glob


# In[3]:

pwd


# In[4]:

search_pattern = 'Datasets/132719078_T_T100D_MARKET_US_CARRIER_ONLY_????.csv'


# In[5]:

csv_files = glob.glob(search_pattern)


# In[6]:

csv_files


# In[9]:

frames = []


# In[10]:

for csv in csv_files:
    df = pd.read_csv(csv, low_memory=False)
    frames.append(df)


# In[11]:

# frames


# In[12]:

on_time_data = pd.concat(frames)


# In[13]:

on_time_data.shape


# In[14]:

on_time_data.dtypes


# In[15]:

on_time_data.info()


# In[ ]:



