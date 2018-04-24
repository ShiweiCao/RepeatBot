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

    if '@ME' in content:
        bot.SendTo(contact, "别喊我，不复读都是因为你脸黑")
        return

    if bot.isMe(contact, member):
        time.sleep(0.1)
        return
    else:
        if content.endswith('还行')  and not content == '还行':
            if learn(content):
                print("已收录新的数据")

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
            ran = random.random()
            if ran < 0.05 and not '/表情' in content:
                if ran < 0.015:
                    bot.SendTo(contact, content + "还行")
                else:
                    if content != '':
                        bot.SendTo(contact, content)
