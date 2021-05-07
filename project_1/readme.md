
# Csc 8711, Databases and the Web - Programming Project 1

**Due**: Sunday, January 31, 2021  
To be completed in teams of 2 members, with one person focusing on frontend and the other focusing on backend. This does not preclude helping each other!

### An Online QBE Processor for MySQL

In this programming assignment, you will implement a Web-based QBE (Query By Example) Processor for MySQL databases. [QBE](http://tinman.cs.gsu.edu/~raj/8711/sp21/p1/qbe.pdf) is a visual query language in which the user expresses a relational query using example elements and variables. You will implement a subset of the language. The subset should include simple Select-Project-Join (SPJ) queries as well as two additional advanced features.

### Technologies to be used

You will implement this project as a Single Page Application (SPA) using modern Web application architecture with:

1. MySQL database on which the querying will be done
2. Backend Web Services using GraphQL in Python Graphene
3. Frontend with HTML/Javascript or ReactJS or AngularJS

### User Interface

Here are the screenshots of the user interface, shown progressively as the user interacts with the UI:

#### Initial Screen

![](./initial.png)

#### Screen after user successfully enters MySQL credentials

![](./second.png)

#### Screen after user retrieves table skeletons to express QBE query

![](./3.png)

#### Screen after user submits QBE query for execution

![](./4.png)

#### Notes

1. The initial screen will allow the user to provide the credentials for a MySQL database on the server. These will include database name, username, and password. We will assume that the database is available on the server where the application is running.
2. Upon successfully verifying the credentials, the user should be shown a list of tables in the MySQL database along with a choice of 0/1/2 for number of table skeletons.
3. To express a query, the user enters form elements in the table skeletons and condition box. There are four types of elements: P., P.\_Variable, Constant, and \_Variable. A P. under the table name is a shorthand notation for P. under all the columns of the table. String constants should be enclosed within single quotes.
4. Once the query is formulated, the user may submit the query for execution. The QBE processor should first check for any syntax or semantic errors in the query. Once the QBE query is error free, the QBE processor should generate an appropriate SQL query, execute it against the database and return the results.
5. The "Reset Skeletons" button when clicked should blank out the "QBE Interface" and the "Query Results" divisions of the SPA.
6. Implementing simple Queries (the S-P-J variety) will earn you 80% of the credit. To earn the remaining 20%, you must implement at least 2 advanced features of QBE. Please review the QBE documentation and choose any two additional features and implement them.
7. For testing purposes, you may load the SQL files available at [Classroom Database](http://tinman.cs.gsu.edu/~raj/h1000/f19/load-data/) and [Congress Database](http://tinman.cs.gsu.edu/~raj/8711/sp21/p1/congress-db) into your MySQL account.

#### What to Submit?

1. All code to develop the project.
2. Short project report and contributions of group members. (1-2 pages in pdf)
