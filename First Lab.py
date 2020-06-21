#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url, header=None)


# In[9]:


print("The first 5 rows of the dataset")
df.head(5)


# In[12]:


print("The last 10 rows of the dataframe")
df.tail(10)


# In[13]:


# since our dataset does not have any header, and as we can see above, python adds automatic numbers to the columns
# therefore, we will create the headers by creating a list with the appropriate names of the headers

#create header
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)


# In[14]:


# we replace headers and recheck our data frame
df.columns = headers
df.head()


# In[4]:


# drop the missing values for the price column, the axis 0 is the row, axis 1 is column
df.dropna(subset=["price"], axis=0)
print(df.dtypes)


# In[2]:


# find the name of the columns in the dataframe
print(df.columns)
print(df.dtypes)


# In[22]:


# save the dataframe as a new csv file
df.to_csv("Elona.csv", index=False)


# In[1]:


# as we know dataframes consist of different padans data types
# in different scenarious we will need the pandas data type
# therefore to view what pandas data type you have in your dataset
# we use df.dtypes
print(df.dtypes)


# In[9]:


import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url, header=None)
print(df.head(5))
print(df.dtypes)


# In[13]:


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
df.columns=headers
# if we want a statistical summary of each column we use df.describe
# it also includes the valus NaN
# but is not applicable for object data type
df.describe()

# to include the object data type as well we use df.decribe(include = "all")
# which adds these additional rows: unique, top, freq
df.describe(include = "all")


# In[21]:


# we can select specific columns and get a summary of those columns
df[['symboling','aspiration']].describe(include="all")


# In[22]:


# another way to check the dataset is using the .info()
df.info()


# In[ ]:




