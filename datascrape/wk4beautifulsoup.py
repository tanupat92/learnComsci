# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 11:24:09 2020

@author: tanupatsurface
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input('Enter -')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    
    print(tag)
    #print(tag.get('href',None))
    
    