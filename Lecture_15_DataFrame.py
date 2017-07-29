
# coding: utf-8

# # Lecture 15 - DataFrame

# ## Robert Esteves

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


from pandas import Series, DataFrame


# In[4]:


import webbrowser


# In[5]:


website_url = 'http://en.wikipedia.org/wiki/NFL_win-loss_records'


# In[6]:


webbrowser.open(website_url)


# In[10]:


nfl_frame = pd.read_clipboard()


# In[11]:


nfl_frame


# In[12]:


nfl_frame.info()


# In[13]:


nfl_frame.columns


# In[14]:


nfl_frame['Team ']


# In[15]:


# Retrieve columns
DataFrame(nfl_frame, columns=['Team ', 'First NFL Season ', 'Total Games '])


# In[16]:


# Retrieve rows from from a DataFrame
nlf_frame.ix[3]


# In[18]:


# Assign values to an entire data frame
nfl_frame['Stadium'] = "Levi's Stadium"


# In[19]:


nfl_frame


# In[20]:


nfl_frame['Stadium']= np.arange(5)


# In[21]:


nfl_frame


# In[24]:


# Add a Series to a data frame
stadiums = Series(["Levi's Stadium", "AT&T Stadium"], index=[4,0])


# In[25]:


stadiums


# In[26]:


nfl_frame['Stadium'] = stadiums


# In[27]:


nfl_frame


# In[28]:


# Delete entire column

del nfl_frame['Stadium']


# In[29]:


nfl_frame


# In[30]:


# Construct a dataframe from a dictionary
data = {'City':['SF', 'LA', 'NYC'], 'Population':[837000, 3880000, 8400000]}


# In[31]:


data


# In[32]:


city_frame = DataFrame(data)


# In[33]:


city_frame


# In[34]:


website = "http:pandas.pydata.org/pandas-docs/dev/generated/pandas.DataFrame.html"


# In[35]:


webbrowser.open(website)


# In[ ]:




