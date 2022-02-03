# -*- coding: utf-8 -*-
"""
Created on Sun Jul 11 23:46:04 2021

@author: sidvs
"""

num = int(input("Enter a number: "))  
  
# if num > 1:  
#     for i in range(2,num):  
#         if (num % i) == 0:  
#             print(num,"is not a prime number")  
#             print(i,"times",num//i,"is",num)  
#             break  
        
#     else:  
#         print(num,"is a prime number")  
        
         
# else:  
#     print(num,"is not a prime number") 
   
i=2 
if num>1:
    while(i<num):
        if(num%i)==0:
            print("NP")
            break
        else:
            print("P")
            break
else:
    print("NP")


