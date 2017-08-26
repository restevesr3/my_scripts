
# coding: utf-8

# # Melting Data
# ### Robert Esteves
# ### 8/26/2017
# ### Notes: How to use the pandas melt method

# In[2]:

import pandas as pd


# In[3]:

url = '/datasets/airquality.csv'


# In[4]:

airquality = pd.read_csv(url)


# In[5]:

airquality.shape


# In[6]:

airquality.columns


# In[7]:

airquality.info()


# In[8]:

# Melt based on the columns that you "do not want melt"
airquality_melt = pd.melt(frame=airquality, id_vars=['Month', 'Day'])


# In[25]:

airquality_melt.head()


# In[23]:

# Melt using specific columns and renaming the variable header to "measurements"
air_quality_melt_v2 = pd.melt(frame=airquality, 
                              id_vars = ['Month', 'Day'],
                              value_vars=['Ozone', 'Solar.R', 'Wind', 'Temp'],
                               var_name='measurements'
                             )


# In[24]:

air_quality_melt_v2.head()


# In[20]:

# This version renames the variable and the value headers
air_quality_melt_v3 = pd.melt(frame = airquality,
                             id_vars = ['Month', 'Day'],
                             value_vars = ['Ozone', 'Solar.R', 'Wind', 'Temp'],
                              var_name = 'measurements',
                              value_name = 'reading'
                             )


# In[22]:

air_quality_melt_v3.head()


# In[ ]:



