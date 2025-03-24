# Maygan Book
# March 24/2025
# Lesson 16
# Working with lists 

import random 
numlist=[]
for i in range(100):
    num=random.randint(0,100)
    numlist.append(num)
print(numlist)
avg=sum(numlist)/100 
print(" your average is:" , avg)

