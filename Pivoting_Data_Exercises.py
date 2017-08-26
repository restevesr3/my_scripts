
# coding: utf-8

# # Pivoting Data Exercises
# ### Robert Esteves
# ### 8/26/2017
# ### Notes using pandas.pivot method

# In[1]:

import pandas as pd


# In[2]:

url = '/datasets/airquality.csv'


# In[3]:

air_quality = pd.read_csv(url)


# In[4]:

air_quality.shape


# In[5]:

air_quality.columns


# In[14]:

# Assumptions:
# Given a data set that is already melted (analysis friendly format) pivot the data
# so the report is presented in a tidy format (reporting friendly format)

airquality_melt = pd.melt(frame=air_quality, id_vars = ['Month', 'Day']
                         ,var_name=['Measurements']
                          ,value_name = 'Readings'
                         )


# In[16]:

airquality_melt.head()


# In[18]:

# The pivot_table is used because we have duplicate entries in the data set for each 
# Specific Month and Day
airquality_pivot = airquality_melt.pivot_table(index = ['Month', 'Day'], 
                                         columns = 'Measurements',
                                         values = 'Readings'
                                        
                                        )


# In[19]:

airquality_pivot.head()


# ## Resetting the index of a DataFrame

# In[20]:

airquality_pivot = airquality_pivot.reset_index()


# In[24]:

airquality_pivot.index


# In[22]:

airquality_pivot.head()


# ## Pivoting Duplicate values

# In[ ]:



