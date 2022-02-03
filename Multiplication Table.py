# -*- coding: utf-8 -*-
"""
Created on Wed Oct  6 16:37:15 2021

@author: sidvs
"""

"""
This program prints the multiplication table of a number n
"""

n = int(input("Enter the number whose table you want: "))
m = int(input("Enter the final multiple of %d that you want: "%(n)))

# Using while loop

# i = 1
# while(i<=m):
#     print("%d x %d = %d"%(n,i,n*i))
#     i+=1

# Using for loop

for i in range(1,m+1):
    print("%d x %d = %d"%(n,i,n*i))