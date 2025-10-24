#!/usr/bin/env python
# coding: utf-8

# # tuples
# # tupes indicates in () brackets
# ### 1. onces tuple created we cannot change the tuple elements
# ### 2. it follows the indexing order
# ### 3. it allows duplicates
# 

# # tuple methods
# ### len(): Returns the number of elements in the tuple.
# ### min(): Returns the smallest element in the tuple (if elements are comparable).
# ### max(): Returns the largest element in the tuple (if elements are comparable).
# ### sum(): Returns the sum of all elements in the tuple (if elements are numeric).
# ### sorted(): Returns a new sorted list containing all items from the tuple.
# ### tuple(): Converts an iterable (like a list or string) into a tuple.

# In[12]:


a=(23,54,23,46,23,76)      # creating tuple
print(a)
print(a[1])                #display element in index 1
print("Max:",max(a))       #display maximum element from the tuple 
print("Min : ", min(a))    #display minimum element from the tuple 
print("Total: ",sum(a))    #display sum of element in the tuple 
print("No.of values :",len(a));  #display the length of the tuple 
print("sorted:",sorted(a));     #display sorted tuple default in ascending order
#a[1]=100  # Error because tuple is immutable
print(a[:])         #display element in the tuple
a[2:]               #display element in the tuple from index 2
print(a[:3])        #display element in the tuple before index 3
a[-1]               #display element in the last index
print(a[::])         #display element in the tuple
a[::-1]              #display element in reverse order


# In[9]:


b=(23,45,46,75,3,34,46,346,34,6,346,5,7,5,34)
print(b[::-1])       #display element in reverse order  


# # list vs tuple
# ### 1.list is mutable and tuple is immutable
#     list=[23,54,77]
#     list[1]=99      ==>     23   99  77
# 
#     tuple=(23,54,77)
#     tuple[1]=99      ==>     throws erroe
# ### 2. both data structure will allows duplicate values and follous indexing order.
# ### 3. type casting:
#     t=(23,44,46,34,)
#     l=list(t)        # TUPLE will be converted into list
# 
#     l=[23,35,56,342,57,23]
#     t=tuple(l)         # list will converted into list
# ### 4. it is unordered data structure till python 3.6 version, from 3.7 it is ordered amd mutable  
# 

# # dictionary 

# In[ ]:




