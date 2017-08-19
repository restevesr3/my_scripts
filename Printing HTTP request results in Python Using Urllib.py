
# coding: utf-8

# In[1]:

# Pringint HTTP request results in Python using urllib


# In[3]:

from urllib.request import urlopen, Request


# In[13]:

# source url
url = "http://www.datacamp.com/teach/documentation"


# In[14]:

# submit the request
request = Request(url)


# In[15]:

response = urlopen(request)


# In[16]:

html = response.read()


# In[17]:

print(html)


# In[12]:

response.close()


# In[ ]:



