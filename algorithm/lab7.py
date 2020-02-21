# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:16:14 2020

@author: tanupatsurface
"""
# lab 7 divide and conquer
def double(l):
    print(l)
    if len(l) ==1:
        return l[0]
    mid = len(l)//2
    left = l[:mid]
    right = l[mid:]
    if len(l)%2 != 0:
        if left[-1] != right[0]:
            if len(left)%2 == 0:
                return double(right)
            else:
                return double(left)
        else:
            if len(left)%2 == 0:
                return double(left[:-1])
            else:
                return double(right[1:])
  
    

l1 = [1, 1, 2, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8]
l2 = [10, 10, 17, 17, 18, 18, 19, 19, 21, 21, 23]
l3 = [1, 3, 3, 5, 5, 7, 7, 8, 8, 9, 9, 10, 10]
print(double(l1))
print(double(l2))
print(double(l3))