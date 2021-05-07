from pymongo import MongoClient
import sys

def load_teams(db,file):
    db.teams.delete_many({})
    with open(file) as input:
      for line in input:
            inv = {"tname":"","tlocation":""}
            l = []
            for value in  line.rstrip().split(':'):
                l.append(value)
            inv["tname"] = l[0]
            inv["tlocation"] = l[1]
            inv["_id"] = l[2]
            db.teams.insert_one(inv)


def main():
                
    client = MongoClient()
    db = client.baseballDB
    load_teams(db,sys.argv[1])


main()