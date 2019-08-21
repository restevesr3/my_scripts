
# coding: utf-8

# # Data Cleaning-Ebola Data Set Using the split and get methods
# #### Robert Esteves
# #### 8/26/2017
# #### Notes: Using pandas.melt method and the split and get string methods

# In[2]:

import pandas as pd


# In[3]:

url = '~/datasets/ebola.csv'


# In[4]:

ebola = pd.read_csv(url)


# In[5]:

ebola.shape


# In[6]:

ebola.columns


# In[7]:

ebola.head()


# In[14]:

ebola_melt = pd.melt(frame = ebola, 
                     id_vars=['Date', 'Day'],
                     var_name = 'type_country',
                     value_name = 'counts'
                    )


# In[15]:

ebola_melt.head()


# In[16]:

ebola_melt['str_split'] = ebola_melt['type_country'].str.split('_')


# In[17]:

ebola_melt.head()


# In[18]:

ebola_melt['type']= ebola_melt['str_split'].str.get(0)


# In[19]:

ebola_melt.head()


# In[20]:

ebola_melt['country'] = ebola_melt['str_split'].str.get(1)


# In[21]:

ebola_melt.head()


# In[ ]:



