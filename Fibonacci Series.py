# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 14:13:00 2021

@author: sidvs
"""

"""
WAP to print the first n terms of the Fibonacci series (n>2)

0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""

n = int(input("Enter the number of terms you want in the series: "))
a = 0
b = 1

# Using for loop

# for i in range(n+1):
#     c = a+b
#     print(c)
#     a = b
#     b = c
 
# Using while loop
    
i = 0
while(i<=n):
    c = a+b
    print(c)
    a = b
    b = c
    i+=1
