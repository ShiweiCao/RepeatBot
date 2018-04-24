# -*- coding: utf-8 -*-

import random
import json
import requests
import urllib.request
from bs4 import BeautifulSoup
import re

# 抽卡
def drawcard(choice):
    res = ""
    ran = random.random()
    if choice == 0:        
        if ran < 0.007:
            res += "抽到UP五星从者"
        elif ran < 0.01:
            res += "抽到五星从者，然而并不是UP"
        else:
            res +=  "没出货，懒得写了，反正不是五星从者"
    else:
        if ran < 0.068:
            res +=  "恭喜抽到UP五星从者"
        elif ran < 0.096:
            res +=  "抽到五星从者，然而并不是UP"
        else:
            res +=  "没出货，懒得写了，反正没出五星从者"
    return res

data = set()

try:
    with open("./.qqbot-tmp/plugins/learn.json","w+") as f:
        d = f.read()
        d = json.loads(d)
        data = set(d)
except:
    pass

def learn(content):
    content = content.replace("还行","").strip()

    if not content in data:
        data.add(content)
        
        with open("./.qqbot-tmp/plugins/learn.json","w+") as f:
            json.dump(list(data),f)

def news():
    string = ""
    response = urllib.request.urlopen('https://worldofwarships.com/')
    result = response.read()
    html = BeautifulSoup(result, 'html5lib')

    res = html.find(id = 'news-container')
    link = res.find('a')
    string += "worldofwarships.com" + link.get('href') + "\n"

    res = html.findAll(id = re.compile('news\-\d+'), limit=2)
    link = res[0].contents[1].find('a')
    string += "worldofwarships.com" + link.get('href') + "\n"

    link = res[1].contents[1].find('a')
    string += "worldofwarships.com" + link.get('href')
    return string

