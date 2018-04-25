# -*- coding: utf-8 -*-

import random
import wows
import time
from botfunction import *

def onQQMessage(bot, contact, member, content):
    if content == '--hello':
        bot.SendTo(contact, '你好，我是QQ机器人')
    elif content == '--stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()

    if content == '?news':
        bot.SendTo(contact, news())
        time.sleep(0.1)
        return

    if content == '?help':
        string = '''欢迎使用智障复读机器人（兼睿智窝窝屎bot）\n主要功能：\n1.低概率复读群员对话，极低概率自动加上“还行”\n2.窝窝屎水表，请使用命令“水表?username server” 服务器列表["NA","ASIA","RU","EU"],不写或出错默认美服\n3.窝窝屎美服新闻，请使用命令“?news”获取最新的三条新闻'''
        bot.SendTo(contact, string)
        time.sleep(0.1)
        return
        
    if '@ME' in content:
        bot.SendTo(contact, "别喊我，不复读都是因为你脸黑")
        return

    if bot.isMe(contact, member):
        time.sleep(0.1)
        return
    
    if content.endswith('还行')  and not content == '还行':
        learn(content)

        if random.random() < 0.2 and not '/表情' in content:
            bot.SendTo(contact, content)
            return

    if content == '?单抽':
        bot.SendTo(contact, drawcard(0))
    elif content == '?十连':
        bot.SendTo(contact, drawcard(1))

    elif content.startswith("水表?") or content.startswith("水表？"):
        user = content[3:]
        (bts, wr, pr) = wows.getWOWS(user)

        if bts == -1:
            bot.SendTo(contact, "网络错误")
            return
        elif bts == -2:
            bot.SendTo(contact, "查不到")
            return

        # if wr <= 0.47:
        #     bot.SendTo(contact, "是菜鸡")

        wr = format(wr,'.2%')

        bot.SendTo(contact, "场次 " + str(bts) +
                   ", 胜率 " + str(wr) + ", 评级 " + str(pr))

    else:
<<<<<<< HEAD
        if content.endswith('还行')  and not content == '还行':
            learn(content)


        if content == '?单抽':
            bot.SendTo(contact, drawcard(0))
        elif content == '?十连':
            bot.SendTo(contact, drawcard(1))

        elif content.startswith("水表?") or content.startswith("水表？"):
            string = content[3:]
            user = string.split(" ")[0]
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

        else:
            ran = random.random()
            if ran < 0.05 and not '/表情' in content:
                if ran < 0.015:
                    bot.SendTo(contact, content + "还行")
                else:
                    if content != '':
                        bot.SendTo(contact, content)
=======
        ran = random.random()
        if ran < 0.05 and not '/表情' in content and not '@' in content:
            if ran < 0.015:
                bot.SendTo(contact, content + "还行")
            else:
                if content != '':
                    bot.SendTo(contact, content)
>>>>>>> ee429101378c01e9ee68802ba45a4bd78f17e87a
