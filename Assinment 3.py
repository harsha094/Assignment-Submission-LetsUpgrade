#!/usr/bin/env python
# coding: utf-8

# In[1]:


data = data2 = "" 
  
# Reading data from file1 
with open('file1.txt') as fp: 
    data = fp.read() 
  
# Reading data from file2 
with open('file2.txt') as fp: 
    data2 = fp.read() 
  
# Merging 2 files 
# To add the data of file2 
# from next line 
data += "\n"
data += data2 
  
with open ('file3.txt', 'w') as fp: 
    fp.write(data) 


# In[9]:


keys = [1,2,3,4,5]
values = ["a","b","c","d","e"]
dictionary = dict(zip(keys, values))
print(dictionary)
{1:"a",2:"b",3:"c",4:"d",5:"e"}


# In[ ]:




