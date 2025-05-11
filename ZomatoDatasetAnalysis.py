#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('zomato.csv',encoding='latin')
df.head()


# In[3]:


df.columns


# In[4]:


df.info()


# In[5]:


df.describe()
# all integer/ numerical data here


# # Things we do in Data Analysis
# 1. Missing values
# 2. Explore about numerical variables
# 3. Explore about catergorical variables
# 4. Finding relationship between features

# In[6]:


# df.isnull()
df.isnull().sum()


# In[7]:


[i for i in df.columns if df[i].isnull().sum()>0]


# In[8]:


# sns.heatmap(df.isnull())
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')


# In[9]:


df_country = pd.read_excel('Country-Code.xlsx')
df_country.head()


# In[10]:


df_country.columns


# In[11]:


df.columns


# In[12]:


final_df = pd.merge(df,df_country,on='Country Code',how='left')


# In[13]:


final_df.head(2)


# In[14]:


final_df.dtypes


# In[15]:


final_df.Country.value_counts()
# So in India, zomato is available for use than in other countries


# In[16]:


final_df.Country.value_counts().index


# In[17]:


final_df.Country.value_counts().values


# In[18]:


country_name = final_df.Country.value_counts().index
country_val = final_df.Country.value_counts().values


# In[19]:


# PIE CHART

plt.pie(country_val,labels=country_name)


# In[20]:


# Pie chart of top 3 countries that uses zomato
plt.pie(country_val[:3],labels=country_name[:3])


# In[21]:


# Pie chart with annotation
plt.pie(country_val[:3],labels=country_name[:3],autopct='%1.2f%%')


# Observation: Zomato maximum records or transaction are from India and the minimum are from United Kingdom. United States have the average zomato transaction.

# In[22]:


final_df.columns


# In[23]:


# Grouping numerical functions
final_df.groupby(['Aggregate rating','Rating color','Rating text'])


# In[24]:


final_df.groupby(['Aggregate rating','Rating color','Rating text']).size()


# In[25]:


# Converting it into a dataframe
ratings = final_df.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'Rating count'})


# In[26]:


ratings.head()


# # Conclusion or Observation
# 1. Ratings 4.5-4.9 stands for Excellent
# 2. Ratings 4.1-4.4 indicates Very Good
# 3. Ratings between 3.5-4.4 is for Good
# 4. Ratings 2.5-3.4 states Average
# 5. Ratings 1.8-2.4 text is Poor

# In[27]:


plt.figure(figsize=(10,5))
sns.barplot(x='Aggregate rating',y='Rating count',data=ratings)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# In[28]:


# observation: gaussian curve


# In[29]:


#Let us give graph the color as it is represented in the DataFrame!
# plt.figure(figsize=(10,6))
sns.barplot(x='Aggregate rating',y='Rating count',hue='Rating color',data=ratings)
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# In[30]:


#as the colors aren't matching with the actual colors in the dataframe then we need to map it manually
#by using pallete


# In[31]:


plt.figure(figsize=(10,3))
sns.barplot(data=ratings,x='Aggregate rating',y='Rating count',hue='Rating color',palette=['blue','red','orange','yellow','green','green'])
plt.tight_layout()
plt.xticks(rotation=90)
plt.show()


# Observation:
# 1. Not rated count is very high.
# 2. Maximum number of rating are between 2.5 to 3.4

# In[32]:


# Count Plot of the above data on the basis of categorical data!
sns.countplot(x='Rating color',data=ratings, palette=['blue','red','orange','yellow','green','green'] )


# In[33]:


# Find the country with 0 rating on zomato
final_df.columns


# In[34]:


final_df.groupby(['Aggregate rating','Country']).size().reset_index()


# Observation:
#         Maximum number of zero ratings are from Indian customers

# In[35]:


# Find which country uses which currency 
final_df.groupby(['Country','Currency']).size().reset_index() #can use aggregate function with this method later if required
final_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index() #can't use agg func more restricted but it is memory efficient as it uses only 2 columns


# In[36]:


# Which countries do have online delivery option
# Method 1
final_df[['Country','Has Online delivery']].groupby(['Country','Has Online delivery']).size().reset_index()
# Method 2
final_df[final_df['Has Online delivery']=='Yes'].Country.value_counts()


# Observation:
# India and UAE has online delivery option

# In[37]:


# Create a pie chart for cities distribution (top 5)


# In[38]:


final_df.columns


# In[39]:


final_df.City.value_counts().index


# In[44]:


city_val = final_df.City.value_counts().values
city_name = final_df.City.value_counts().index


# In[52]:


plt.pie(city_val[:5],labels=city_name[:5],autopct='%1.2f%%')


# In[62]:


# Find the number of top 10 cuisines
final_df.Cuisines.value_counts().head(10)


# In[68]:


cuisines_label = final_df.Cuisines.value_counts().index
cuisines_val = final_df.Cuisines.value_counts().values


# In[72]:


plt.pie(cuisines_val[:10],labels=cuisines_label[:10],autopct='%1.2f%%')


# In[ ]:




