# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 22:52:53 2021

@author: sidvs
"""
# For bianry search to apply, list must be sorted

def binary_search(l,x,start,end):
    # Base case: 1 element
    if start == end:
        if l[start] == x:   # can use end also since 
            return start    # the two are equal
        else:
            return -1
    else:
        # Divide the array into halves
        mid = int((start+end)/2)
        if l[mid] == x:
            return(mid)
        elif l[mid] > x:
            # Left half
            # We now check from the beginning till one place before the mid value
            return binary_search(l,x,start,mid-1)
        else:
            # Right half
            # We now check from the beginning till one place after the mid value
            return binary_search(l, x, mid+1, end)
l = [20,45,60,70,90]
x=int(input("Enter search key: "))
dex = binary_search(l, x, 0, len(l)-1)
if dex==-1:
    print(x, " is not found")
else:
    print(x," is found at position ",dex+1)