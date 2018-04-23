# -*- coding: utf-8 -*-

import random
import wows
import time

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
        return
    else:
        if content == '?单抽':
            ran = random.random()
            if ran<0.007:
                bot.SendTo(contact, "恭喜抽到UP五星从者")
            elif ran<0.01:
                bot.SendTo(contact, "抽到五星从者，然而并不是UP")
            else:
                bot.SendTo(contact, "没出货，懒得写了，反正不是五星从者")
        elif content == '?十连':
            ran = random.random()
            if ran<0.068:
                bot.SendTo(contact, "恭喜抽到UP五星从者")
            elif ran<0.096:
                bot.SendTo(contact, "抽到五星从者，然而并不是UP")
            else:
                bot.SendTo(contact, "没出货，懒得写了，反正没出五星从者")
        elif content.startswith("水表?"):
	        user = content[3:]
	        (bts, wr, pr) = wows.getWOWS(user)

	        if bts == -1:
                bot.SendTo(contact, "查不到")
                return

            if wr[0] == '4':
                bot.SendTo(contact, "是菜鸡")

            
            bot.SendTo(contact, "场次 " + bts + ", 胜率 " + wr + ", 评级 " + pr)
		        
        else:
            ran = random.random()
            if ran < 0.1:
                if content != '' and content != '/表情':
                    bot.SendTo(contact, content)