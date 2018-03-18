#Integrating everything 1
#Compares IDEX and Forkdelta

import requests
import json


ethbinance = requests.get("https://api.binance.com/api/v1/depth?symbol=ETHBTC")
ethbinance2 = ethbinance.content
ethbinancelist = json.loads(ethbinance2)
print ethbinancelist['bids'][0][0]
from collections import defaultdict

d3 = json.load(open("/Users/tm/Downloads/commonfdelta-topia"
                    ".json"))




#########FORKDELTA#####
responsedelta = requests.get("https://api.forkdelta.com/returnTicker")
m = responsedelta.content
deltadatalist = json.loads(m)

##d3 format = idexkey - deltakey

for key in d3:
    #########Cryptopia#####
    url = 'https://www.cryptopia.co.nz/api/GetMarket/'+key+'_BTC'
    responsecryptopia = requests.get(url)
    cryp = responsecryptopia.content
    cryptopialist = json.loads(cryp)
    if float(cryptopialist['Data']['BidPrice'])/float(ethbinancelist['bids'][0][0]) > float(deltadatalist[d3[key]]['ask']):
        print key
        print "Delta Sell Price"
        print deltadatalist[d3[key]]['ask']
        print "Cryyptopia ETH Price:"
        print float(cryptopialist['Data']['BidPrice'])/float(ethbinancelist['bids'][0][0])
        print '\n'


'''    if float(deltadatalist[d3[key]]['bid']) > float(cryptopialist['Data']['AskPrice'])/float(ethbinancelist['bids'][0][0]):
        print key
        print deltadatalist[d3[key]]['bid']
        print "Cryyptopia BTC Price: "
        print cryptopialist['Data']['AskPrice']
        print "Cryyptopia ETH Price:"
        print float(cryptopialist['Data']['AskPrice'])/float(ethbinancelist['bids'][0][0])
        print '\n'
        # print float(deltadatalist[d3[key]]['bid']) - float(idexdatalist[concatkey]['lowestAsk'])'''











