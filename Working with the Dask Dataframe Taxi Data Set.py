
# coding: utf-8

# # Working with the Dask DataFrame
# 
# ### Developer: Robert Esteves
# ### Date: 2018-03-12
# 
# ### Problem: To practice using Dask dataframes

# In[34]:

import dask.dataframe as dd


# In[35]:

import matplotlib.pyplot as plt


# ## Reading & cleaning files
# 
# ### Here you'll be working with a subset of the NYC Taxi Trip data. The first step is to use the Dask dd.read_csv() function to read multiple files at once. Dask will automatically concatenate the contents of the files into a single DataFrame. Notice that you'll use the option assume_missing=True in the call to dd.read_csv() to suppress warning messages.
# 
# ### Your job is to use a glob pattern containing the * character to read all of the CSV files from the taxi/ subdirectory into a single Dask DataFrame. You'll then construct a new column called 'tip_fraction' using the 'tip_amount' and 'total_amount' columns. The 'total_amount' is the sum of the fare, other fees, and the tip_amount.
# 
# Read all .csv files from the taxi/ directory (with a wildcard pattern *).
# 
# Create a column 'tip_fraction', which is the result of the 'tip_amount' divided by the difference of the 'total_amount' and 'tip_amount' columns.
# 
# Convert the 'tpep_dropoff_datetime' column to datetime using dd.to_datetime().
# 
# Create a column 'hour' using the .dt.hour attribute of the 'tpep_dropoff_datetime' column.

# In[36]:

# Read all .csv files: df
df = dd.read_csv('F:/Data Camp Courses/Parallel Computing with Dask/nyctaxi/nyctaxi/yellow_tripdata_2015*.csv',
                assume_missing=True
                )


# In[37]:

# Make column 'tip_fraction'
df['tip_fraction'] = df['tip_amount']/(df['total_amount'] - df['tip_amount'])


# In[38]:

# Convert 'tpep_dropoff_datetime' column to datetime objects
df['tpep_dropoff_datetime'] = dd.to_datetime(df['tpep_dropoff_datetime'])


# In[39]:

# Construct column 'hour'
df['hour'] = df['tpep_dropoff_datetime'].dt.hour


# ## Filtering & grouping data
# 
# ### You have the Dask dataframe df prepared using multiple CSV files from the last exercise. It contains a subset of the 2015 yellow taxi ride data from New York City with some additional columns from preprocessing. Remember, none of the files have actually been loaded, nor has any computation been done to construct the new columns.
# ### Your task now is to build a pipeline of computations to compute the hourly average tip fraction for each hour of the day across the entire year of data. You'll have to filter for payments of type 1 (credit card transactions) from the 'payment_type' column, group transactions using the 'hour' column, and finally aggregate the mean from the 'tip_fraction' column.
# 
# Filter out rows where payment_type is 1 and call the resulting dataframe credit.
# 
# Group credit using the 'hour' column and call the result 'hourly'.
# 
# Select the 'tip_fraction' column and aggregate the mean.
# 
# Display the data type of result.

# In[40]:

# Filter rows where payment_type == 1: credit
credit = df.loc[df['payment_type']==1 ]


# In[41]:

# Group by 'hour' column: hourly
hourly = credit.groupby('hour')


# In[42]:

# Aggregate mean 'tip_fraction' and print its data type
result = hourly['tip_fraction'].mean()


# In[43]:

# Aggregate mean 'tip_fraction' and print its data type
print(type(result))


# ## Computing & plotting
# 
# ### Now that you've got the entire delayed pipeline prepared it's time compute and plot the result. Matplotlib has been imported for you as plt.
# 
# ### Warning: The execution of of this exercise is expected to be several seconds.
# 
# Perform the computation on result and assign it to tip_frac.
# 
# Print the type of tip_frac.
# 
# Hit 'Submit Answer to view the plot.

# In[44]:

# Perform the computation
tip_frac = result.compute()


# In[45]:

# # Print the type of tip_frac
print(type(tip_frac))


# In[46]:

tip_frac


# In[48]:

# Generate a line plot using .plot.ine()
_ = tip_frac.plot.line()


# In[49]:

_ = plt.ylabel('Tip fraction')


# In[50]:

plt.show()


# In[ ]:



