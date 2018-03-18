#USED to get Symbols of the short abbreviated Addresses from forkdelta API.
import requests
import json
from collections import defaultdict
a = {}# dictionary of abbreviated addresses i.e 0x05f3432
a = defaultdict(lambda:0,a)



responseidex = requests.post("https://api.idex.market/returnTicker")


responseforkdelta = requests.get("https://api.forkdelta.com/returnTicker")

########################################################################
#Reading file linking Symbol and ETH address

with open('/Users/tm/Downloads/data.json', 'r') as inputjson:
    json_data = inputjson.read()
data = json.loads(json_data)




###############################################################

k2 = responseforkdelta.content
#print k
forkdeltadatalist = json.loads(k2)
#print(type(l))



for key in forkdeltadatalist:
    a[key] = 1

print a
for item in data:
    lowercase = item['address'][:9].lower()
    if a['ETH_'+lowercase] == 1:
        chars = set('()_- ,.')
        if any((c in chars) for c in item['symbol']):
            pass
        else:
            print item['symbol']





