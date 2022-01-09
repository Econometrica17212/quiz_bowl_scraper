# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import scrapy
import requests
import re
from bs4 import BeautifulSoup

#flow control

ACF = 1
NAQT = 1

level = "College"
hsqb_query = "ACF"
naqt_query = "SCT"


if(ACF == 1):
    
    to_visit = set()
    response = requests.get("https://hsquizbowl.org/db/tournaments/search/?dist=&loc=&state=&level=&name=ACF&host=&dates=past&startdate=&enddate=")
    #A hard-coded url which has search results from all tournaments with ACF in the name.
    soup = BeautifulSoup(response.content, 'html.parser')
    for url in soup.find_all('a'):
        to_visit.add(url.get('href'))
        print(url.get('href'))
    print(to_visit)
    
    good_links = to_visit
    for url in good_links:
        
        tourn_pattern = '^tournaments/....+/$'
        search_page_pattern = '^tournaments/search/+[1-50]'
        
        print(re.findall(pattern = search_page_pattern, string = url))


if(NAQT == 1):
    print("null")