#Make a dictionary with common addresses(abbreviated) and symbols. The reference used is a Json
#file that has contract addresses and Syymbols. Do note, it is incomplete and a lot of symbols need to be added.

import requests
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


responseidex = requests.post("https://api.idex.market/returnTicker")


responseforkdelta = requests.get("https://api.forkdelta.com/returnTicker")

########################################################################
#Reading file linking Symbol and ETH address

with open('/Users/tm/Downloads/data.json', 'r') as inputjson:
    json_data = inputjson.read()
data = json.loads(json_data)




###############################################################
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

#Next we will check common elements between Forkdelta generated Dictionary and Cryptopia

responsecryptopia = requests.get("https://www.cryptopia.co.nz/api/GetMarkets/BTC")

cryp = responsecryptopia.content

#print k
cryptopialist = json.loads(cryp)
#print(type(l))


#print l['ETH_0x05f4a42']
#print l

for key in cryptopialist['Data']:
    symbol = key['Label'].split('/')[0]
    if b[symbol]['val'] == 1:
        d[symbol] = b[symbol]['address']



deletelist = ['SMART','NET','FUEL','BNC']

for item in deletelist:
    if item in d: del d[item]

json.dump(d, open('/Users/tm/Downloads/commonfdelta-topia.json','w'))

#This d is a dictionary with keys as Symbolsfrom Cryptopia and Corresponding abbreviated addresses from Forkdelta.