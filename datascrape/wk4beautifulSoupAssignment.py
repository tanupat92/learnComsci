# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:39:50 2020

@author: tanupatsurface
"""


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# http://py4e-data.dr-chuck.net/known_by_Danikah.html
url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))


for i in range(count+1):
    print('Retrieving', url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[position-1].get('href',None)
    
