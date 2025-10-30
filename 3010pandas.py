#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
census_data=pd.read_csv("census.csv")   # to read the from dataset
census_data.head()   # to display top 5 data


# In[58]:


census_data.tail() # to display last 5 data


# # adding column names
# 

# In[3]:


import pandas as pd
column_names = ['age', 'education', 'Marital_Status', 'gender','parents_status', 'salary','occupation','country','region','no.']
census_data = pd.read_csv("census.csv", names=column_names)
print(column_names)  


# # 1. education analysis

# ### education category-wise gender-wise count

# In[4]:


edu_gender_counts = census_data.groupby(['gender']).size().reset_index(name='count') 
print(edu_gender_counts)     # counts gender 


# ### education qualification count based on employment

# In[5]:


edu_gender_counts = census_data.groupby(['education']).size().reset_index(name='count')
print(edu_gender_counts)   #to display education


# # 2.social analysis

# ### -> No. of Employable Female Citizens who are widows or Divorced
# 

# In[6]:


# Filter employable female widows or divorced
result = census_data[
    (census_data['gender'] == "Female") &
    (census_data['Marital_Status'].isin(["Widowed", "Divorced"])) &
    (~census_data['education'].str.contains("Children", case=False, na=False))
]

# Display the filtered data
print(result)

# Display the count
print(len(result))


# # 3. Financial analysis
# 

# ### > Gender wise Total Income Generated
# 

# In[10]:


census_data['salary'] = pd.to_numeric(census_data['salary'], errors='coerce')

#  Group by gender and sum up salaries
gender_income = census_data.groupby('gender')['salary'].sum()

# Display the result
print("Gender-wise Total Income Generated:")
print(gender_income)


# ### ->Total Income of different types of Tax Payers

# In[8]:


# Convert 'salary' column to numeric
census_data['salary'] = pd.to_numeric(census_data['salary'], errors='coerce')

# Group by taxpayer type (parents_status) and sum up salaries
taxpayer_income = census_data.groupby('parents_status')['salary'].sum().sort_values(ascending=False)

# Display result
print(" Total Income of Different Types of Tax Payers:\n")
print(taxpayer_income)


# # 4. Planning analysis
# 

# ### -->No. of Voters to get added in next x years
# 

# In[9]:


census_data['age'] = pd.to_numeric(census_data['age'], errors='coerce')
# Input — years in the future
x_years = int(input("Enter number of years (X): "))

#  Filter those who will become eligible voters in next X years
new_voters = census_data[
    (census_data['age'] < 18) & 
    ((census_data['age'] + x_years) >= 18)
]
# Count and display
print("\nNumber of voters to get added in next", x_years, "years:", len(new_voters))


# In[ ]:




