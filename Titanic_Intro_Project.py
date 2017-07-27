
# coding: utf-8

# # Titanic Intro project

# Language: Python
# Author: Robert Esteves

# In[2]:


import pandas as pd


# In[3]:


from pandas import Series, DataFrame


# In[13]:


import numpy as np


# In[14]:


import matplotlib.pyplot as plt


# In[15]:


import seaborn as sns


# In[16]:


get_ipython().magic('matplotlib inline')


# In[5]:


source_directory_path = '/xxxxxxxxxxxxxxx/Downloads/'


# In[6]:


source_file_name = 'titanic_train.csv'


# In[7]:


titanic_df = pd.read_csv(source_directory_path + source_file_name )


# In[8]:


titanic_df.shape


# In[9]:


titanic_df.axes


# In[10]:


titanic_df.head()


# # Notes:
# #### 1. Survived column: 1 = survived; 0 = did not survive
# #### 2. Pclass column: Passenger class 1st, 2nd, 3rd
# #### 3. SibSp column: siblings on board; 1=True, 0=False
# #### 4. Parch column: Parents or Children on board; 1=True, 0=False
# #### 5. Cabin column: where available the letters A,B,C,D and so on stand for the deck the of the cabin
# #### 6. Embarked column: location where the passenger embarked
# 

# In[12]:


# check for nulls and column data types
titanic_df.info()  


# ## First some basic questions:
# #### 1.) who were the passengers on the Titanic? (Ages, Gender, Class, ..etc)
# #### 2.) What decks were the passangers on and how does that relate to their class?
# #### 3.) Where did the passangers come from?
# #### 4.) Who was alone and who was with family?
# ## Then we'll dig deeper, with a broaders question:
# #### 5.) What factors helped someone survive the sinking?

# In[19]:


# Q1: who were the passengers on the Titanic? (Ages, Gender, Class, ..etc)

sns.factorplot('Sex', data=titanic_df, kind="count")


# In[20]:


# Sex by Passenger Class

sns.factorplot('Sex', data=titanic_df, kind='count', hue='Pclass')


# In[22]:


sns.factorplot('Pclass', data=titanic_df, kind='count', hue='Sex')


# In[23]:


def male_female_child (passenger):
    age, sex = passenger
    
    if age < 16:
        return 'child'
    else:
        return sex


# In[24]:


# Add new column to the dataset

titanic_df['person'] = titanic_df[ ['Age', 'Sex'] ].apply(male_female_child, axis = 1)


# In[25]:


titanic_df.head(10)


# In[26]:


sns.factorplot('Pclass', data=titanic_df, kind='count', hue='person')


# In[27]:


titanic_df['Age'].hist(bins=70)


# In[28]:


titanic_df['Age'].mean()


# In[29]:


# Overall comparison of male, female, and children populations

titanic_df['person'].value_counts()




