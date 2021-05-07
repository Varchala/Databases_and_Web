import mysql.connector as mysql
from flask import abort
from flask import make_response
from flask import request
from flask import Flask, jsonify
from flask_cors import CORS
import pymongo
from pymongo import MongoClient
import sys
app = Flask(__name__)
CORS(app)

@app.route('/baseball/standings/', methods=['GET'])
def standings():
    client = MongoClient()
    db = client.baseballDB
    standings = {}
    l = []
    print(db)
    for i in db.teams.find():
        wins = 0
        loss = 0
        tie = 0
        for j in db.games.find({'visitingTCode':i['_id']}):
            if(int(j['visitingTScore'])>int(j['homeTScore'])):
                wins += 1
            elif(int(j['visitingTScore'])<int(j['homeTScore'])):
                loss += 1
            else:
                tie += 1
        print("In 2nd")
        for j in db.games.find({'homeTCode':i['_id']}):
            if(int(j['visitingTScore'])>int(j['homeTScore'])):
                loss += 1
            elif(int(j['visitingTScore'])<int(j['homeTScore'])):
                wins += 1
            else:
                tie += 1
        l.append({'losses': loss, 'percent': round(float((float(wins)+0.5*tie)/float(wins+loss+tie)),3), 'tcode': i['_id'], 'ties': tie, 'tname': i['tname'], 'wins': wins})
    standings['standings'] = l
    return jsonify(standings)
@app.route('/baseball/results/<string:tcode>/', methods=['GET'])
def results(tcode):

        client = MongoClient()
        db = client.baseballDB
        results = {}
        l = []
        r = ""
        for j in db.games.find({'$or': [{'visitingTCode':tcode},{"homeTCode":tcode}]}).sort([('gdate',1)]):
            if(j['visitingTCode']==tcode):
                if(int(j['visitingTScore'])>int(j['homeTScore'])):
                    r = "WIN"
                elif(int(j['visitingTScore'])<int(j['homeTScore'])):
                    r = "LOSS"
                else:
                    r = "TIE"
                l.append({'gdate': j['gDate'], 'opponent': "at "+j['homeTCode'], 'result': r, 'them': j['homeTScore'], 'us': j['visitingTScore'] })
            else:
                if(int(j['visitingTScore'])>int(j['homeTScore'])):
                    r = "LOSS"
                elif(int(j['visitingTScore'])<int(j['homeTScore'])):
                    r = "WIN"
                else:
                    r = "TIE"
                l.append({'gdate': j['gDate'], 'opponent': j['visitingTCode'], 'result': r, 'them': j['visitingTScore'], 'us': j['homeTScore'] })
        
        results['results'] = l
        results['tloc'] = db.teams.find({'_id':tcode},{"tlocation":1})[0]['tlocation']
        results['tname'] = db.teams.find({'_id':tcode},{"tname":1})[0]['tname']
        return jsonify(results)

app.run(debug=True)

    