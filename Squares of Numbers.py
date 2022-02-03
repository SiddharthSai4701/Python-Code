# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:31:18 2021

@author: sidvs
"""

"""
This program prints the squares of all numbers from 1 to 10
using both while and for loops
"""

# Using while loop
i = 1
while(i<=10):
    print("The square of %d is %d\n"%(i,pow(i,2)))
    i+=1
    
# Using for loop
for j in range(1,11):
    print("The square of %d is %d\n"%(j,pow(j,2)))