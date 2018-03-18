import requests
import json
from collections import defaultdict

text_file = open("/Users/tm/Downloads/common.txt", "w")



a = {}
a = defaultdict(lambda:0,a)

b = {}# dictionary of Symbols
b = defaultdict(lambda:0,b)

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
            b[item['symbol']] = 1
            #print item['symbol']






print '\n\n\n'

print "hello"

############################################################

k = responseidex.content
idexdatalist = json.loads(k)

for key in idexdatalist:
    if key[:3] == 'ETH':
        if b[key[4:]] == 1:
            #print key[4:]
            text_file.write(key[4:])
            text_file.write('\n')




text_file.close()