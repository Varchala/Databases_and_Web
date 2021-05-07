### Csc 8711, Databases and the Web - Project 5

**Due**: Tuesday, April 20th  
Pair Assignment (Maximum of 2 persons per group).

### Semantic Web, RDF, SPARQL, Web Services, UI

Consider the Periodic Table Ontology specified in the following OWL/n3 files:

- [Periodictable.owl](http://tinman.cs.gsu.edu/~raj/8711/sp21/p5/Periodictable.owl)
- [Periodictable.n3](http://tinman.cs.gsu.edu/~raj/8711/sp21/p5/Periodictable.n3)

Note: The .n3 file is given so that you can recognize the "triples" easily. Both the .owl and the .n3 files contain the same Ontology and you should use just the .owl file. Build a Web application that allows the user to browse the data in this ontology.

#### Project Requirements

1. Use Python-SPARQL API to run SPARQL queries against the Ontologies and embed these into Python-Flask RESTful Services. Some of the endpoints you would need are (add other end points as needed):
    
    @app.route('/periodictable/standard\_states/', methods=\['GET'\])
    @app.route('/periodictable/standard\_state/<string:state>'/ methods=\['GET'\])
    @app.route('/periodictable/classifications/', methods=\['GET'\])
    @app.route('/periodictable/classification/<string:clss>'/ methods=\['GET'\])
    @app.route('/periodictable/blocks/', methods=\['GET'\])
    @app.route('/periodictable/block/<string:blk>'/ methods=\['GET'\])
    @app.route('/periodictable/groups/', methods=\['GET'\])
    @app.route('/periodictable/group/<int:gnum>'/ methods=\['GET'\])
    @app.route('/periodictable/periods/', methods=\['GET'\])
    @app.route('/periodictable/period/<int:pnum>'/ methods=\['GET'\])
    @app.route('/periodictable/element/<string:sym>'/ methods=\['GET'\])
    
2. Write OPENAPI Specifications using Swagger.
3. Build Web Client/UI (Single Page App) to enable users to browse the Elements by Classification, Standard State, Block, Group, and Period. These should produce a list of elements that belong to the particular category. These elements should be hyper-linked to a separate div within the page describing the details of that element.
4. The project will be graded for a reasonable UI.

#### What to submit

1. A zip or tar archive of the project; the main folder should contain the RESTful API program, elements.py, and a folder called frontend that contains all your UI code (html/Javascript/css etc); Our grader will simply launch the REST API program and use your frontend to test. Also, please include the OPENAPI specification in file, OpenAPI\_PeriodicTable.json.
