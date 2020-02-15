# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:03:21 2020

@author: tanupatsurface
"""

#http://py4e-data.dr-chuck.net/comments_372615.xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter location: ')
data = urllib.request.urlopen(url).read()

tree = ET.fromstring(data)
lst = tree.findall('comments/comment')

total = 0
for a in lst:
    total = total + int(a.find('count').text)
    
print('Count:', len(lst))
print('Sum:', total)    