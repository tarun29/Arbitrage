import requests
import json

#Make a dictionary with common addresses(abbreviated) and symbols. The reference used is a Json
#file that has contract addresses and Syymbols. Do note, it is incomplete and a lot of symbols need to be added.

import json
from collections import defaultdict

text_file = open("/Users/tm/Downloads/common.txt", "w")
d = {}



a = {}
#a = defaultdict(lambda:0,a)
a = defaultdict(lambda: defaultdict(lambda:0,a))

b = {}# dictionary of Symbols
#b = defaultdict(lambda:0,b)
b = defaultdict(lambda: defaultdict(lambda:0,b))





responseforkdelta = requests.get("https://api.forkdelta.com/returnTicker")

########################################################################
#Reading file linking Symbol and ETH address

with open('/Users/tm/Downloads/data.json', 'r') as inputjson:
    json_data = inputjson.read()
data = json.loads(json_data)



########################################################################

#Finds the symbol for the corresponding abbreviated address
k2 = responseforkdelta.content

forkdeltadatalist = json.loads(k2)




for key in forkdeltadatalist:
    a[key] = 1

print a

for item in data:
    lowercase = item['address'][:9].lower()
    if a['ETH_'+lowercase] == 1:
        chars = set('()_- ,')
        if any((c in chars) for c in item['symbol']):
            pass
        else:
            b[item['symbol']]['val'] = 1
            b[item['symbol']]['address'] = 'ETH_'+lowercase
            #print item['symbol']





print '\n\n\n'




##########################################################################################


###############################################################

reqkucoin = requests.get("https://api.kucoin.com/v1/market/open/symbols")
ku = reqkucoin.content

#print k
kucoinlist = json.loads(ku)
#print(type(l))


#print l['ETH_0x05f4a42']
#print l






for i in range(298):
    if b[kucoinlist['data'][i]['coinType']]['val'] == 1:
        #print b[kucoinlist['data'][i]['coinType']]
        d[kucoinlist['data'][i]['coinType']] = b[kucoinlist['data'][i]['coinType'][:3]]['address']

        if d[kucoinlist['data'][i]['coinType']]==0:
            try:
                del d[kucoinlist['data'][i]['coinType']]
            except KeyError:
                pass





json.dump(d, open('/Users/tm/Downloads/commonfdelta-kucoin.json','w'))




