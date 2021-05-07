#########################################################################
# HOMEWORK-6
# NEO4J Project - Company Database Queries and Browser
#########################################################################


#########################################################################
#
# Contributors:
#
# Varchaleswari Ganugapati, email : vganugapati1@student.gsu.edu
# Bhagirath Tallapragada, email : btallapragada1@student.gsu.edu
#
#########################################################################



#########################################################################
# Thank you for a wonderful learning experience @ Dr. Sunderraman and TA
# -Both team members
#########################################################################


### Csc 8711, Databases and the Web - Project 6

**Due**: Monday, May 3rd  
Pair Assignment (Maximum of 2 persons per group).

### NEO4J Project - Company Database Queries and Browser

Consider the [Company Database](http://tinman.cs.gsu.edu/~raj/8711/sp21/p6/CompanyER.pdf) ER diagram from the popular Elmasri-Navathe database textbook. This is the same database we looked at in HW2 in XML. The data for this database is available in [data](http://tinman.cs.gsu.edu/~raj/8711/sp21/p6/data/).

1. Write a Python program, loadCompany.py, that takes the data directory as a command line argument and creates a NEO4J database that stores all entities as nodes and all relationships as edges.
    
    $ python3 loadCompany.py ./data
    
    Please use the following labels for nodes and relationships so that when we grade against our database we can see the correct answers:
    
    Node Labels:
      
    "Department"
    "Employee"
    "Dependent"
    "Project"
    
    Relationship Labels:
    
    Relationship(d,"employs",e)
    Relationship(e,"works\_for",d)
    
    Relationship(e,"supervisee",boss)
    Relationship(boss,"supervisor",e)
    
    Relationship(d,"managed\_by",e)
    Relationship(e,"manages",d)
    
    Relationship(e,"dependent",d)
    Relationship(d,"dependent\_of",e)
    
    Relationship(d,"controls",p)
    Relationship(p,"controlled\_by",d)
    
    Relationship(p,"worker",e)
    Relationship(e,"works\_on",p)
    
2. Write Cypher queries for the following:
    1. Retrieve the names and addresses of employees who work for the "Research" department.
    2. For every project located in "Stafford", retrieve the project number, the controlling department number, and the department’s manager’s last name, address, and birth date.
    3. Retrieve the names of all employees who have two or more dependents.
    4. Retrieve the names of managers who have at least one dependent.
    5. Retrieve the names of employees who work on all projects controlled by department "5"If you find the Cypher query to be tricky or difficult, you may solve the query by writing a Python program that produces the query answer in the output.
3. Write Python-Flask RESTful services (company.py) to implement the following endpoints that could be used by a UI frontend to browse the data in the entire database:
    
    @app.route('/company/departments/', methods=\['GET'\])
    @app.route('/company/employees/', methods=\['GET'\])
    @app.route('/company/projects/', methods=\['GET'\])
    @app.route('/company/cities/', methods=\['GET'\])
    @app.route('/company/supervisees/<string:ssn>/' methods=\['GET'\])
    @app.route('/company/department/<int:dno>/' methods=\['GET'\])
    @app.route('/company/employee/<string:ssn>/' methods=\['GET'\])
    @app.route('/company/project/<int:pno>/' methods=\['GET'\])
    @app.route('/company/projects/<string:cty>/' methods=\['GET'\])
    @app.route('/company/departments/<string:cty>/' methods=\['GET'\])
    
    Sample return values are shown [here](http://tinman.cs.gsu.edu/~raj/8711/sp21/p6/apiResults.html).
    
    [frontend code](http://tinman.cs.gsu.edu/~raj/8711/sp21/p6/frontend/)
    

#### What to submit

1. loadCompany.py
2. q1.cypher/q1.py, q2.cypher/q2.py, q3.cypher/q3.py, q4.cypher/q4.py, and q5.cypher/q5.py.
3. company.py
4. README that includes team members for Problem 3
