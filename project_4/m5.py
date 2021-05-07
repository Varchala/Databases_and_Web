## Get the total price of products in order 1024.

from pymongo import MongoClient
client = MongoClient()
db = client.moDB

result = 0.0
for i in db.orders.find({'ONO':1024}):
    for j in i['ITEMS']:
        result += db.parts.find({'PNO':j['PARTNUMBER']},{'PRICE':1,'_id':0})[0]['PRICE']*j['QUANTITY']
print("Total sale in order 1024")
print(result)
