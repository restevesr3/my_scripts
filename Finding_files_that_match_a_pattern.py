
# coding: utf-8

# # Finding files that match a pattern

# In[1]:

import pandas as pd


# In[2]:

import glob


# In[3]:

pwd


# In[4]:

#F:/Virtual_NAS_Drive/Datasets/132719078_T_T100D_MARKET_US_CARRIER_ONLY_2014.csv
# replace the year with question marks (?) to search for the individual years
pattern = 'Datasets/132719078_T_T100D_MARKET_US_CARRIER_ONLY_????.csv'


# In[5]:

csv_files = glob.glob(pattern)


# In[6]:

csv_files


# In[7]:

csv_files[2]


# In[9]:

f_2015 = pd.read_csv(csv_files[1], low_memory=False)


# In[10]:

f_2015.shape


# In[ ]:



