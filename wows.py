import json
import urllib.request
from math import log

def getWOWS(user):
    try:
        response = urllib.request.urlopen(
            'https://api.worldofwarships.com/wows/account/list/?application_id=777eb24bbf6737cd08132d5997401bc6&search=' + user)
        result = response.read()
        rst = json.loads(result)

        id = rst['data'][0]['account_id']

        url = 'https://api.worldofwarships.com/wows/account/info/?application_id=777eb24bbf6737cd08132d5997401bc6&account_id=' + \
            str(id)
        response = urllib.request.urlopen(url, timeout=10)
        result = response.read()

        rst = json.loads(result)

        st = rst['data'][str(id)]['statistics']['pvp']

        wins = int(st['wins'])

        bts = int(st['battles'])
        dmg = int(st['damage_dealt']) / bts
        wr = round(float(wins) / bts, 4)
        xp = int(int(st['xp']) / bts)

        pr = ((wr - 0.5)**1.5 * 1000 + xp / 100 + dmg / 100 + log(bts) * 20) * 1.8

        return (bts, wr, int(pr))

    except:
        print('Parse Error')
        return (-2, -1, -1)

def main():
    print(getWOWS('lkytal'))
    print(getWOWS('caoshiwei'))
    print(getWOWS('_sunYj'))
    print(getWOWS('MI6_007'))
    print(getWOWS('September0616'))
    print(getWOWS('Ren_Amamiya'))

if __name__ == '__main__':
    main()
