import rdflib
from flask import abort
from flask import make_response
from flask import request
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

g = rdflib.Graph()
g.parse("PeriodicTable.owl")
print("graph has %s statements." % len(g))



## Query 1: Find element name, element symbol, atomic weight and color of
## all elements from the group with group name "Halogen"
@app.route('/periodictable/load', methods=['GET'])
def inserttable():
    # g = rdflib.Graph()
    # g.parse("PeriodicTable.owl")
    # print("graph has %s statements." % len(g))
    

    qres = g.query(
    """
    PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
    SELECT (str(?c) as ?NAME)
    { 
        ?c rdf:type table:Classification
    }""")

    res1 = []
    for row in qres:
        res1.append(row['NAME'].partition('#')[2])
        print("%s" % row['NAME'].partition('#')[2])
    qres = g.query(
    """
    PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
    SELECT (str(?c) as ?NAME)
    { 
        ?c rdf:type table:StandardState
    }""")

    res2 = []
    for row in qres:
        res2.append(row['NAME'].partition('#')[2])
        print("%s" % row['NAME'].partition('#')[2])

    qres = g.query(
    """
    PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
    PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
    SELECT (str(?c) as ?NAME)
    { 
        ?c rdf:type table:Block
    }""")

    res3 = []
    for row in qres:
        res3.append(row['NAME'].partition('#')[2])
        print("%s" % row['NAME'].partition('#')[2])

    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?c) as ?NAME)
        { 
           ?g rdf:type table:Group;
            table:element ?e.
            ?e table:group ?c;
    
        }""")
        
    res4 = []
    for row in qres:
        print(row[0])
        res4.append(row['NAME'].partition('#')[2])
        print("%s" % row)
    print({'name':res4})

    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT  (str(?c) as ?NAME)
        { 
            ?g rdf:type table:Group;
            table:element ?e.
            ?e table:period ?c;
        }""")
        
    res5 = []
    for row in qres:
        print(row[0])
        res5.append(row[0][0:].partition('#')[2])
        print("%s" % row)
    res5.sort()
    return jsonify({'class':res1,'state':res2,'block':res3,'group':res4,'period':res5})

@app.route('/periodictable/classification/<string:clss>',methods=['GET'])
def inserttable6(clss):
    # g = rdflib.Graph()
    # g.parse("PeriodicTable.owl")
    # print("graph has %s statements." % len(g))
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?c) as ?NAME)
        { 
            ?g rdf:type table:Element;
            table:name ?c;
            table:classification table:"""+clss+""";
            
        }""")
        
    res = []
    for row in qres:
        print(row[0])
        res.append(row[0][0:])
        print("%s" % row)
    res.sort()
    print({'ele':res})
    return jsonify({'ele':res})



@app.route('/periodictable/block/<string:clss>',methods=['GET'])
def inserttable89(clss):
    # g = rdflib.Graph()
    # g.parse("PeriodicTable.owl")
    # print("graph has %s statements." % len(g))
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?c) as ?NAME)
        { 
            ?g rdf:type table:Element;
            table:name ?c;
            table:block table:"""+clss+""";
            
        }""")
        
    res = []
    for row in qres:
        print(row[0])
        res.append(row[0][0:])
        print("%s" % row)
    res.sort()
    print({'ele':res})
    return jsonify({'ele':res})



@app.route('/periodictable/group/<string:clss>',methods=['GET'])
def inserttable869(clss):
    # g = rdflib.Graph()
    # g.parse("PeriodicTable.owl")
    # print("graph has %s statements." % len(g))
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?c) as ?NAME)
        { 
            ?g rdf:type table:Element;
            table:name ?c;
            table:group table:"""+clss+""";
            
        }""")
        
    res = []
    for row in qres:
        print(row[0])
        res.append(row[0][0:])
        print("%s" % row)
    res.sort()
    print({'ele':res})
    return jsonify({'ele':res})




@app.route('/periodictable/state/<string:clss>',methods=['GET'])
def inserttable8659(clss):
    # g = rdflib.Graph()
    # g.parse("PeriodicTable.owl")
    # print("graph has %s statements." % len(g))
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?c) as ?NAME)
        { 
            ?g rdf:type table:Element;
            table:name ?c;
            table:standardState table:"""+clss+""";
            
        }""")
        
    res = []
    for row in qres:
        print(row[0])
        res.append(row[0][0:])
        print("%s" % row)
    res.sort()
    print({'ele':res})
    return jsonify({'ele':res})


@app.route('/periodictable/period/<string:clss>',methods=['GET'])
def inserttable86597(clss):
    # g = rdflib.Graph()
    # g.parse("PeriodicTable.owl")
    # print("graph has %s statements." % len(g))
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT (str(?c) as ?NAME)
        { 
            ?g rdf:type table:Element;
            table:name ?c;
            table:period table:"""+clss+""";
        }""")
        
    res = []
    for row in qres:
        print(row[0])
        res.append(row[0][0:])
        print("%s" % row)
    res.sort()
    print({'ele':res})
    return jsonify({'ele':res})

@app.route('/periodictable/element/<string:sym>', methods=['GET'])
def inserttable7(sym):
    # g = rdflib.Graph()
    # g.parse("PeriodicTable.owl")
    # print("graph has %s statements." % len(g))
    qres = g.query(
        """
        PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
        PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
        SELECT  (str(?n) as ?NAME) (str(?s) as ?SYMBOL) (str(?gp) as ?group) (str(?p) as ?period) (str(?st) as ?standardState) 
        (str(?b) as ?block) (str(?cl) as ?classification) (str(?i) as ?casRegistryID) (str(?a) as ?ATOMICWEIGHT) (str(?k) as ?atomicNumber)  (str(?c) as ?COLOR) 
           
        { 
            ?g rdf:type table:Element;
            table:name \""""+sym+"""\"^^xsd:string;
            table:name ?n;
            table:symbol ?s;
            table:group ?gp;
            table:period ?p;
            table:standardState ?st;
            table:block ?b;
            table:classification ?cl;
            table:casRegistryID ?i;
            table:atomicWeight ?a;
            table:atomicNumber ?k;
            table:color ?c.
            
        }""")
        
    res = []
    for row in qres:
        # print(row[0])
        print({"name":row[0][0:],"symbol":row[1][0:],"group":row[2][0:].partition('#')[2],"period":row[3][0:].partition('#')[2],"standardstate":row[4][0:].partition('#')[2],"block":row[5][0:].partition('#')[2],"classification":row[6][0:].partition('#')[2],"casRegistryID":row[7][0:],"atmoicweight":row[8][0:],"atomicnumber":row[9][0:],"color":row[10][0:]})
        res.append({"name":row[0][0:],"symbol":row[1][0:],"group":row[2][0:].partition('#')[2],"period":row[3][0:].partition('#')[2],"standardstate":row[4][0:].partition('#')[2],"block":row[5][0:].partition('#')[2],"classification":row[6][0:].partition('#')[2],"casRegistryID":row[7][0:],"atmoicweight":row[8][0:],"atomicnumber":row[9][0:],"color":row[10][0:]})
        
        # print("%s" % row)
    # res.sort()
    # print(res[0])
    return jsonify(res[0])
# @app.route('/periodictable/blocks', methods=['GET'])
# def inserttable3():
#     # g = rdflib.Graph()
#     # g.parse("PeriodicTable.owl")
#     # print("graph has %s statements." % len(g))
#     qres = g.query(
#     """
#     PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
#     PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#     PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>
#     SELECT (str(?c) as ?NAME)
#     { 
#         ?c rdf:type table:Block
#     }""")

#     res = []
#     for row in qres:
#         res.append(row['NAME'].partition('#')[2])
#         print("%s" % row['NAME'].partition('#')[2])
#     return jsonify({'name':res})


# @app.route('/periodictable/groups', methods=['GET'])
# def inserttable5():
#     # g = rdflib.Graph()
#     # g.parse("PeriodicTable.owl")
#     # print("graph has %s statements." % len(g))
#     qres = g.query(
#     """
#     PREFIX table:<http://www.daml.org/2003/01/periodictable/PeriodicTable#>
#     PREFIX rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#     PREFIX xsd:<http://www.w3.org/2001/XMLSchema#>

#     SELECT DISTINCT (str(?n) as ?group)
#     { 
#     ?g rdf:type table:Group;
#     table:element ?e.
#     ?e table:group ?n;
    
    
#     }""")

#     # print(qres)
#     grp = []
#     for row in qres:
#         row = "%s" % row
#         grp.append(row.split("#")[-1])
#     # result = {"groups":grp}
#     # return result


#     return jsonify({'name':grp})
# Add security, response and request body definitions



app.run(debug=True)
