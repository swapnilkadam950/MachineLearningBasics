#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np


# In[8]:


my_list=[1,2,3,4,5,6]


# In[9]:


arr=np.array(my_list)


# In[10]:


print(arr)


# In[9]:


type(arr)


# In[11]:


mylist1=[1,2,3,4]
mylist2=[2,3,4,5]
mylist3=[5,6,7,8]


# In[12]:


arr1=np.array([mylist1,mylist2,mylist3])


# In[12]:


arr1


# In[13]:


arr1.shape


# In[13]:


arr1.reshape(4,3)


# In[16]:


arr1[2]


# In[17]:


arr1[0:2,1:3] #,is the delimiter,the left comma indicates the row and on the right indicates the column
#in the example the number before : indicates the starting point and the one on the right indicates the before which point
#0 is the starting point and 2 indicates the ending point so the rows that will be read will be 0 and 1.Same thing with column


# In[24]:


arr2=np.arange(0,15) #creates a numpy array within the given range


# In[23]:


arr2

