## For each customer, find a list of Order Numbers they have placed.

from pymongo import MongoClient
client = MongoClient()
db = client.moDB

result = []
for i in db.customers.find():
    # print(i)
    pno = []
    query = {}
    cursor2 = db.orders.find({'CUSTOMER':int(i['CNO'])},{'ONO':1,'_id':0})
    for j in cursor2:
        pno.append(int(j['ONO']))
    query['CNO'] = int(i['CNO'])
    query['orders'] = pno
    result.append(query)
# result = set(result)
for i in result:
    print(i)