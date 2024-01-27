#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


data = pd.read_csv("Unemployment in India.csv")


# ## EDA :- 

# In[3]:


data.head(10)


# In[4]:


data.info()


# In[5]:


data.isnull().sum


# In[7]:


data.describe()


# In[8]:


numeric_data = data.select_dtypes(include='number')

plt.style.use("ggplot")

plt.figure(figsize=(10, 10))
sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


# In[9]:


plt.style.use("dark_background")

data.columns = ["Region", "Date", "Frequency", "Estimated Unemp Rate", "Estimated Emp Rate", "Estimated Labour Rate", "Area"]

plt.figure(figsize=(10, 6))
sns.histplot(x="Estimated Emp Rate", hue="Area", data=data, kde=True, palette="Set2")
plt.title("Histogram of Estimated Employment Rate by Area")
plt.xlabel("Estimated Employment Rate")
plt.ylabel("Count")
plt.show()


# In[10]:


plt.style.use("dark_background")

data.columns = ["Region", "Date", "Frequency", "Estimated Unemp Rate", "Estimated Emp Rate", "Estimated Labour Rate", "Area"]

plt.figure(figsize=(10, 6))
sns.histplot(x="Estimated Unemp Rate", hue="Area", data=data, kde=True, palette="Set2")
plt.title("Histogram of Estimated Unemployment Rate by Area")
plt.xlabel("Estimated Unemployment Rate")
plt.ylabel("Count")
plt.show()


# In[11]:


import seaborn as sns

data = data[['Region', 'Estimated Unemp Rate']]
sns.boxplot(x='Region', y='Estimated Unemp Rate', data=data)
plt.xlabel('Region')
plt.ylabel('Estimated Unemployment Rate')
plt.title('Box Plot of Estimated Unemployment Rate by Region')
plt.xticks(rotation=45)
plt.show()


# In[12]:


import pandas as pd
import matplotlib.pyplot as plt


data = data[['Region', 'Estimated Unemp Rate']]
data_grouped = data.groupby('Region')['Estimated Unemp Rate'].mean()
data_grouped.plot(kind='bar')
plt.xlabel('Region')
plt.ylabel('Mean Estimated Unemployment Rate')
plt.title('Mean Estimated Unemployment Rate by Region')
plt.show()


# In[13]:


data = data[['Region', 'Estimated Unemp Rate']]
data_grouped = data.groupby('Region')['Estimated Unemp Rate'].sum()
data_grouped.plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribution of Estimated Unemployment Rate by Region')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[ ]:




