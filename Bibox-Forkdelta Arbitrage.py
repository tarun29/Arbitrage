#Integrating everything 1
#Compares Bibox and Forkdelta

import requests
import json



from collections import defaultdict

d3 = json.load(open("/Users/tm/Downloads/commonfdelta-bibox.json"))




#########FORKDELTA#####
responsedelta = requests.get("https://api.forkdelta.com/returnTicker")
m = responsedelta.content
deltadatalist = json.loads(m)

##d3 format = idexkey - deltakey

for key in d3:
    #########Cryptopia#####

    url = 'https://api.bibox.com/v1/mdata?cmd=depth&pair=' + key + '_ETH&size=1'
    responsebibox = requests.get(url)
    bibox = responsebibox.content
    biboxlist = json.loads(bibox)

    if float(biboxlist['result']['bids'][0]['price']) > float(deltadatalist[d3[key]]['ask']):
        print key
        print "Delta Sell Price"
        print deltadatalist[d3[key]]['ask']
        print "Bibox Buy Price:"
        print float(biboxlist['result']['bids'][0]['price'])
        print '\n'

    if float(deltadatalist[d3[key]]['bid']) > float(biboxlist['result']['asks'][0]['price']):
        print key
        print "Delta Buy Price"
        print deltadatalist[d3[key]]['bid']
        print "Bibox Sell Price:"
        print biboxlist['result']['asks'][0]['price']
        print '\n'
        # print float(deltadatalist[d3[key]]['bid']) - float(idexdatalist[concatkey]['lowestAsk'])'''













