
# coding: utf-8

# # Turning a webpage into data using BeatifulSoup-Getting the Text

# In[1]:

# import libraries
import requests


# In[2]:

# import libraries
from bs4 import BeautifulSoup


# In[3]:

url = 'https://www.python.org/~guido/'


# In[4]:

r = requests.get(url)


# In[5]:

# Extract the response as html
html_doc = r.text


# In[6]:

# Create a BeautifulSoup object from the HTML
soup = BeautifulSoup(html_doc, 'lxml')


# In[17]:

# Get the title of the webpage
guido_title = soup.title


# In[18]:

# print the title
guido_title


# In[14]:

# Get the text of the html document (no tags)

guido_text = soup.get_text()


# In[16]:

print(guido_text)


# In[ ]:



