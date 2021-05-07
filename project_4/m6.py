## Get employee numbers and total sales for each employee.

from pymongo import MongoClient
client = MongoClient()
db = client.moDB

print("Employee numbers and total sales for each employee.")
for i in db.employees.find():
    result = 0.00
    for k in db.orders.find({'TAKENBY':i['ENO']}):
        for j in k['ITEMS']:
            result += db.parts.find({'PNO':j['PARTNUMBER']},{'PRICE':1,'_id':0})[0]['PRICE']*j['QUANTITY']
    print(str(int(i['ENO']))+"   "+str(result))