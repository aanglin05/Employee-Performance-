#!/usr/bin/env python
# coding: utf-8

# In[85]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# In[87]:


df = pd.read_csv('Employe_Performance_dataset.csv')
df


# In[89]:


###pd.set_option('display.max.rows',561)


# In[91]:


df


# In[93]:


df.info()


# In[95]:


df.isnull().sum()


# In[97]:


df['Name'].value_counts()


# In[99]:


df.dropna(subset =['Performance Score'], inplace = True)
df


# In[101]:


#location and session rename 
df.rename(columns={'Location': 'Residency'},inplace = True)
df


# In[103]:


df.rename(columns= {'Performance Score' : 'Performance Rating'}, inplace = True)
df


# In[105]:


df.rename(columns={'Session' : 'Shift'},inplace= True)
df


# In[107]:


#lets get the mean to experience, salary, and age
avg_years_of_experience = round(df['Experience'].mean(),1)
print("What is the average years of experience for employees:", avg_years_of_experience)


# In[109]:


avg_salary = round(df['Salary'].mean(),1)
print("What is the average salary that employees make:",avg_salary)


# In[111]:


avg_age = round(df['Age'].mean(),1)
print("What is the average age for employees", avg_age)


# In[113]:


#what is the performance rating of employees of 10 years
experienced_employees = df[df['Experience'] > 10]
print(experienced_employees[['Name', 'Age','Performance Rating','Experience']])


# In[115]:


#Find the employees who have a salary greater than 1000
salary_earnings = df[df['Salary'] > 1000]
print(salary_earnings[['Name','Age','Gender','Salary']])


# In[117]:


#the next thing I wanted to do is see the employees with the ratings below 3 
low_ratings = df[df['Performance Rating'] < 3]
print(low_ratings[['Name', 'Gender','Salary','Performance Rating']])


# In[119]:


#avg salary in each department
avg_salary_2 = round(df.groupby('Department')['Salary'].mean(),1)
print("what is the average salary in each",avg_salary_2)


# In[121]:


highest_rating_department = round(df.groupby('Department')['Performance Rating'].mean(),1)
print('which department has the highest average',highest_rating_department)


# In[123]:


df.drop(columns=['ID'],inplace = True)
df


# In[125]:


df.loc[[0,1]]


# In[127]:


df[(df['Department']== 'Sales') & (df['Performance Rating']== 2.0)]


# In[129]:


df.head(10)


# In[131]:


df[df['Status']== 'Inactive']


# In[133]:


df[df['Residency']=='Los Angeles']


# In[135]:


df[df['Residency']=='Chicago']


# In[137]:


df.describe()


# In[145]:


plt.figure(figsize = (10,6))
sns.barplot(data=df, y='Salary', x='Performance Rating',palette='viridis')

plt.title('Salary vs Performance Rating', fontsize=16)
plt.xlabel('Perfromance Rating', fontsize=12)
plt.ylabel('Salary',fontsize=12)
plt.xticks(fontsize= 10)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()


# In[ ]:




