import json
import urllib.request
from bs4 import BeautifulSoup

def getWOWS(user):
    result = ''
    
    try:
        response = urllib.request.urlopen('https://api.worldofwarships.com/wows/account/list/?application_id=demo&search=' + user)
        result = response.read()
        rst = json.loads(result)

        id = rst['data'][0]['account_id']

        #url = 'https://api.na.warships.today/api/player/' + str(id) + '/current'

        #response = urllib.request.urlopen(url)
        #result = response.read()
        #rst = json.loads(result)

        #s = rst['intervals'][-1]

        #st = s['subResultViews']['pvp']['overall']['player']['value']

        #b = st['statistics']['ShipCalculableStatistics']

        #print('win rate=', b['wins']/b['battles'])

        #print('WTR=', st['ratings']['ShipRatings']['warships_today_rating'])

        url = 'https://na.wows-numbers.com/player/' + str(id) + ',' + user + '/'
        response = urllib.request.urlopen(url, timeout=10)
        result = response.read()
    except:
        try:
            url = 'https://na.wows-numbers.com/player/' + str(id) + ',' + user + '/'
            response = urllib.request.urlopen(url, timeout=10)
            result = response.read()
        except:
            print('Network Error')
            return (-1, -1, -1)

    try:
        html = BeautifulSoup (result, 'html5lib')

        line = html.select('table > tbody > tr')

        bts = line[1].select('td > span')[0].get_text().strip()
        wr = line[2].select('td > span')[0].get_text().split()[0]
        pr = line[3].select('td > span')[0].get_text(strip=True)

        return (bts, wr, pr)

    except:
        print('Parse Error')
        return (-2, -1, -1)