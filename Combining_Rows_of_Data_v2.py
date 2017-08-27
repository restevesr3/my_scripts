
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

flight_2014 = 'Datasets/132719078_T_T100D_MARKET_US_CARRIER_ONLY_2014.csv'


# In[7]:

flight_2015 = 'Datasets/132719078_T_T100D_MARKET_US_CARRIER_ONLY_2015.csv'


# In[5]:

f_2014 = pd.read_csv(flight_2014,
                    low_memory=False)


# In[8]:

f_2015 =pd.read_csv(flight_2015,
                   low_memory=False
                   )


# In[9]:

f_2014.shape


# In[10]:

f_2015.shape


# In[11]:

flights = pd.concat([f_2014, f_2015])


# In[12]:

flights.shape


# In[ ]:



