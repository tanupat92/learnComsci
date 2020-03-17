# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:20:50 2020

@author: tanup
"""
import networkx as nx
import numpy as np 
import matplotlib.pyplot as plt
import math
mat = np.array([[0,10,5,15,0,0,0,0],[0,0,4,0,9,15,0,0],[0,0,0,4,0,8,0,0],[0,0,0,0,0,0,30,0],
       [0,0,0,0,0,15,0,10],[0,0,0,0,0,0,15,10],[0,0,6,0,0,0,0,10],[0,0,0,0,0,0,0,0]])
G = nx.from_numpy_array(mat, create_using = nx.DiGraph)
G = nx.relabel_nodes(G, {0:'s',1:2,2:3,3:4,4:5,5:6,6:7,7:'t'})
G.nodes 
G.edges(data=True)
nx.draw_networkx(G, with_labels = True, width = weight)

def dijkstra(g, s, t):
    for n in G.nodes:
        G.nodes[n]['dist'] = math.inf
    G.nodes[s]['dist'] = 0 
    for n in G.nodes:
        G.nodes[n]['previous'] = []
    G.nodes[s]['previous'].append(s)
    q = list(G.nodes)
    while len(q)>0 :
        u = min([(k, at['dist']) for k, at in G.nodes.items() if k in q], key = lambda t: t[1])[0]
        q.remove(u)
        if u != t:
            for nei in G[u]:
                alt = G.nodes[u]['dist'] + G[u][nei]['weight']
                if alt < G.nodes[nei]['dist']:
                    G.nodes[nei]['dist'] = alt 
                    G.nodes[nei]['previous'] = G.nodes[u]['previous'] + [nei]
        else:
            return G.nodes[t]['previous']
print(dijkstra(G,'s', 't'))