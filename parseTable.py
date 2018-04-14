from bs4 import BeautifulSoup
import requests
from pprint import pprint

req = 'http://www.fifa.com/worldcup/matches/index.html'
req = requests.get(req).content

footPlace={'Luzhniki Stadium':{'lat':'55.715989','lng':'37.553758'},
           'Spartak Stadium':{'lat':'55.817861','lng':'37.44025'},
           'Saint Petersburg Stadium':{'lat':'59.972953','lng':'30.220533',},
           'Kaliningrad':{'lat':'54.698056','lng':'20.533889',},
           'Kaliningrad Stadium':{'lat':'55.820639','lng':'49.161111',},
           'Nizhny Novgorod Stadium':{'lat':'56.3375','lng':'43.963333',},
           'Samara Arena':{'lat':'53.277778','lng':'50.237222'},
           'Volgograd Arena':{'lat':'48.734444','lng':'44.548611'},
           'Mordovia Arena':{'lat':'54.182778','lng':'45.201389'},
           'Rostov Arena':{'lat':'47.209444','lng':'39.737778'},
           'Fisht Stadium':{'lat':'43.402267','lng':'39.956111'},
           'Ekaterinburg Arena':{'lat':'56.8325','lng':'60.573611'},
           }

table = []

soup = BeautifulSoup(req, 'html.parser')
parse = soup.find_all('div',{'class':'mu-i-stadium'})

for stad, gr, city, time in zip(soup.find_all('div',{'class':'mu-i-stadium'}),
                    soup.find_all('div',{'class':'mu-i-group'}),
                    soup.find_all('div',{'class':'mu-i-venue'}),
                    soup.find_all('div',{'data-timeutc':True})):
    table.append({'stadium':stad.next,
                  'group':gr.next,
                  'city':city.next.strip(),
                  'time':'{}-{}-2018 {}'.format(time['data-daymonthutc'][:2],
                                                time['data-daymonthutc'][2:],
                                                time['data-timeutc'])})


#for i in range(lenTable):
    #print(parse[i])
    #table[i]['stadium']=parse[i]
#pprint(len([el.next for el in parse]))
parse = soup.find_all('div',{'class':'mu-i-group'})
#for i in range(lenTable):
    #table[i]['group']=parse[i].next
#pprint([el.next for el in parse])
parse = soup.find_all('div',{'data-timeutc':True})
#[s = '{}'.format(1) for i in range(2)]
#for i in range(lenTable):
    #table[i]['time']='{}-{}-2018 {}'.format(parse[i]['data-daymonthutc'][:2],parse[i]['data-daymonthutc'][2:],parse[i]['data-timeutc'])
#[el.time= for el in table]
pprint(table)