
# coding: utf-8

# #  Data Cleaning-Tuberculosis Data Set
# ### Robert Esteves
# ### 8/26/2017
# #### Notes:  Using pandas.melt method

# In[1]:

import pandas as pd


# In[2]:

url = '/datasets/tb.csv'


# In[3]:

tb = pd.read_csv(url)


# In[4]:

tb.shape


# In[5]:

tb.columns


# In[6]:

tb.head()


# In[21]:

tb_melt = pd.melt(frame = tb, id_vars =['country', 'year'],
                 var_name = 'measurement',
                 value_name = 'reading'
                 )


# In[22]:

tb_melt.head()


# In[23]:

tb_melt['sex'] = tb_melt['measurement'].str[0]


# In[25]:

tb_melt.head()


# In[27]:

tb_melt['age_group'] = tb_melt['measurement'].str[1:]


# In[29]:

tb_melt.head()


# In[ ]:



