
# coding: utf-8

# # Performing HTTP requests in Python using requests

# In[6]:

# import package
import requests


# In[7]:

# source file
url = "http://www.datacamp.com/teach/documentation"


# In[8]:

# package the request
r = requests.get(url)


# In[9]:

# Extract the response
text = r.text


# In[10]:

# print the html
print(text)


# In[ ]:



