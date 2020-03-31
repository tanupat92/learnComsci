# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:32:33 2020

@author: tanup
"""
import statistics as st
import random 

def distance(a,b):
        n = len(a)
        dist = 0 
        for i in range(n):
            dist += (b[i]-a[i])**2
        return dist**(1/n)

def cost(cluster):
    centroid = ()
    if len(cluster) == 1:
        return 0
    #print('cluster', cluster)
    for i in range(len(cluster[0])):
        centroid = centroid + (st.mean([a[i] for a in cluster]),)
    dist = 0
    for p in cluster:
        dist += distance(p, centroid)
    return dist

def overallCost(clusters):
    #print('overall', [cost(c) for c in clusters])
    return sum([cost(c) for c in clusters])

def partition(points, k):
    n = len(points)
    random.shuffle(points)
    clusters = []
    for i in range(k-1):
        cluster = points[i*(n//k):(i+1)*(n//k)]
        clusters.append(cluster)
    clusters.append(points[(k-1)*(n//k):])
    return clusters

def switching(clusters, switch):
    '''
    >>> clusters = [[1,2,3], [4,5,6],[7,8,9]]
    >>> switch = [(1,[4,5,6]),(2,[7,8,9]),(7,[1,2,3]),(8,[4,5,6])]
    >>> switching(clusters, switch)
    [[3,7],[4,5,6,1,8], [9,2]]
    '''
    clusters2 = [c.copy() for c in clusters].copy()
    for i in range(len(clusters)):
        s = [s[0] for s in switch if s[0] in clusters[i]]
        h = [s[0] for s in switch if s[1] == clusters[i]]
        for a in s:
            clusters2[i].remove(a)
        for a in h:
            clusters2[i].append(a)
    return clusters2 
    
def greedyKmean(points, k):
    clusters = partition(points,k)
    while True:
        bestChange = 0
        oldCost = overallCost(clusters)
        switch = []
        for cluster in clusters:
            for p in [a for c in clusters if c != cluster and len(c)>1 for a in c]:
                tmpSwitch = (p, cluster)
                #print('clusters', clusters)
                newCost = overallCost(switching(clusters, [tmpSwitch]))
                #print(oldCost, newCost, oldCost-newCost, bestChange)
                if oldCost-newCost > bestChange and len(switch) <1:
                    bestChange = oldCost - newCost
                    switch += [(p,cluster)]
                    #print('switch',switch)
        if bestChange > 0:
            clusters = switching(clusters, switch)
            #print(clusters)
        else:
            return clusters 
        
points = [(5,5), (6,6), (7,7), (-15,-15), (-16,-16), (13,-13), (12,-12), (-17,71), (-8,81), (-10, 90)]
print(greedyKmean(points, 4))

    