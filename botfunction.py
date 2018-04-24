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


def learn(content):
    with open("./.qqbot-tmp/plugins/learn.json","w+") as f:
        content = content.replace("还行","")
        content = content.strip()

        data = json.loads(f)
        a = set(data)

        a.add(content)

        json.dump(list(a),f)

