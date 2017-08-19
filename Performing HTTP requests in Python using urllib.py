
# coding: utf-8

# # Performing HTTP requests in Python using urllib

# In[2]:

# import package
from urllib.request import urlopen


# In[3]:

from urllib.request import Request


# In[4]:

# source file
url = "http://www.datacamp.com/teach/documentation"


# In[5]:

request = Request(url)


# In[10]:

response = urlopen(request)


# In[11]:

print(type(response))


# In[12]:

# close connection
response.close()


# In[ ]:



