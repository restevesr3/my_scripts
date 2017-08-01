
# coding: utf-8

# # Lecture 22 - Summary Statistics

# ## Robert Esteves

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from pandas import Series, DataFrame


# In[4]:


arr = np.array([[1,2, np.nan], [np.nan, 3, 4]])


# In[5]:


dframe1 = DataFrame(arr, index=['A', 'B'], columns=['One', 'Two', 'Three'])


# In[6]:


dframe1


# In[7]:


# sum functions ignores the null values
dframe1.sum()


# In[8]:


dframe1.sum(axis=1)


# In[9]:


dframe1.min()


# In[10]:


dframe1.min(axis=1)


# In[11]:


# minium index
dframe1.idxmin()


# In[12]:


dframe1


# In[13]:


dframe1.cumsum()


# In[14]:


dframe1.describe()


# In[15]:


from IPython.display import YouTubeVideo


# In[16]:


YouTubeVideo('xGbpuFNR1ME')


# In[17]:


YouTubeVideo('4EXNedimDMs')


# In[22]:


import pandas_datareader as pdr


# In[23]:


# import pandas.io.data as pdweb  --old way
# new way

from pandas_datareader import data, wb


# In[24]:


import datetime


# In[27]:


cvx = pdr.get_data_google('CVX')


# In[28]:


xom = pdr.get_data_google('XOM')


# In[29]:


bp = pdr.get_data_google('BP')


# In[25]:


#prices = pdr.get_data_yahoo(['CVX', 'XOM', 'BP'], start=datetime.datetime(2010,1,1),
#                             end = datetime.datetime(2013,1,1))['Adj Close']


# In[31]:


cvx['Symbol']='CVX'


# In[32]:


cvx.head()


# In[33]:


xom['Symbol']='XOM'


# In[35]:


xom.head()


# In[34]:


bp['Symbol']='BP'


# In[36]:


bp.head()


# In[37]:


xom['Close']


# In[47]:


xom_close_ser  = xom[xom.columns[3]]


# In[48]:


xom_close_ser.head()


# In[50]:


cvx_close_ser = cvx[cvx.columns[3]]


# In[52]:


bp_close_ser = bp[bp.columns[3]]


# In[53]:


prices = DataFrame({'XOM':xom_close_ser, 'CVX':cvx_close_ser, 'BP':bp_close_ser})


# In[54]:


prices


# In[55]:


rets = prices.pct_change()


# In[56]:


# Correlation of the stocks
corr = rets.corr


# In[57]:


get_ipython().magic('matplotlib inline')


# In[58]:


prices.plot()


# In[59]:


import seaborn as sns


# In[60]:


import matplotlib.pyplot as plt


# In[62]:


from seaborn.linearmodels import corrplot


# In[64]:


corrplot(rets, annotation=False, diag_names=False)


# In[66]:


ser1 = Series(['w', 'w','x', 'y', 'z', 'w', 'x', 'a'])


# In[67]:


ser1


# In[68]:


ser1.unique()


# In[69]:


ser1.value_counts()


# In[ ]:




