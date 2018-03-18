#Make a dictionary with common addresses(abbreviated) and symbols. The reference used is a Json
#file that has contract addresses and Syymbols. Do note, it is incomplete and a lot of symbols need to be added.

import requests
import json
from collections import defaultdict

text_file = open("/Users/tm/Downloads/common.txt", "w")
c = {}



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



############################################################
#Comparing IDEX with the above generated dictioanry to check for common Coins.
k = responseidex.content
idexdatalist = json.loads(k)

del1 =0
for key in idexdatalist:
    if key[:3] == 'ETH':
        if b[key[4:]]['val'] == 1:
            #print key[4:]

            c[key[4:]] = b[key[4:]]['address']
            text_file.write(key[4:])
            text_file.write('\n')





text_file.close()

c['NEWB']='ETH_0x814964b'
c['MAN']='ETH_0xe25bcec'
c['PXS']='ETH_0x358d124'
#c['BTO']='ETH_0x36905fc'
#c['EXY']='ETH_0x5c743a3'
c['TIE']='ETH_0x999967e'
#c['INS']='ETH_0x5b2e4a7'
c['ING']='ETH_0x24ddff6'
c['GET']='ETH_0x8a85428'

#c['GEM']='ETH_0xc7bba5b'

#c['EQC']='ETH_0xc438b4c'
c['ATMT']='ETH_0x331a550'
#c['CND']='ETH_0xd4c435f'
c['DVN']='ETH_0x9b7593a'
#c['QASH']='ETH_0x618e75a'

c['HBT']= 'ETH_0xdd6c68b'
c['RCN']= 'ETH_0xf970b8e'
c['ENG']= 'ETH_0xf0ee6b2'
c['PKT']= 'ETH_0x2604fa4'
c['WRC']= 'ETH_0x72adadb'

c['LINK']='ETH_0x5149107'
c['AXP']='ETH_0x9af2c6b'
c['EBET']='ETH_0x7d5edcd'
c['ARY']='ETH_0xa5f8fc0'
c['BLN']='ETH_0x7b1309c'
c['EPY']='ETH_0x50ee674'

json.dump(c, open('/Users/tm/Downloads/commondict.json','w'))
#print c






