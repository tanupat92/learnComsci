# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 15:56:06 2020

@author: tanup
"""

import networkx as nx

s = { 'ATG', 'TGC', 'GTG', 'TGG', 'GGC', 'GCA', 'GCG', 'CGT'}
G = nx.DiGraph()
B = []
for a in s:
    G.add_edge(a[:2], a[-2:])
nx.draw_networkx(G, with_labels = True, pos= nx.circular_layout(G), node_color='white')
C = list(nx.eulerian_path(G))
result = ''
for a in C:
    result = result+a[0][0]
result = result+C[-1][1]
print(result)