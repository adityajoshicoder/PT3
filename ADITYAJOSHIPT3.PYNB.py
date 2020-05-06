#!/usr/bin/env python
# coding: utf-8

#     ADITYA  JOSHI
#     B.Tech CSE 4A
#     2K18CSUN01002
#     Python PT3
# 
# [Theoritical Questions]
# 
# 1. What is the syntax to call a constructor of a base class from child class
# 
#              Class Employee(self,firstname,lasname):
#                  def _init_(self,firstname,lastname)
#                  super()._init_(firstname,lastname)
# 
# 
# 2. How is a class made as inherited class (syntax of child class) 
#              class ParentClass:
#                    Body of parent class
#              class ChildClass(ParentClass):
#                    Body of child class
# 
# 
# 3. Print an element of a nested dictionary 
# 
# 
#              Dictionary= {1:'A',2:'B',3:('C','D'),4:['E','F','G','H'],5:{1:'X',2:'Y',3:'Z'}}
#              print(Dictionary[4])

# In[3]:


items = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0) :
        items.append(s)
print( ",".join(items))


# In[6]:


def calculateSum (a,b):
	s = int(a) + int(b)
	return s 


num1 = input("Enter 1st Number")
num2 = input("Enter 2nd Number")


sum = calculateSum(num1, num2)


print("Sum = ", sum)

