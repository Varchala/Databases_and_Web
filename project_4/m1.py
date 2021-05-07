## Get the names of parts that cost less than 20.00.

from pymongo import MongoClient
client = MongoClient()
db = client.moDB
cursor = db.parts.find({"PRICE" :{"$lt":20.00}},{'PNAME':1,'_id':0})
for i in cursor:
    print(i)