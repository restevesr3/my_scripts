
# coding: utf-8

# # Lecture 26 - JSON with Python

# ## Robert Esteves

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from pandas import Series, DataFrame


# In[4]:


import sys


# In[7]:


import json


# In[5]:


json_obj = """
{
"zoo_animal": "Lion",
"food":["Meat", "Veggies", "Honey"],
"fur":"Golden",
"clothes":null,
"diet":[{"zoo_animal":"Gazelle","food":"grass", "fur":"Brown"}]
}
"""


# In[6]:


json_obj


# In[9]:


data = json.loads(json_obj)


# In[10]:


data


# In[11]:


dframe = DataFrame(data['diet'])


# In[12]:


dframe


# In[ ]:




