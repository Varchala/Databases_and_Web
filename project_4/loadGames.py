from pymongo import MongoClient
import sys


def load_games(db,file):
    db.games.delete_many({})
    with open(file) as input:
      for line in input:
            inv = {"gDate":"","visitingTCode":"","homeTCode":"","visitingTScore":"","homeTScore":""}
            l = []
            for value in  line.rstrip().split(':'):
                l.append(value)
            inv["gDate"] = l[0]
            inv["visitingTCode"] = l[1]
            inv["homeTCode"] = l[2]
            inv["visitingTScore"] = l[3]
            inv["homeTScore"] = l[4]
            if(len(list(db.teams.find({"_id":inv["visitingTCode"]},{"_id":1}))) == 0  or len(list(db.teams.find({"_id":inv["homeTCode"]},{"_id":1}))) == 0):
                print("Cannot insert {} into the collections in baseballDB as the given team code was not found in teams colection ".format(line.rstrip()))
            else:
                db.games.insert_one(inv)


def main():
                
    client = MongoClient()
    db = client.baseballDB
    load_games(db,sys.argv[1])


main()