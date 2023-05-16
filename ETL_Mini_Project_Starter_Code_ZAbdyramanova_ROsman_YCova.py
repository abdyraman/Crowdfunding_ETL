#!/usr/bin/env python
# coding: utf-8

# In[40]:


# Import dependencies
import pandas as pd
import numpy as np
pd.set_option('max_colwidth', 400)


# ### Extract the crowdfunding.xlsx Data

# In[41]:


# Read the data into a Pandas DataFrame
crowdfunding_info_df = pd.read_excel('Resources/crowdfunding.xlsx')
crowdfunding_info_df.head()


# In[42]:


# Get a brief summary of the crowdfunding_info DataFrame.
crowdfunding_info_df.info()


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

# In[43]:


# Get the crowdfunding_info_df columns.
crowdfunding_info_df.columns


# In[44]:


# Assign the category and subcategory values to category and subcategory columns.
split_category_sub = crowdfunding_info_df['category & sub-category'].str.split('/', expand=True)
split_category_sub.columns = ["category", "sub-category"]
crowdfunding_info_df = pd.concat([crowdfunding_info_df, split_category_sub], axis=1)
crowdfunding_info_df


# In[51]:


# Get the unique categories and subcategories in separate lists.
categories = crowdfunding_info_df["category"].unique().tolist()
subcategories = crowdfunding_info_df["sub-category"].unique().tolist()
print(categories)
print(subcategories)


# In[52]:


# Get the number of distinct values in the categories and subcategories lists.
print(len(categories))
print(len(subcategories))


# In[53]:


# Create numpy arrays from 1-9 for the categories and 1-24 for the subcategories.
category_ids = np.arange(1, 10)
subcategory_ids = np.arange(1, 25)

print(category_ids)
print(subcategory_ids)


# In[62]:


# Use a list comprehension to add "cat" to each category_id. 
cat_ids = ['cat'+str(cat_id) for cat_id in category_ids]
# Use a list comprehension to add "subcat" to each subcategory_id
scat_ids = ['subcat'+str(subcat_id) for subcat_id in subcategory_ids]
print(cat_ids)
print(scat_ids)


# In[67]:


category_dict = {'category_id': cat_ids, 'category': categories}
category_df = pd.DataFrame(category_dict)
category_df


# In[68]:


# Create a category DataFrame with the category_id array as the category_id and categories list as the category name.
category_dict = {'category_id': cat_ids, 'category': categories}
category_df = pd.DataFrame(category_dict)
# Create a category DataFrame with the subcategory_id array as the subcategory_id and subcategories list as the subcategory name. 
subcategories_dict = {'subcategory_ids': scat_ids, 'subcategory': subcategories}
subcategory_df = pd.DataFrame(subcategories_dict)


# In[69]:


category_df


# In[70]:


subcategory_df


# In[71]:


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

# In[23]:


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

# In[24]:


# Iterate through the contact_info_df and convert each row to a dictionary.
import json
dict_values = []


# Print out the list of values for each row.
print(dict_values)


# In[25]:


# Create a contact_info DataFrame and add each list of values, i.e., each row 
# to the 'contact_id', 'name', 'email' columns.


# In[26]:


# Check the datatypes.


# In[27]:


# Create a "first"name" and "last_name" column with the first and last names from the "name" column. 


# Drop the contact_name column


# In[28]:


# Reorder the columns


# In[29]:


# Check the datatypes one more time before exporting as CSV file.


# In[30]:


# Export the DataFrame as a CSV file. 
contacts_df_clean.to_csv("Resources/contacts.csv", encoding='utf8', index=False)


# ### Option 2: Use regex to create the contacts DataFrame.

# In[31]:


contact_info_df_copy = contact_info_df.copy()
contact_info_df_copy.head()


# In[32]:


# Extract the four-digit contact ID number.


# In[33]:


# Check the datatypes.


# In[34]:


# Convert the "contact_id" column to an int64 data type.


# In[35]:


# Extract the name of the contact and add it to a new column.


# In[36]:


# Extract the email from the contacts and add the values to a new column.


# In[37]:


# Create a copy of the contact_info_df with the 'contact_id', 'name', 'email' columns.


# In[38]:


# Create a "first"name" and "last_name" column with the first and last names from the "name" column. 


# Drop the contact_name column


# In[39]:


# Reorder the columns


# In[40]:


# Check the datatypes one more time before exporting as CSV file.


# In[41]:


# Export the DataFrame as a CSV file. 
# contacts_df_clean.to_csv("Resources/contacts.csv", encoding='utf8', index=False)


# In[ ]:




