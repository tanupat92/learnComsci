# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 15:17:37 2020

@author: BDJ
"""

import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse 
import urllib.error
import pickle
import pandas as pd
completeLinks = set() 
edgelist = [] # [('ธีรเดช','บุษกร')]
vertexAttr = {} # JSON style ie. {'ธีรเดช วงศ์พัวพันธ์':{'วันเกิด':'22 มิถุนายน พ.ศ.2510'}}
thainum = ['๐','๑','๒','๓','๔','๕','๖','๗','๘','๙']
thainumcoded = ['\%E0\%B9\%90',
 '\%E0\%B9\%91',
 '\%E0\%B9\%92',
 '\%E0\%B9\%93',
 '\%E0\%B9\%94',
 '\%E0\%B9\%95',
 '\%E0\%B9\%96',
 '\%E0\%B9\%97',
 '\%E0\%B9\%98',
 '\%E0\%B9\%99']
def glanceAge(url):
    try:
        html = urlopen('https://th.wikipedia.org{}'.format(url))
        bs = BeautifulSoup(html, 'html.parser')
    except urllib.error.HTTPError :
        return False
    except urllib.error.URLError:
        return False
    try:
        bs.find(lambda tag: tag.get_text()=='เกิด').next.next.next.next.find('font').get_text()
        #ht = bs.find(lambda tag: tag.get_text()=='ส่วนสูง').next.next.next.next.get_text()
    except AttributeError:
        return False
    return True
def movenext(previousUrl):
    '''previousUrl is /wiki/.....
    '''
    try:
        html = urlopen('https://th.wikipedia.org{}'.format(previousUrl))
    except urllib.error.HTTPError :
        return True
    except urllib.error.URLError:
        return True
    bs = BeautifulSoup(html, 'html.parser')
    title = bs.find('h1', {'id':'firstHeading'}).get_text()
    print(title)
    try:
        s = bs.find(lambda tag: tag.get_text()=='เกิด').next.next.next.next.find('font').get_text()
        #ht = bs.find(lambda tag: tag.get_text()=='ส่วนสูง').next.next.next.next.get_text()
    except AttributeError:
        return True 
    age = int(re.search('([0-9]+)', s).group(1)) 
    #height = int(re.search('([0-9]+)', ht).group(1))
    attr = {}
    attr['age'] = age
    #attr['height'] = height 
    vertexAttr[title] = attr   
    for a in bs.find_all('table', {'class':'navbox'}):
        a.decompose()
    links = bs.find('div', {'id':'bodyContent'}).find_all('a', href = re.compile('^(/wiki/)((?!:).)*$'))
    couple = [(title, a) for a in links]
    while len(couple) > 0 :
        link = couple.pop(0)
        url = link[1].attrs['href']  
        if len(re.findall('_', url)) >0 and glanceAge(url) and len(re.findall('\.|[0-9]{4}',url)) == 0 :
            #and sum([len(re.findall(a, url))>0 for a in thainumcoded]) == 0:
            edge = (link[0], link[1].attrs['title'])
            edgelist.append(edge)
            print(edge)
            print(len(edgelist))
            if url not in completeLinks:
                try:
                    html = urlopen('https://th.wikipedia.org{}'.format(url))
                    completeLinks.add(url)
                except urllib.error.HTTPError :
                    continue
                except urllib.error.URLError:
                    continue
                bs = BeautifulSoup(html, 'html.parser')
                title = bs.find('h1', {'id':'firstHeading'}).get_text()
                print(title)
                try:
                    s = bs.find(lambda tag: tag.get_text()=='เกิด').next.next.next.next.find('font').get_text()
                except AttributeError:
                    continue
                age = int(re.search('([0-9]+)', s).group(1)) 
                attr = {}
                attr['age'] = age
                vertexAttr[title] = attr        
                if len(bs.find_all('table', {'class':'navbox'}))>0:
                    for a in bs.find_all('table', {'class':'navbox'}):
                        a.decompose()
                links = bs.find('div', {'id':'bodyContent'}).find_all('a', href = re.compile('^(/wiki/)((?!:).)*$'))
                tmp = [(title, a) for a in links]
                couple = couple + tmp 
                print(len(couple))
            if len(edgelist)%200 == 0:
                with open('edgelist','wb') as edgeli:
                    pickle.dump(edgelist,edgeli)
                with open('verAttr', 'wb') as verat:
                    pickle.dump(vertexAttr, verat)
    
uurl = '/wiki/%E0%B8%98%E0%B8%B5%E0%B8%A3%E0%B9%80%E0%B8%94%E0%B8%8A_%E0%B8%A7%E0%B8%87%E0%B8%A8%E0%B9%8C%E0%B8%9E%E0%B8%B1%E0%B8%A7%E0%B8%9E%E0%B8%B1%E0%B8%99%E0%B8%98%E0%B9%8C'
movenext(uurl)


#fromnode = [a[0] for a in edgelist] 
#tonode = [a[1] for a in edgelist]
#vertexname = list(vertexAttr.keys())
#vertexage = [int(vertexAttr[a]['age']) for a in vertexname]
#edgeDf = pd.DataFrame({'from':fromnode, 'to':tonode})
#edgeDf2 = edgeDf.groupby(['from','to']).to.agg('count').to_frame('weight').reset_index()
#edgeDf2.to_csv('fulledge.csv')
#vertexDf = pd.DataFrame({'name':vertexname, 'age':vertexage})
#vertexDf.to_csv('fullvertex.csv')
