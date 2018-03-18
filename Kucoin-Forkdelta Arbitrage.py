

import requests
import json
from collections import defaultdict




from collections import defaultdict

d3 = json.load(open("/Users/tm/Downloads/commonfdelta-kucoin"
                    ".json"))


pricedict = defaultdict(lambda: defaultdict(lambda:0,pricedict))


#########FORKDELTA#####
responsedelta = requests.get("https://api.forkdelta.com/returnTicker")
m = responsedelta.content
deltadatalist = json.loads(m)

##d3 format = idexkey - deltakey
reqkucoin = requests.get("https://api.kucoin.com/v1/market/open/symbols")
ku = reqkucoin.content
kucoinlist = json.loads(ku)


for i in range(298):
    if kucoinlist['data'][i]["symbol"][-3:]=='ETH':
        pricedict[kucoinlist['data'][i]["coinType"]]['bid'] = kucoinlist['data'][i]["buy"]
        pricedict[kucoinlist['data'][i]["coinType"]]['ask'] = kucoinlist['data'][i]["sell"]

for key in d3:
    #########Cryptopia#####
    if key =='MTH' or key == 'BNTY':
        pass
    else:
        if float(pricedict[key]['bid']) > float(deltadatalist[d3[key]]['ask']):
            print key
            print "Delta Sell Price"
            print deltadatalist[d3[key]]['ask']
            print "Kucoin ETH Price:"
            print pricedict[key]['bid']
            print '\n'

        if float(deltadatalist[d3[key]]['bid']) > float(pricedict[key]['ask']):
            print key
            print "delta bid"
            print deltadatalist[d3[key]]['bid']
            print "Kucoin ETH sell Price: "
            print pricedict[key]['ask']
            print '\n'











