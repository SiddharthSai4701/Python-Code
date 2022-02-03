# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:42:28 2021

@author: sidvs
"""

"""
This program computes the sum of all even numbers from 2 to n
"""

n = int(input("Enter the upper end of the range: "))

# Using while loop

total = 0
# i = 2
# while(i<=n):
#     if(i%2==0):
#         total+=i
#     i+=1
        
# print("The sum is: ",total)

# Using for loop

for i in range(2,n+1):
    if(i%2==0):
        total+=i
print("The sum is: ",total)