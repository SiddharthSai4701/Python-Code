# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 16:06:52 2021

@author: sidvs
"""

s1 = input("Enter a string: ")
s1=s1.upper()
s2=""

# # Using for loop
# for i in range(1,len(s1)+1):
#     s2=s2+s1[-i]
    
# if s1==s2:
#     print(s1,"is a palindrome")
    
# else:
#     print(s1,"is not a palindrome")

#Using while loop
i=1
while i<=len(s1)/2:
    s2=s2+s1[-i]
    i+=1
    
if s1==s2:
    print(s1,"is a palindrome")
    
else:
    print(s1,"is not a palindrome")

