
# coding: utf-8

# # Lecture 13 - Array input and output

# ## Robert Esteves

# In[1]:


import numpy as np


# In[2]:


arr = np.arange(5)


# In[3]:


arr


# In[4]:


# save the array
np.save('my_array', arr)


# In[6]:


arr = np.arange(10)


# In[7]:


arr


# In[10]:


# how to call the save array
np.load('my_array.npy')


# In[11]:


# How to save multiple arrays
arr1 = np.load('my_array.npy')


# In[12]:


arr1


# In[13]:


arr2 = arr


# In[14]:


arr2


# In[15]:


# Save both arrays in a zipped file
np.savez('zip_array.npz', x = arr1, y=arr2)


# In[18]:


# load multiple arrays
archive_array = np.load('zip_array.npz')


# In[19]:


archive_array['x']


# In[20]:


archive_array['y']


# In[21]:


# save and load text files with numpy
arr = np.array([[1,2,3], [4,5,6]])


# In[22]:


arr


# In[23]:


# save as as text file
np.savetxt('my_text_array.txt', arr, delimiter='|')


# In[24]:


# Load the text array
arr = np.loadtxt('my_text_array.txt', delimiter='|')


# In[25]:


arr


# In[ ]:




