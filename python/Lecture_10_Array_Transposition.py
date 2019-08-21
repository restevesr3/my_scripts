
# coding: utf-8

# # Lecture 10 - Array Transposition

# ## Robert Esteves

# In[1]:


import numpy as np


# In[2]:


# Create an array of 50 numbers and then transpose it as 10 by 5 matrix
arr = np.arange(50).reshape(10, 5)


# In[3]:


arr


# In[4]:


# To transpose the matrix just use the ".T" property
arr.T


# In[5]:


# tak the product of the arr
np.dot(arr.T, arr)


# In[6]:


# How to create a three dimensional matrix

arr3d = np.arange(50).reshape((5,5,2))


# In[7]:


arr3d


# In[8]:


# transpose a 3d matrix
arr3d.transpose(1,0,2)


# In[9]:


# swapping axes in an array
arr = np.array([[1,2,3]])


# In[10]:


arr


# In[11]:


arr.swapaxes(0,1)


# In[ ]:




