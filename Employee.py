#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd 
import matplotlib.pyplot as plot
import seaborn as sns


# In[5]:


df = pd.read_csv('Employe_Performance_dataset.csv')
df


# In[7]:


###pd.set_option('display.max.rows',561)


# In[10]:


df


# In[12]:


df.info()


# In[14]:


df.isnull().sum()


# In[16]:


df['Name'].value_counts()


# In[18]:


df.dropna(subset =['Performance Score'], inplace = True)
df


# In[19]:


#location and session rename 
df.rename(columns={'Location': 'Residency'},inplace = True)
df


# In[22]:


df.rename(columns= {'Performance Score' : 'Performance Rating'}, inplace = True)
df


# In[24]:


df.rename(columns={'Session' : 'Shift'},inplace= True)
df


# In[26]:


#lets get the mean to experience, salary, and age
avg_years_of_experience = round(df['Experience'].mean(),1)
print("What is the average years of experience for employees:", avg_years_of_experience)


# In[28]:


avg_salary = round(df['Salary'].mean(),1)
print("What is the average salary that employees make:",avg_salary)


# In[30]:


avg_age = round(df['Age'].mean(),1)
print("What is the average age for employees", avg_age)


# In[32]:


#what is the performance rating of employees of 10 years
experienced_employees = df[df['Experience'] > 10]
print(experienced_employees[['Name', 'Age','Performance Rating','Experience']])


# In[34]:


#Find the employees who have a salary greater than 1000
salary_earnings = df[df['Salary'] > 1000]
print(salary_earnings[['Name','Age','Gender','Salary']])


# In[36]:


#the next thing I wanted to do is see the employees with the ratings below 3 
low_ratings = df[df['Performance Rating'] < 3]
print(low_ratings[['Name', 'Gender','Salary','Performance Rating']])


# In[38]:


#avg salary in each department
avg_salary_2 = round(df.groupby('Department')['Salary'].mean(),1)
print("what is the average salary in each",avg_salary_2)


# In[40]:


highest_rating_department = round(df.groupby('Department')['Performance Rating'].mean(),1)
print('which department has the highest average',highest_rating_department)


# In[42]:


df.drop(columns=['ID'],inplace = True)
df


# In[44]:


df.loc[[0,1]]


# In[77]:


df[(df['Department']== 'Sales') & (df['Performance Rating']== 2.0)]


# In[ ]:


df.head(10)


# In[ ]:


df[df['Status']== 'Inactive']


# In[ ]:





# In[51]:


df[df['Residency']=='Los Angeles']


# In[53]:


df[df['Residency']=='Chicago']


# In[55]:


df.describe()


# In[75]:


plot.hist(df['Salary'], bins=50,color = 'red', alpha = 0.8)
plot.title('Performance Rating to Salary')
plot.xlabel('Salary')
plot.ylabel('Rating')
plot.show()


# In[ ]:




