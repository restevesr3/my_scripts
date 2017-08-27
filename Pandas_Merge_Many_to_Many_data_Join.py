
# coding: utf-8

# # Pandas Merge Many-to-Many Join

# In[2]:

import pandas as pd


# In[3]:

import glob


# In[4]:

search_pattern = 'Datasets/north_pole_research_*.csv'


# In[5]:

search_pattern


# In[6]:

csv_files = glob.glob(search_pattern)


# In[7]:

csv_files


# In[8]:

site = pd.read_csv(csv_files[0], sep='|')


# In[9]:

visited = pd.read_csv(csv_files[2], sep='|')


# In[11]:

survey = pd.read_csv(csv_files[1], sep='|')


# In[12]:

m2m = pd.merge(left=site, right=visited, left_on='name', right_on='site')


# In[13]:

m2m


# In[14]:

m2m = pd.merge(left=m2m, right=survey, left_on='id', right_on = 'taken')


# In[15]:

m2m


# In[ ]:



