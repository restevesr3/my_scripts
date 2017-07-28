
# coding: utf-8

# # Lecture 12 - Array Processing

# ## Robert Esteves

# In[1]:


import numpy as np


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


# View visualizations
get_ipython().magic('matplotlib inline')


# In[4]:


# Create a grid
points = np.arange(-5, 5, 0.01)


# In[5]:


points


# In[6]:


dx, dy = np.meshgrid(points, points)


# In[7]:


dx


# In[8]:


# Create evaluating function
z = (np.sin(dx) + np.sin(dy))


# In[9]:


z


# In[10]:


# plot z
plt.imshow(z)


# In[13]:


plt.imshow(z)
plt.colorbar()

plt.title('Plot the sin(x) + sin(y)*')


# In[14]:


# Numpy where
A = np.array([1,2,3,4])


# In[15]:


B = np.array([100, 200, 300, 400])


# In[16]:


condition = np.array([True, True, False, False])


# In[18]:


# List comprehension
answer = [(A_val if cond else B_val) for A_val, B_val, cond in zip(A,B, condition)]


# In[19]:


answer


# In[20]:


# replace the list comprehension logic
answer2 = np.where(condition, A, B)


# In[21]:


answer2


# In[22]:


from numpy.random import randn


# In[23]:


arr = randn(5, 5)


# In[24]:


arr


# In[25]:


np.where(arr < 0, 0, arr)


# In[26]:


arr = np.array([[1,2,3], [4,5,6], [7,8,9]])


# In[27]:


arr


# In[28]:


arr.sum()


# In[29]:


# do the sum along an axis i.e. columns
arr.sum(0) # 0 equals columns


# In[30]:


arr.mean()


# In[31]:


arr.std()


# In[32]:


arr.var()


# In[33]:


bool_arr = np.array([True, False, True])


# In[34]:


# returns an array if any value in the array is true
bool_arr.any()


# In[35]:


# All will return true only if all values in the array are true
bool_arr.all()


# In[36]:


# Sort an array
arr = np.array([10,9,4,3,1,8, 24, 7])


# In[37]:


arr


# In[38]:


arr.sort()


# In[39]:


arr


# In[40]:


# unique function 
countries = np.array(['France', 'Germany', 'France', 'Mexico', 'Spain', 'Russia', 'USA', 'USA'])


# In[41]:


np.unique(countries)


# In[42]:


# This command checks inf the countries in the list exists in the countries array
np.in1d(['France', 'USA', 'Sweden'], countries)


# In[ ]:




