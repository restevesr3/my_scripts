
# coding: utf-8

# # Lecture 27 - HTML with Python

# ## Robert Esteves

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from pandas import Series, DataFrame


# In[4]:


import sys


# In[5]:


from pandas import read_html


# In[6]:


from bs4  import BeautifulSoup # import beautiful soup 4


# In[7]:


import html5lib


# In[8]:


# failed bank list
url = 'http://www.fdic.gov/bank/individual/failed/banklist.html'


# In[9]:


# pip install beautifulsoup4
# pip install html5lib
# Downloaded #83b409a, run pip install -r requirements.txt, I'm getting the error:

# bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
# Solution:

# apt-get install libxslt1-dev libxml2 python-dev
# pip install --upgrade lxml


# In[10]:


dframe_list = pd.io.html.read_html(url)


# In[11]:


dframe = dframe_list[0]


# In[12]:


dframe


# In[14]:


dframe.columns.values


# In[15]:


dframe.columns


# In[16]:


dframe.axes


# In[ ]:




