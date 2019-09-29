# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 23:46:55 2019

@author: user
"""


from googlesearch import search_news
import urllib
from bs4 import BeautifulSoup
import pandas as pd
#import time

Bursa_MainList = pd.read_csv(r"C:\Users\user\Downloads\scraping\Bursa Main List.csv")
bursa_mainlist = pd.DataFrame(Bursa_MainList.iloc[:,[1]])
columns= list(bursa_mainlist)
#print(bursa_mainlist)

def google_scrape(url):
    
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib.request.urlopen( req )
    soup = BeautifulSoup(con, "html.parser")
    return soup.title.text

i = 1
Table_list=[]
table_names = pd.DataFrame()

for query in columns:
    print(query)
    for url in search_news(query, tbs='qdr:h'):
        print(url)
        req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
        con = urllib.request.urlopen( req )
        soup = BeautifulSoup(con, "html.parser")
        a = soup.title.text
        i += 1
        Table_list.append(a)
        
    #print (i,  a)
    #time.sleep(1)
    #print(Table_list)

table_append= table_names.append(Table_list)
table_append.to_csv("test.csv")

print(table_append)
#Table_list.to_csv("test" + ".csv")  