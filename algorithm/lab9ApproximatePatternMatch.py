# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:40:09 2020

@author: tanup
"""

# write a program for removing duplicate entry in a list of integer in linear time complexity

from doctest import testmod 

def dedup(x):
    ''' input is a list of integer, output is a string without duplicates
    >>> dedup([1,2,3,4,5,6,7,8,8,9,10,10,10,20, 5,5, 0,0])
    '1 2 3 4 5 6 7 8 9 10 20 0'
    '''
    dic = {}
    for i in range(len(x)):
        if x[i] not in dic.keys():
            dic[x[i]] = []
        dic[x[i]] = dic[x[i]] + [i]
    s = " "
    return s.join([str(a) for a in list(dic.keys())])

    

def approxPatternMatching(p,t,k):
    ''' t = text, p = pattern , k = penalty
    output is tuple of number of matches and list of position of t
    >>> t = '11111111111122334411111111'
    >>> p = '223345'
    >>> k = 1
    >>> approxPatternMatching(p,t,k)
    (1, [12])
    '''
    n = 0
    m = []
    
    def match(a,b,k):
        ''' a and b have same length of text and output is boolean if match with penalty less than k'''
        c = 0 
        for i in range(len(a)):
            if a[i] == b[i]:
                c+=1
        if len(a)-c <= k:
            return True
        else: 
            return False
    
    for i in range(len(t)-len(p)+1):
        if match(p, t[i:i+len(p)], k):
            n += 1
            m.append(i)
    return (n, m)

testmod(name ='approxPatternMatching', verbose = True) 
    