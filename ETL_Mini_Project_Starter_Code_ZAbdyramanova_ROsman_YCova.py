#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import dependencies
import pandas as pd
import numpy as np
pd.set_option('max_colwidth', 400)


# ### Extract the crowdfunding.xlsx Data

# In[2]:


# Read the data into a Pandas DataFrame
crowdfunding_info_df = pd.read_excel('Resources/crowdfunding.xlsx')
crowdfunding_info_df.head()


# In[3]:


# Get a brief summary of the crowdfunding_info DataFrame.


# ### Create the Category and Subcategory DataFrames
# ---
# **Create a Category DataFrame that has the following columns:**
# - A "category_id" column that is numbered sequential form 1 to the length of the number of unique categories.
# - A "category" column that has only the categories.
# 
# Export the DataFrame as a `category.csv` CSV file.
# 
# **Create a SubCategory DataFrame that has the following columns:**
# - A "subcategory_id" column that is numbered sequential form 1 to the length of the number of unique subcategories.
# - A "subcategory" column that has only the subcategories. 
# 
# Export the DataFrame as a `subcategory.csv` CSV file.

# In[4]:


# Get the crowdfunding_info_df columns.


# In[5]:


# Assign the category and subcategory values to category and subcategory columns.


# In[6]:


# Get the unique categories and subcategories in separate lists.


print(categories)
print(subcategories)


# In[7]:


# Get the number of distinct values in the categories and subcategories lists.
print(len(categories))
print(len(subcategories))


# In[8]:


# Create numpy arrays from 1-9 for the categories and 1-24 for the subcategories.
category_ids = np.arange(1, 10)
subcategory_ids = np.arange(1, 25)

print(category_ids)
print(subcategory_ids)


# In[9]:


# Use a list comprehension to add "cat" to each category_id. 

# Use a list comprehension to add "subcat" to each subcategory_id.    

    
print(cat_ids)
print(scat_ids)


# In[10]:


# Create a category DataFrame with the category_id array as the category_id and categories list as the category name.

# Create a category DataFrame with the subcategory_id array as the subcategory_id and subcategories list as the subcategory name. 


# In[11]:


category_df


# In[12]:


subcategory_df


# In[13]:


# Export categories_df and subcategories_df as CSV files.
category_df.to_csv("Resources/category.csv", index=False)

subcategory_df.to_csv("Resources/subcategory.csv", index=False)


# ### Campaign DataFrame
# ----
# **Create a Campaign DataFrame that has the following columns:**
# - The "cf_id" column.
# - The "contact_id" column.
# - The “company_name” column.
# - The "blurb" column is renamed as "description."
# - The "goal" column.
# - The "goal" column is converted to a `float` datatype.
# - The "pledged" column is converted to a `float` datatype. 
# - The "backers_count" column. 
# - The "country" column.
# - The "currency" column.
# - The "launched_at" column is renamed as "launch_date" and converted to a datetime format. 
# - The "deadline" column is renamed as "end_date" and converted to a datetime format.
# - The "category_id" with the unique number matching the “category_id” from the category DataFrame. 
# - The "subcategory_id" with the unique number matching the “subcategory_id” from the subcategory DataFrame.
# - And, create a column that contains the unique four-digit contact ID number from the `contact.xlsx` file.
#  
# 
# Then export the DataFrame as a `campaign.csv` CSV file.
# 

# In[14]:


# Create a copy of the crowdfunding_info_df DataFrame name campaign_df. 
campaign_df = crowdfunding_info_df.copy()
campaign_df.head()


# In[15]:


# Rename the blurb, launched_at, and deadline columns.


# In[16]:


# Convert the goal and pledged columns to a `float` data type.


# In[17]:


# Check the datatypes


# In[18]:


# Format the launched_date and end_date columns to datetime format
from datetime import datetime as dt


# In[19]:


# Merge the campaign_df with the category_df on the "category" column and 
# the subcategory_df on the "subcategory" column.


campaign_merged_df.tail(10)


# In[20]:


# Drop unwanted columns


# In[21]:


# Export the DataFrame as a CSV file. 
campaign_cleaned.to_csv("Resources/campaign.csv", index=False)


# ### Extract the contacts.xlsx Data.

# In[130]:


# Read the data into a Pandas DataFrame. Use the `header=2` parameter when reading in the data.
contact_info_df = pd.read_excel('Resources/contacts.xlsx', header=2)
contact_info_df.head()


# ### Create the Contacts DataFrame 
# ---
# **Create a Contacts DataFrame that has the following columns:**
# - A column named "contact_id"  that contains the unique number of the contact person.
# - A column named "first_name" that contains the first name of the contact person.
# - A column named "last_name" that contains the first name of the contact person.
# - A column named "email" that contains the email address of the contact person
# 
# Then export the DataFrame as a `contacts.csv` CSV file.

# ### Option 1: Use Pandas to create the contacts DataFrame.

# In[131]:


# Iterate through the contact_info_df and convert each row to a dictionary.
import json
dict_values = []


# Print out the list of values for each row.
print(dict_values)


# In[191]:


import json

dict_values = []
for i, row in contact_info_df.iterrows():
    json_data = json.loads(row[0])
    values = [value.strip() for value in json_data.values()]
    print(json_data)
    dict_values.append(values)

# print(dict_values)



# In[187]:


# Create a contact_info DataFrame and add each list of values, i.e., each row 
# to the 'contact_id', 'name', 'email' columns.


# In[26]:


# Check the datatypes.
contact_info.info()


# In[27]:


# Create a "first"name" and "last_name" column with the first and last names from the "name" column. 
# Drop the contact_name column

#Done in Option 2


# In[28]:


# Reorder the columns

#Done in Option 2


# In[29]:


# Check the datatypes one more time before exporting as CSV file.

#Done in Option 2


# In[30]:


# Export the DataFrame as a CSV file. 
contacts_df_clean.to_csv("Resources/contacts.csv", encoding='utf8', index=False)

#Done in Option 2


# ### Option 2: Use regex to create the contacts DataFrame.

# In[62]:


contact_info_df_copy = contact_info_df.copy()
contact_info_df_copy.head()
contact_info_df_copy.columns =['contact_info']


# In[63]:


# Extract the four-digit contact ID number.
contact_info_df_copy['contact_id']=contact_info_df_copy['contact_info'].str.extract(r'(\d{4})')
contact_info_df_copy = contact_info_df_copy.drop(0)
contact_info_df_copy.head(5)


# In[64]:


# Check the datatypes.
contact_info_df_copy.info()


# In[65]:


# Convert the "contact_id" column to an int64 data type.
contact_info_df_copy['contact_id']=contact_info_df_copy['contact_id'].astype(int)
contact_info_df_copy.info()


# In[80]:


# Extract the name of the contact and add it to a new column.
contact_info_df_copy['name'] = contact_info_df_copy['contact_info'].str.extract(r'"name":\s*"([^"]+)"')
contact_info_df_copy


# In[81]:


# Extract the email from the contacts and add the values to a new column.
contact_info_df_copy['email'] = contact_info_df_copy['contact_info'].str.extract(r'\s*"(\S+@\S+)"')
contact_info_df_copy


# In[89]:


# Create a copy of the contact_info_df with the 'contact_id', 'name', 'email' columns.
contact_info_df=contact_info_df_copy[['contact_id','name','email']]
contact_info_df.head(10)


# In[90]:


# Create a "first"name" and "last_name" column with the first and last names from the "name" column. 

# Drop the contact_name column
contact_info_df[["first_name","last_name"]] = contact_info_df["name"].str.split(' ', n=1, expand=True)
contact_info_df.drop('name', axis=1, inplace=True)
contact_info_df


# In[93]:


# Reorder the columns
contact_info_df=contact_info_df[['contact_id','first_name','last_name','email']]
contact_info_df


# In[97]:


# Check the datatypes one more time before exporting as CSV file.
contact_info_df_clean = contact_info_df.reset_index(drop=True)
contact_info_df_clean.info()


# In[100]:


# Export the DataFrame as a CSV file. 
contact_info_df_clean.to_csv("Resources/contacts.csv", encoding='utf8', index=False)

