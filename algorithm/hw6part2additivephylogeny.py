# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:58:26 2020

@author: tanup
"""

import numpy as np
import pandas as pd
import math
import networkx as nx
def makeDistDf(list_keys, list_val):
    dic = dict(list(zip(list_keys, list_val)))
    distDf = pd.DataFrame(dic)
    distDf.index = list_keys
    return distDf


a = [-np.inf, 8, 7, 12]
b = [8, -np.inf, 9, 14]
c = [7, 9, -np.inf , 11]
d = [12, 14, 11, -np.inf]
list_k1 = ['a','b','c','d']
list_v1 = [a,b,c,d]

A = [-np.inf, 4, 10, 9]
B = [4, -np.inf, 8, 7]
C = [10, 8, -np.inf, 9]
D = [9, 7, 9, -np.inf]
list_k2 = ['A', 'B','C','D']
list_v2 = [A,B,C,D]

distDf1 = makeDistDf(list_k1, list_v1)
distDf = makeDistDf(list_k2, list_v2)

#A = [-np.inf, 2, 1]
#B = [2, -np.inf, 1]
#C = [1, 1, -np.inf]
#list_k = ['A','B','C']
#list_v = [A,B,C]
#distDf = makeDistDf(list_k, list_v)

def degenerativeMat(distDf):
    name = list(distDf.columns)
    for i in name:
        for j in name:
            if j != i:
                for k in name:
                    if k not in [i,j]:
                        if distDf[i][j] + distDf[j][k] == distDf[i][k]:
                            return (True, i, j, k)
                        
    return (False,)
                        
def additivePhylogeny(distDf):
    def buildTree(distDf):
        if distDf.shape == (2,2):
            weight = distDf.iloc[0,1]
            Gra = nx.Graph()
            node= list(distDf.columns)
            Gra.add_edge(node[0], node[1], weight = weight)
            print('first', Gra.edges.data('weight'))
            return Gra
        elif degenerativeMat(distDf)[0] ==False:
    
            for n in range(2, int(math.ceil(np.max(distDf)[0])),2):
                distDfnew = distDf - n
                d = degenerativeMat(distDfnew)
        
                if d[0] == True:
                    delta = n
                    i, j, k = (d[1], d[2], d[3])
                    distDf = distDfnew
                    break
        else:
            delta = 0 
            d = degenerativeMat(distDf)
            i, j, k = (d[1], d[2], d[3])
        
        x = distDf[i][j]
        left = [a for a in list(distDf.columns) if a != j]
        distDf2 = distDf.loc[left,left]
        print('pre', distDf2)
        G = buildTree(distDf2)
        print('distDf', distDf)
        v = j+'new'
        print(i,j,k,v,x)
        #for n in G.nodes:
        #avail = {x for a in nx.all_simple_paths(G, 'A','C') for x in a}
        #if G[]
        paths = list(nx.all_simple_paths(G, i, k))
        for path in paths:
            if len(path) >2:
                k = path[1]
        if (i,k) in G.edges:
            G.remove_edge(i,k)
        G.add_edge(v, j, weight = 0)
        G.add_edge(k, v, weight = x) 
        G.add_edge(i, v, weight = x) 
        print(G.edges)
        print('last', G.edges.data('weight'))
        
        for u, v, weight in G.edges.data('weight'):
            if u in name or v in name:
                G[u][v]['weight'] += delta/2
        
        return G
    name = list(distDf.columns)
    G = buildTree(distDf)
    Gresult = G.copy()
    for u, v, weight in G.edges.data('weight'):
        if u in name and v in name:
            Gresult.remove_edge(u,v)
    return Gresult
    
G = additivePhylogeny(distDf)
pos = nx.spring_layout(G)
nx.draw(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edge_labels(G, pos, labels = edge_labels)
