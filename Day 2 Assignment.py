#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Initializing list  
test_list = [5, 6, [], 3, [], [], 9] 
  
# printing original list  
print("The original list is : " + str(test_list)) 
  
# Remove empty List from List 
# using filter 
res = list(filter(None, test_list)) 
  
# printing result  
print ("List after empty list removal : " + str(res)) 


# In[2]:


s = "Python is great and Java is also great"
l = s.split() 
k = [] 
for i in l: 
  
    # If condition is used to store unique string  
    # in another list 'k'  
    if (s.count(i)>1 and (i not in k)or s.count(i)==1): 
        k.append(i) 
print(' '.join(k))


# In[3]:


inp_str = "GeeksforGeeks"
  
# frequency dictionary 
freq = {}  
    
for ele in inp_str:  
    if ele in freq:  
        freq[ele] += 1
    else:  
        freq[ele] = 1
    
# printing result   
print ("Occurrence of all characters in GeeksforGeeks is :\n "+ str(freq))  


# In[ ]:




