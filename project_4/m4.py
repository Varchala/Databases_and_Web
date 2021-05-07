## Get the names of customers who have ordered parts only from employees living in Wichita.
from pymongo import MongoClient
client = MongoClient()
db = client.moDB

result = []
for i in db.customers.find():
    # print(i)
    pno = []
    query = {}
    cursor2 = db.orders.find({'CUSTOMER':int(i['CNO'])},{'TAKENBY':1,'_id':0})
    for j in cursor2:
        pno.append(int(j['TAKENBY']))
    query['eno'] = pno
    flag = True
    for k in pno:
        emp = db.employees.find({'ENO':k},{'ENO':1,'CITY':1,'_id':0})
        if emp[0]['CITY'] == 'Wichita':
            continue
        else:
            flag=False
    # print(i)
    if(flag):
        print({'cname':i['CNAME']})
