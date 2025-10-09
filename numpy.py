#!/usr/bin/env python
# coding: utf-8

# # Numpy
# Numpy is a linear algebra library in python and it is the holy grail and the main building block of data science using python

# In[1]:


pip install numpy


# In[2]:


import numpy as np


# In[3]:


arr1=np.array([1,2,3,4,5])
arr1


# In[9]:


type(arr1)


# In[6]:


arr1.size


# In[7]:


arr1.ndim


# In[8]:


arr1.shape


# # arrays can be of n dimensions.

# In[10]:


my_matrix=[[2,3,4.5,4],[3,5,43,64],[5,6.6,45,4]]
my_matrix


# In[11]:


b=np.array(my_matrix)
b


# In[12]:


print('the dimensions of array',b.ndim)


# In[13]:


print('the size od array:',b.size)


# In[15]:


print('the type of array:',type(b))


# In[16]:


print('the shape od array:',b.shape)


# In[ ]:





# In[27]:


import numpy as py
int8_arr=np.array([1,2,3],dtype=np.int8)
int16_arr=np.array([1003,-2000.3000],dtype=np.int16)
int32_arr=np.array([1003000,2000000.3000000],dtype=np.int32)
int16_arr=np.array([100300000,20000000000.30000000000],dtype=np.int64)


# # float

# In[19]:


float16_arr = np.array([1.1,-2.2,3.3],dtype=np.float16)
float32_arr = np.array([1.112345,2.212345,3.321123],dtype=np.float32)
float16_arr = np.array([1.5434534541,2.2123456789,.31234234567],dtype=np.float16)


# # compex

# In[25]:


complex64_arr = np.array([1-2, 3+43], dtype=np.complex64)
complex128_arr = np.array([1-2, 3+4], dtype=np.complex128)


# # boolean

# In[26]:


bool_arr=np.array([True,False,True],dtype=bool)
print("bool:",bool_arr,bool_arr.dtype)


# # string

# In[28]:


string_arr=np.array(["apple","banana","cherry"],dtype='<U10')


# # object type

# In[29]:


object_arr=np.array([1,"two",3.0,True],dtype=object)


# In[ ]:




