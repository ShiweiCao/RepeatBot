# -*- coding: utf-8 -*-

import random
import json

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

