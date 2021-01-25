#!/usr/bin/env python
# coding: utf-8

# In[3]:
# Q1

lower = int(input("Enter first number"))
upper = int(input("Enter number upto which you want to print prime"))

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   
   if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            print (num)


# In[ ]:
# 

num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Sorry factorial does not exist for negative number")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num + 1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)
    


# In[ ]:


num = int(input("enter the number upto which you want to calculate sum"))
if num < 0:
    print("enter the positive number")
else:
    sum = 0
    while(num > 0):
        sum +=num
        num -=1
    print("The sum is ", sum)


# In[ ]:




