
# coding: utf-8

# # Pandas Data Merge Many-to-1 Join

# In[1]:

import pandas as pd


# In[2]:

import glob


# In[3]:

search_pattern = 'Datasets/north_pole_research_*.csv'


# In[4]:

search_pattern


# In[6]:

csv_files = glob.glob(search_pattern)


# In[7]:

sites = pd.read_csv(csv_files[0], sep='|')


# In[8]:

sites


# In[9]:

visited = pd.read_csv(csv_files[1], sep='|')


# In[10]:

visited


# In[11]:

m2o = pd.merge(left=sites, right=visited, left_on='name', right_on='site')


# In[12]:

m2o


# In[ ]:



