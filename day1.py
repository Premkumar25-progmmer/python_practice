#!/usr/bin/env python
# coding: utf-8

# In[15]:


r=float(input())
a=3.14*r*r
print(a)


# In[18]:


s=input()
vowels="aeiouAEIOU"
c=0
count=0
for char in s:
    if char in vowels:
        count+=1
    else:
        c+=1
print("vowels:",count)        
print(c)





# In[34]:


list= [35, 42, 53, 70, 35]
j=[]
for i in list:
    if i%5==0:
        j.append(i-5)
    else:
        j.append(i)
print(j)



# In[47]:


l=list(map(int,input().split()))
j=[]
p=[]
for i in l:
    if i%2==0:
        j.append(i)
    else:
        p.append(i)
print(j)
print(p)


# In[55]:


n = list(map(int, input().split()))

e = 0
o = 0

for i in range(len(n)):     
    if n[i] % 2 == 0:       
        e+=i
    else:
        o+=i

print("even=",e)
print("odd=",o)

        
    


# In[54]:


nums = list(map(int, 

a = 0
b = 0

for i in nums:
    if i % 2 == 0:
        even += i
        a += i
    else:
        odd += i
        b += i

print(even)
print(odd)


# In[56]:


n =[20,35,45,60,30,75,85,45,25,40]

e = 0
o = 0

for i in range(len(n)):     
    if n[i] % 2 == 0:       
        e+=i
    else:
        o+=i

print("even=",e)
print("odd=",o)


# In[57]:


li=["Mumbai","Hyd","delhi","Dubai","Jaipur","Kolkata","Dadar","Danish"]
a=[]
for i in li:
    if i[0]=="D" or i[0]=="d":
        a.append(i)
print(a)


# In[60]:


li=["Mumbai","Hyd","delhi","Dubai","Jaipur","Kolkata","Dadar"]
l=[50,40,30,20,100,350,280,200]
c= dict(zip(li, l))
print(c)


# In[ ]:




