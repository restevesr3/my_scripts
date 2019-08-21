
# coding: utf-8

# # Lecture 11 - Universal Array Functions

# ## Robert Esteves

# In[1]:


import numpy as np


# In[2]:


arr = np.arange(11)


# In[3]:


arr


# In[4]:


# Square Root of every value in the array
np.sqrt(arr)


# In[5]:


# Exponential operations
np.exp(arr)


# In[6]:


# Binary function requires two arrays
# create a random array
A = np.random.randn(10)


# In[7]:


A


# In[8]:


B = np.random.randn(10)


# In[9]:


B


# In[10]:


# Adding the two arrays
np.add(A,B)


# In[11]:


# find the max and min between the two arrays
np.maximum(A,B)


# In[12]:


np.minimum(A, B)


# In[13]:


documentation_website = 'http://docs.scipy.org/doc/numpy/reference/ufuncs.html#available-ufuncs'


# In[14]:


import webbrowser


# In[15]:


webbrowser.open(documentation_website)


# In[ ]:




