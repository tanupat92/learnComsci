# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:43:49 2020

@author: tanup
"""

## UPGMA

import numpy as np
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram

def makeDistDf(list_keys, list_val):
    dic = dict(list(zip(list_keys, list_val)))
    distDf = pd.DataFrame(dic)
    distDf.index = list_keys
    return distDf

def upgma(distDf):
    result = {}
    while distDf.shape[1] >1:
        lowest = min([a for a in distDf.min(axis = 0)])
        coord = [(i,) + (distDf.columns[np.where(distDf[i] == lowest)[0]][0],) for i in distDf if len(np.where(distDf[i] == lowest)[0]) > 0][0]
        left = [a for a in distDf.columns if a not in coord]
        bool = [distDf.columns[i] in left for i in range(len(distDf.columns))]
        distDfnew = distDf.loc[bool, bool]
        tmp = []
        for a in left:
            tmp.append((distDf[coord[0]][a]+distDf[coord[1]][a])/2)
        distDfnew[coord] = tmp
        distDfnew = distDfnew.append(pd.Series(tmp+[np.inf], index=distDfnew.columns), ignore_index = True)
        distDfnew.index = list(distDfnew.columns)
        result[coord] = lowest
        distDf = distDfnew
    return result


def buildDendrogram(e):
    G = nx.DiGraph()
    for i in range(len(e)):
        G.add_edge(list(e.keys())[i], list(e.keys())[i][0], weight = e[list(e.keys())[i]]/2)
        G.add_edge(list(e.keys())[i], list(e.keys())[i][1], weight = e[list(e.keys())[i]]/2)
    nodes       = G.nodes()
    leaves      = set( n for n in nodes if G.out_degree(n) == 0 )
    inner_nodes = [ n for n in nodes if G.out_degree(n) > 0 ]

    subtree = dict( (n, [n]) for n in leaves )
    for u in inner_nodes:
        children = set()
        node_list = [n for n in G[u]]
        while len(node_list) >0:
            v = node_list.pop(0)
            children.add(v)
            node_list += [n for n in G[v]]
        subtree[u] = sorted(children & leaves)

    inner_nodes.sort(key=lambda n: len(subtree[n])) # <-- order inner nodes ascending by subtree size, root is last

    leaves = sorted(leaves)
    index  = dict( (n, i) for i, n in enumerate(leaves+inner_nodes) )

    Z = []
    for u in inner_nodes:
        i = [n for n in G[u]][1]
        j = [n for n in G[u]][0]
        if i in leaves:
            z = G[u][i]['weight']
        else:
            z = G[u][j]['weight']
        s = len(subtree[u])
        Z.append([index[i],index[j],z,s])
    dendrogram(Z, labels=leaves)
    plt.show()

a = [np.inf, 8, 7, 12]
b = [8, np.inf, 9, 14]
c = [7, 9, np.inf , 11]
d = [12, 14, 11, np.inf]
list_k1 = ['a','b','c','d']
list_v1 = [a,b,c,d]

A = [np.inf, 2, 4, 6, 6, 8]
B = [2, np.inf, 4, 6, 6, 8]
C = [4, 4, np.inf, 6, 6, 8]
D = [6, 6, 6, np.inf, 4, 8]
E = [6, 6, 6, 4, np.inf, 8]
F = [8, 8, 8, 8, 8, np.inf]
list_k2 = ['A', 'B','C','D','E','F']
list_v2 = [A,B,C,D,E,F]

distDf1 = makeDistDf(list_k1, list_v1)
distDf2 = makeDistDf(list_k2, list_v2)

e1 = upgma(distDf1)
print(e1)
e2 = upgma(distDf2)
print(e2)

buildDendrogram(e1)
buildDendrogram(e2)
