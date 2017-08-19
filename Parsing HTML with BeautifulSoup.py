
# coding: utf-8

# # Parsing HTML with BeautifulSoup

# In[2]:

# import packages
import requests


# In[3]:

# import packages
from bs4 import BeautifulSoup


# In[4]:

# Assign the url
url = 'https://www.python.org/~guido/'


# In[5]:

r = requests.get(url)


# In[6]:

html_doc = r.text


# In[8]:

soup = BeautifulSoup(html_doc, 'lxml')


# In[12]:

pretty_soup = soup.prettify()


# In[13]:

print(pretty_soup)


# In[ ]:



