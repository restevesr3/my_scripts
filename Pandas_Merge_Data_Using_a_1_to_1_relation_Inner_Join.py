
# coding: utf-8

# # Pandas Merge Data Using a 1 to 1 relation (Inner Join)

# In[7]:

import pandas as pd


# In[8]:

import glob


# In[9]:

search_pattern = 'Datasets/north_pole_research_*.csv'


# In[10]:

search_pattern


# In[11]:

csv_files = glob.glob(search_pattern)


# In[12]:

csv_files


# In[15]:

sites = pd.read_csv(csv_files[0], sep='|')


# In[16]:

sites


# In[17]:

visited = pd.read_csv(csv_files[1], sep = '|')


# In[18]:

visited


# In[20]:

o2o = pd.merge(left = sites,
               right = visited,
               left_on = 'name',
               right_on = 'site'
              
              )


# In[21]:

o2o


# In[ ]:



