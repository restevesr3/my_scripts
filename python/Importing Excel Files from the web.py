
# coding: utf-8

# # Importing non-flat files from the web

# In[1]:

# import pandas
import pandas as pd


# ## Importing an MS Excel File

# In[2]:

# Assing url of file
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'


# In[3]:

# import the entire workbook
xl = pd.read_excel(url, sheetname = None)


# In[8]:

# Extract the sheetnames
sheets = xl.keys()


# In[9]:

# Pring the sheet names
sheets


# In[13]:

# Print the first five rows of the '1700' spreadsheet.
xl['1700'].head()


# In[ ]:



