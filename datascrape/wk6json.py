# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:21:57 2020

@author: tanupatsurface
"""

import json
data = '''{
    "name":"Chuck",
    "phone" : {
            "type" : "intl",
            "number" : "+1 734 303 4456"
            },
    "email" : {
            "hide" : "yes"
            }
    }'''

info = json.loads(data) #become python dictionary
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])


inp = '''[
    {"id" : "001",
    "x" : "2",
    "name" : "Chuck"
    },
    {"id" : "009",
    "x" : "7",
    "name" : "Chuck"
    }
    ]'''
inf = json.loads(inp) # become list of 2 dicts
print('User count:', len(inf))
for item in inf:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])