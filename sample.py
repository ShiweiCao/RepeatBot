# -*- coding: utf-8 -*-

import random
import wows
import time
from botfunction import *

last_repeated = ""
p = 0.03

def onQQMessage(bot, contact, member, content):
    global last_repeated
    global p

    # bot control
    if content == '--hello':
        bot.SendTo(contact, '你好，我是QQ机器人')
    elif content == '--stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()

    # isMe?
    if bot.isMe(contact, member) or (contact.ctype != 'buddy' and member.qq == bot.conf.qq):
        time.sleep(0.1)
        return

    # @ME message
    if '@ME' in content:
        bot.SendTo(contact, "别喊我，不复读都是因为你脸黑")
        return
    elif '@' in content:
        return

    # Debug module
    if content == '?debug':
        status = "P: " + str(p) + ", last repeated: " + last_repeated
        bot.SendTo(contact, status)
        time.sleep(0.1)
        return

    # News module (NA)
    if content == '?news':
        bot.SendTo(contact, news())
        time.sleep(0.1)
        return

    # Help module
    if content == '?help':
        string = '''欢迎使用智障复读机器人（兼睿智窝窝屎bot）\n主要功能：\n1.低概率复读群员对话，极低概率自动加上“还行”\n2.窝窝屎水表，请使用命令“水表?username server” 服务器列表["NA","ASIA","RU","EU"],不写或出错默认美服\n3.窝窝屎美服新闻，请使用命令“?news”获取最新的三条新闻\n\n作者：美服[MEOW]公会，欢迎巨佬莅临指导，群号682058320，Discord:https://discord.gg/tBNBr28'''
        bot.SendTo(contact, string)
        time.sleep(0.1)
        return

    # Draw card module
    if content == '?单抽':
        bot.SendTo(contact, drawcard(0))
    elif content == '?十连':
        bot.SendTo(contact, drawcard(1))


    # WoWs player data
    if content.startswith("水表?") or content.startswith("水表？"):
        string = content[3:]
        user = string.split(" ")[0].strip()
        serList = ["NA","ASIA","RU","EU"]

        try:
            if string.split(" ")[1] in serList:
                sever = string.split(" ")[1]
        except:
            sever = "NA"

        (bts, wr, pr) = wows.getWOWS(user, sever)

        if bts == -1:
            bot.SendTo(contact, "网络错误")
            return
        elif bts == -2:
            bot.SendTo(contact, "查不到")
            return

        wr = format(wr,'.2%')
        bot.SendTo(contact, "场次 " + str(bts) +
                ", 胜率 " + str(wr) + ", 评级 " + str(pr))

    # Repeat
    if content == last_repeated:
        pass
    elif content.endswith('还行') and not content == '还行':
        learn(content)

        if random.random() < 0.2 and not '/表情' in content:
            last_repeated = content
            bot.SendTo(contact, content)
            return
    elif random.random() < p and not '/表情' in content:
        p = 0.03

        if random.random() < 0.2:
            last_repeated = content + "还行"
            bot.SendTo(contact, content + "还行")
        elif content != '':
            last_repeated = content
            bot.SendTo(contact, content)
    else:
        p = min(p / (1.0 - p), 0.5)