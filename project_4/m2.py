## Get the names and cities of employees who have taken orders for parts costing less than 15.00.

from pymongo import MongoClient
client = MongoClient()
db = client.moDB
query = {}
result = []
for i in db.orders.find():
    # print(i)
    pno = []
    for j in i['ITEMS']:
        pno.append(int(j['PARTNUMBER']))
    query['PNO'] = pno
    # print(query)
    cursor2 = db.parts.find({'PNO':{'$in': query['PNO']}})
    for k in cursor2:
        if float(k['PRICE']) < 15.00:
            if not any(l['ENAME'] == db.employees.find({'ENO':i['TAKENBY']},{'ENAME':1,'CITY':1,'_id':0})[0]['ENAME'] for l in result):
                result.append(db.employees.find({'ENO':i['TAKENBY']},{'ENAME':1,'CITY':1,'_id':0})[0])
# result = set(result)
for i in result:
    print(i)