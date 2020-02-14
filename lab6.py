# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 12:00:09 2020

@author: tanupatsurface
"""
import math
import re
def square(num):
    maxi = math.floor(num**0.5)
    possible = [a for a in range(1,maxi+1)]
    
    def rec(num, result, maxi):
        if num == 0:
            return len(result)
        if result != []:
            #print('maxi', maxi, num)
            s = math.floor(num**0.5)
            if  s < maxi:
                maxi = s 
        result.append(maxi**2)
        #print(result) 
        return rec(num-maxi**2, result, maxi)
    
    return min([rec(num, [], c) for c in possible])
    
def dp(num):
    maxi = math.floor(num**0.5)
    possible = [a**2 for a in range(1,maxi+1)]
    ourdict = {}
    ourdict[0] = 0
    for a in range(1,num+1):
        ourdict[a] = float('inf')
        for c in possible:
            if a >= c:
                if ourdict[a-c] +1 < ourdict[a]:
                    ourdict[a] = ourdict[a-c]+ 1
    return ourdict[num]

def dp2(num):
    maxi = math.floor(num**0.5)
    possible = [a**2 for a in range(1,maxi+1)]
    ourdict = {}
    ourdict[0] = (0,[])
    for a in range(1,num+1):
        ourdict[a] = (float('inf'),[])
        for c in possible:
            if a >= c:
                if ourdict[a-c][0] +1 < ourdict[a][0]:
                    ourdict[a] = (ourdict[a-c][0]+1, ourdict[a-c][1] + [c])
    return ourdict[num]

ourdict = {6:3,79:4,80:2,100:1,180:2}

def run(dicti, function):
    print('our function is', function.__name__)
    for a in dicti.keys():
        result = function(a)
        print(result, 'numbers')
        if re.search('2', function.__name__):
            print('equal=', result[0]==dicti[a])
        else:
            print('equal=', result==dicti[a])

run(ourdict, square)
run(ourdict, dp)
run(ourdict, dp2)
