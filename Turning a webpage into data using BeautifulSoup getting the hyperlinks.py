
# coding: utf-8

# # Turning a webpage into data using BeautifulSoup--getting the hyperlinks

# In[3]:

# import library
import requests 


# In[4]:

# import library
from bs4 import BeautifulSoup


# In[5]:

# source url
url = 'https://www.python.org/~guido/'


# In[6]:

# send the request to get the url
r = requests.get(url)


# In[7]:

# convert to html
html_doc = r.text


# In[8]:

# Create BeautifulSoup object from html doc
soup = BeautifulSoup(html_doc, 'lxml')


# In[9]:

# Print the webpage title
print(soup.title)


# In[12]:

# find all the 'a' tags 
a_tags = soup.find_all('a')


# In[13]:

print(a_tags)


# In[14]:

# print the URLs
for link in a_tags:
    print(link.get('href'))


# In[ ]:



