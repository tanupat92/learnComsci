# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:24:23 2020

@author: tanupatsurface
"""

import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
# University of Arkansas
while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = serviceurl + urllib.parse.urlencode({'address': address, 'key' :'AIzaSyC8d4ILpK_AqQ5wDMrXLbnhUYt7A7vj0ug' })
    
    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    #print(uh.read())
    data = uh.read().decode()
    #print(data)
    print('Retrieved', len(data), 'characters')
    
    try:
        js = json.loads(data)
    except:
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    
    #print(json.dumps(js, indent=4))
    
    placeid = js['results'][0]["place_id"]

    print('Place id', placeid)
    