# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:15:31 2020

@author: tanupatsurface
"""


#http://py4e-data.dr-chuck.net/comments_372616.json

import urllib.request, urllib.parse, urllib.error
import json 


url = input('Enter location: ')
print('Retrieving', url)
data = urllib.request.urlopen(url).read()
print('Retrieved', len(data), 'characters')
js  = json.loads(data)

count = 0
total = 0
for user in js['comments']:
    count += 1
    total += user['count']
    
print('Count:', count)
print('Sum:', total)