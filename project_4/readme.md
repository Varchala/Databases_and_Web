### Csc 8711, Databases and the Web - Project 4

**Due**: Sunday, April 4th  
INDIVIDUAL ASSIGNMENT

### I. JSON Schema

I. Consider the following JSON document that describes data related to posts in a typical discussion forum such as Piazza:

{ "posts": \[
    { "postID": 1,
      "postDate": "2003-01-11",
      "poster": "a@abc.com",
      "subject": "Welcome",
      "content": "Welcome to the bulletin board",
      "followup": \[
        { "postID": 2,
          "postDate": "2003-01-12",
          "poster": "b@abc.com",
          "subject": "Posting 2",
          "content": "This is posting 2",
          "followup": \[
            { "postID": 7,
              "postDate": "2003-01-11",
              "poster": "a@abc.com",
              "subject": "Posting 7",
              "content": "This is posting 7",
              "followup": \[\]
            },
            { "postID": 8,
              "postDate": "2003-01-11",
              "poster": "a@abc.com",
              "subject": "Posting 8",
              "content": "This is posting 8",
              "followup": \[
                { "postID": 9,
                  "postDate": "2003-01-19",
                  "poster": "a@abc.com",
                  "subject": "Posting 9",
                  "content": "This is posting 9",
                  "followup": \[\]
                }
              \]
            }
          \]
        },
        { "postID": 3,
          "postDate": "2003-01-13",
          "poster": "c@abc.com",
          "subject": "Posting 3",
          "content": "This is posting 3",
          "followup": \[\]
        }
      \]
    },
    ...
    ...
  \]
}

The JSON document consists of a single key-value pair, where key is "posts" and it's value is an array of zero of more individual posts. Each individual post consists of several key-value fields such as "postID, "postDate", "poster", "subject", "content", and "followup". "postID" is of positive integer type and all other fields except for "postDate", "poster", and "followup" are of string type. The "postDate" is of "date-time" type, "poster" will be in the format of an email address, and the "followup" field is an array of zero or more individual posts (a recursive structure!).

Write a JSON Schema Specification for documents that describe posts in a discussion forum in a file called postingsSchema.json.

### II. JSONiq Queries

Consider the JSON representation of the mail order database in [mo.json](http://tinman.cs.gsu.edu/~raj/8711/sp21/p4/mo.json). Write JSONiq expressions for the following queries:

1. (: Get the names of customers who have ordered parts from employees living in Wichita. :)
2. (: Get the names of customers who have ordered all parts costing less than 20.00. :)
3. (: Get the names of employees who have never made a sale to a customer living in their own zipcode. :)
4. (: For each employee, find a list of Order Numbers they have taken :)
5. (: Get order numbers of orders that took longer than 2 days to ship. :)
6. (: Get order number and total price for each order. :)

Place each query in a file named m1.jq, m2.jq, etc.

### III. MongoDB Queries

Consider the MongoDB version of the mail order database in [employees.js](http://tinman.cs.gsu.edu/~raj/8711/sp21/p4/employees.js), [customers.js](http://tinman.cs.gsu.edu/~raj/8711/sp21/p4/customers.js), [parts.js](http://tinman.cs.gsu.edu/~raj/8711/sp21/p4/parts.js), [orders.js](http://tinman.cs.gsu.edu/~raj/8711/sp21/p4/orders.js). Write PyMongo programs to answer each of the following queries:

1. \## Get the names of parts that cost less than 20.00.
2. \## Get the names and cities of employees who have taken orders for parts costing less than 15.00.
3. \## For each customer, find a list of Order Numbers they have placed.
4. \## Get the names of customers who have ordered parts only from employees living in Wichita.
5. \## Get the total price of products in order 1024.
6. \## Get employee numbers and total sales for each employee.

Each program should print the results of the query to the standard output. Place each query in a file named m1.py, m2.py, etc.

### IV. Baseball Standings App using MongoDB

Consider the following data describing baseball teams and results of games:

macbook-pro:baseball raj$ more teams.dat 
Braves:Atlanta:ATL
Cardinals:Saint Louis:STL
Cubs:Chicago:CHC
Diamondbacks:Arizona:ARI
Indians:Cleveland:CLE

macbook-pro:baseball raj$ more games.dat
2004-03-20:ARI:CHC:10:11
2004-03-23:ATL:STL:0:1
2004-03-27:STL:CHC:7:9
2004-03-27:CLE:ATL:1:0
2004-03-30:ATL:CHC:10:5
2004-04-01:CLE:ARI:8:8
2004-04-15:ARI:ATL:3:11
2004-04-17:CLE:STL:7:11
2004-04-20:STL:ARI:10:12
2004-04-22:CHC:CLE:7:4
2004-04-24:CHC:ARI:7:12
2004-04-29:STL:ATL:2:10
2004-05-01:ATL:CLE:14:14
2004-05-01:CHC:STL:10:0
2004-05-04:CHC:ATL:10:8
2004-05-04:ARI:CLE:8:7
2004-05-08:ATL:ARI:6:8
2004-05-13:STL:CLE:3:6
2004-05-15:ARI:STL:7:13
2004-05-15:CLE:CHC:6:8
2004-05-18:ARI:CHC:13:5
2004-05-22:ATL:STL:3:6

Rows in teams.dat contain team name, team location, and team code, whereas rows in games.dat contain game date, visiting team code, home team code, visiting team score, and home team score.

1. Write two Python programs (loadTeams.py and loadGames.py) to load this data into a MongoDB database. You should accept the data files as command line parameter (sys.argv\[1\]). You will create two collections (named teams and games) within a database named baseballDB. You must ensure the following two constraints are satisfied:
    
    1. The team code serves as a primary key for the teams collection. So, you should make sure that no duplicate team codes are inserted into the teams collection.
    2. Since the team code is used in the the games data, you must ensure that while inserting into the games collection that both the teams involved are present in the teams collection.
    
    You may assume that the rest of the data is accurate, i.e. there are no data type mis-matches, no missing fields, etc. You may assume that teams.dat and games.dat are available in the current directory where loadTeams.py and loadGames.py are located. Please delete all data before you load!
    
2. Write a REST API program (baseball.py) that implements the following two endpoints:
    
    @app.route('/baseball/standings/', methods=\['GET'\])
    
    which returns the standings information as a JSON object shown below:
    
    { standings: \[
        { losses: 3, percent: 0.667, tcode: "CHC", ties: 0, tname: "Cubs", wins: 6 },
        { losses: 3, percent: 0.611, tcode: "ARI", ties: 1, tname: "Diamondbacks", wins: 5 },
        { losses: 5, percent: 0.444, tcode: "STL", ties: 0, tname: "Cardinals", wins: 4 },
        { losses: 5, percent: 0.389, tcode: "ATL", ties: 1, tname: "Braves", wins: 3 },
        { losses: 4, percent: 0.375, tcode: "CLE", ties: 2, tname: "Indians", wins: 2 }
      \]
    }
    
    and
    
    @app.route('/baseball/results/<string:tcode>/', methods=\['GET'\])
    
    which returns a list of game results for a particular team in chronological order as a JSON object shown below:
    
    {
      results: \[
        { gdate: "2004-03-20", opponent: "ARI", result: "WIN", them: 10, us: 11 },
        { gdate: "2004-03-27", opponent: "STL", result: "WIN", them: 7, us: 9 },
        { gdate: "2004-03-30", opponent: "ATL", result: "LOSS", them: 10, us: 5 },
        { gdate: "2004-04-22", opponent: "at CLE", result: "WIN", them: 4, us: 7 },
        { gdate: "2004-04-24", opponent: "at ARI", result: "LOSS", them: 12, us: 7 },
        { gdate: "2004-05-01", opponent: "at STL", result: "WIN", them: 0, us: 10 },
        { gdate: "2004-05-04", opponent: "at ATL", result: "WIN", them: 8, us: 10 },
        { gdate: "2004-05-15", opponent: "CLE", result: "WIN", them: 6, us: 8 },
        { gdate: "2004-05-18", opponent: "ARI", result: "LOSS", them: 13, us: 5 }
      \],
      tloc: "Chicago",
      tname: "Cubs"
    }
    
    You may use the [front end](http://tinman.cs.gsu.edu/~raj/8711/sp21/p4/front-end/) I have developed to do a final check.

### What to Submit?

1. postingsSchema.json
2. m1.jq, m2.jq, m3.jq, m4.jq, m4.jq, and m6.jq
3. m1.py, m2.py, m3.py, m4.py, m4.py, and m6.py
4. loadTeams.py, loadGames.py, baseball.py
