# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

## Midterm lab exam 

# have object weight list w =[5,10,15,22,25] with value v=[30,40,45,77,90]
# and maximum weight that can be put in a bag is W 
# put object in a bag that has highest total value (use greedy)
v = [30,40,45,77,90]
w = [5,10,15,22,25]
W = 60

def knapsack(W,w,v):
    mydic = {}
    mydic2 = {}
    for i in range(len(v)):
        mydic[w[i]] = (v[i], v[i]/w[i])
        mydic2[w[i]] = (v[i], v[i]/w[i])
    bag = []
    while sum(bag) < W:
        val = max([a[1] for a in mydic.values()])
        for key in mydic.keys():
            if mydic[key][1] == val:
                bag.append(key)
                k = key
        del(mydic[k])
    
    print('Total value:', sum([mydic2[a][0] for a in bag]))
    print('Item:', bag) 
knapsack(W,w,v)

# use dynamic programming to find largest 1s square subset matrix of given square matrix
def largestsquare(mat):
    s = [[0]*len(mat) for a in range(len(mat))]
    for i in range(len(mat)):
        if mat[0][i] == 1:
            s[0][i] =1
        if mat[i][0] ==1:
            s[i][0] =1
    print(s)
    for i in range(1,len(mat)):
        for j in range(1,len(mat)):
            if mat[i][j] ==1 :
                s[i][j] = min(s[i][j-1], s[i-1][j], s[i-1][j-1]) +1
    print(s)
    return max(max([a for a in s]))
                
mat = [[0,1,1,0,1,1],[1,1,0,1,1,1],[0,1,1,1,0,0],[1,1,1,1,0,0],[1,1,1,1,1,0],[0,1,1,1,0,1]]
print(largestsquare(mat))

# use divide and conquer to identify whether this list is homogeneous or not
def dc(l):
    def dandc(l):
        if len(l) ==2:
            return (l[0] == l[1], l[0])
        if len(l) ==1:
            return (True, l[0])
        mid = len(l)//2
        left = dandc(l[:mid])
        right = dandc(l[mid:])
        return (left[0] and right[0] and (left[1] ==right[1]), l[0]) 
    return dandc(l)[0]
print(dc([1,1,1,1,1,1,1]))
print(dc([1,2,2,2]))