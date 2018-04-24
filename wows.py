import json
import urllib.request

def getWOWS(user):
    result = ''
    
    try:
        response = urllib.request.urlopen('https://api.worldofwarships.com/wows/account/list/?application_id=demo&search=' + user)
        result = response.read()
        rst = json.loads(result)

        id = rst['data'][0]['account_id']

        url = 'https://api.worldofwarships.com/wows/account/info/?application_id=777eb24bbf6737cd08132d5997401bc6&account_id=' + str(id)
        response = urllib.request.urlopen(url, timeout=10)
        result = response.read()
        
        rst = json.loads(result)

        st = rst['data'][str(id)]['statistics']['pvp']

        wins = int(st['wins'])

        
        bts = int(st['battles'])
        wr = round(float(wins) / bts, 4)
        pr = int(int(st['xp']) / bts)

        return (bts, wr, pr)

    except:
        print('Parse Error')
        return (-2, -1, -1)

#print(getWOWS('lkytal'))