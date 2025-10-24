#!/usr/bin/env python
# coding: utf-8

# # list
# ### list  indicates [] brackets 
# ### 1. list is a data structure in python
# ### 2. list is mutable and it allows duplicate values
# ### 3. append() append method is used to add the elements at the end of the list. 
# ### 4. it also allows negative indexing

# In[ ]:





# In[3]:


a=[10,34,54,56,4,34]
print(type(a))       #type is use to check the data structure type 


# # list methods
# # to add the elements to a list
# # 1. append() 
# ### -> append is used to add the elements at the end of existing list 
# ### -> append() append method is used to add single or multiple values in the list

# In[6]:


a.append([34,54,54,34,65,32,35])
print(a) #[10, 34, 54, 56, 4, 34, [34, 54, 54, 34, 65, 32, 35]]


# In[7]:


a.append(65)
print(a)


# In[ ]:





# # 2. insert() method
# ###  -> insert() method is used to insert the elements in the list at a specific location mention by index value
# ###  -> index values starts from 0 to n-1

# In[1]:


a=[32,34,6,43,35,34,23]
(a)


# In[2]:


a.insert(2,55)     
print(a)          # add element 55 at the location of 2


# In[3]:


a.insert (-3,44)
print(a)          # adding element 44 by using negative indexing


# # 3.  extend() method 
# ### -> 1. to add the elements in the list
# ### -> 2. append adds elements but its gives only one index value for multiple values but 
# ###     extend gives different index values for each element
# 
# 

# In[14]:


a=[32,53,56,34,67,34,23]
print (a)
b=[345.5,34,67,43,67,34]
(b)
a.extend(b)
print(a)


# # methods to remove the elements from the list
# ### 1. remove()    -> it's remove the element from the list by given element_value
# ### 2. pop(index)  -> it's remove the element from the list by given index_value
# ### 3. clear()     -> it removes the all elements from the list        

# # 1. remove()
# ### remove() -> it's remove the element from the list by given element_value

# In[23]:


a=[23,576,432,223,4,243,664,87]
print(a)      #creating a list


# In[24]:


a.remove(576)     #removing element 576
print(a)     


# # 2. pop() 
# ### pop(index) -> it's remove the element from the list by given index_value

# In[25]:


print(a)
a.pop(3)
print(a)


# # 3. clear ()
# ### clear() -> it removes the all elements from the list

# In[27]:


a.clear()
print(a)



# # 7. sort()
# ### -> to sort the list in the ascending or decending order
# ### -> by default the list is sorted to asending order

# In[4]:


a=[23,65,33,876,35,54]
print(a)
a.sort()                # default sorted to acending order
print(a)
a.sort(reverse=True)    # to sort in decending order
print(a)


# # 8. count()
# ### -> Returns the number of elements with the specified value
# 

# In[33]:


a=[23,564,465,453,7565,34,45]
print(a.index(34))      #display the index value of 34
print(a.count(34))      #display that 34 is repeated no. of times


# # 9. copy()
# ### -> it gives the copy of list

# In[6]:


a=[23,564,465,453,7565,34,45]
a1=[]
a1=a.copy()  # copies the list a data to list  a1.
print(a1)


# # 10. reverse()
# ### ->Reverses the order of the list

# In[9]:


a = [24,46,57,34,76,43,78]
a.reverse()  # display the list in reverse order
a


#  # 11. index()
# ### -> Returns the index of the first element with the specified value

# In[10]:


a = [24,46,57,34,76,43,78]
a.index(57)    # display the index value of element 57 


# # write a pgm to print even numbers in the list

# In[7]:


a=[452,34,53,53,75,465,76,5434]
for i in a:
    if i%2==0:
        print (i,end=" ")


# # write a pgm to print even numbers in the list

# In[55]:


list=[34,56,67,78,32,90,11,13,17]
fact=0
for i in list:
    fact=0
    for j in range(1, (i+1)):
        if i%j==0:
            fact=fact+1
    if fact==2:
        print(i, end=" ")

             
            


# # write a pgm to print second max element in the list

# In[56]:


list=[34,56,67,78,32,90,11,13,17]
list.sort(reverse=True)    #sort the list into descending order
print(list[1])  #dispay the 2nd index element 


# # write a program to find no. of words in the list

# #### input: hi hello this is prem kumar

# In[57]:


str="hi hello this is prem kumar"  #store the words in str
words=str.split(" ")              # spliting the words into list 
print(type(words))           # checking the data structure typr
print(words[2])        
print("Number of words :",len(words))      # counting and display the length of words


# # write a program to find number of characters in each word in a list

# #### input : Hi hello this is prem kumar
# #### output:
#          Hi  -- 2
#          hello  - 5
#          this  -- 4
#          is    - 2
#          prem   - 4
#          kumar  --5

# In[58]:


str="Hi hello this is prem kumar"      #store the words in str
words=str.split(" ")                   # spliting the words into list 
for word in words:
    print(word," -- ", len(word))       # display the length of eacwords


# # write a program to find number of alphabets, no. of digits,no. of special characters in each word of a given sentence

# ### input:  hi12 hello343 this@ is! prem32@ kumar32
# 
# ### output:
#     hi12: alphabets: 2
#             digits : 2
#     hello343: alphabets: 4
#                 digits  :3
#     this@  : alphabets  :4
#             specialchar: 1
#     is!  : alphabet   :2
#             specialchar: 1
#     prem32@ :alphabet: 4
#             digits  :2
#         specialchar: 1
#     kumar32 : alphabet:5

# In[16]:


n = "hi12 hello343 this@ is! prem32@ kumar32"
words = n.split(" ")

for word in words:
    alpha = 0
    digits = 0
    special = 0
    for char in word:
        if char.isalpha():
            alpha += 1
        elif char.isdigit():
            digits += 1
        else:
            special += 1

    print(word + ":")
    if alpha > 0:
        print("  alphabets   :", alpha)
    if digits > 0:
        print("  digits      :", digits)
    if special > 0:
        print("  specialchar :", special)


# In[ ]:




