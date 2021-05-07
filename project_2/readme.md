# Csc 8711, Databases and the Web - Programming Project 2

**Due**: Sunday, February 28, 2021

### XML Schema

1. Consider the XML document, [mo.xml](http://tinman.cs.gsu.edu/~raj/8711/sp21/p2/mo.xml), containing data from the mail order database.
    
    The XML document has the <mo> element at the root and contains four sub-elements: <customers>, <employees>, <parts>, and <orders> in sequence.
    
    The <customers> element contains zero or more <customer> sub-elements and the <customer> element contains one attribute, cno, whose value is a 4-digit integer between 1000 and 9999, and five sub-elements: <cname> of type string, <street> of type string, <city> of type string, <zip> whose value is either a 5-digit number or a 5-digit number followed by a “-“ followed by a 4-digit number, and <phone> whose value is a 3-digit area code followed by a “-“ followed by a 3-digit exchange code, followed by a “-“ and followed by a 4-digit number.
    
    The <employees> element contains zero or more <employee> sub-elements and the <employee> element contains one attribute, eno, whose value is a 4-digit integer between 1000 and 9999, and four sub-elements: <ename> of type string, <city> of type string, <zip> whose value is either a 5-digit number or a 5-digit number followed by a “-“ followed by a 4-digit number, and <hdate> of type date.
    
    The <parts> element contains zero or more <part> sub-elements and the <part> element contains one attribute, pno, whose value is a 5-digit integer between 10000 and 99999, and four sub-elements: <pname> of type string, <qoh> of type positive integer, <price> of type positive decimal with two fractional digits, and <level> of type positive integer.
    
    The <orders> element contains zero or more <order> sub-elements and the <order> element contains three attributes, ono, whose value is a 4-digit integer between 1000 and 9999, takenBy whose value is the same type as an employee number, and customer whose value is the same type as a customer number, and the following sub-elements: <receivedDate> of type date, an optional <shippedDate> of type date, and <items> which is a repeating group (one or more) of <item> elements. The <item> element contains two sub-elements: <partNumber> whose value is the same type as a part number and <quantity> of type positive integer.
    
    Write an XML Schema specification for the mail order document and validate several instance documents against the schema.
    

### XQuery

1. Consider the XML document, [ships.xml](http://tinman.cs.gsu.edu/~raj/8711/sp21/p2/ships.xml), that contains information about battleships. Write XQuery expressions to solve the following queries:
    1. Find the names of the classes that had at least 10 guns.
    2. Find the names of the ships that had at least 10 guns.
    3. Find the names of the ships that were sunk.
    4. Find the names of the classes with at least 3 ships.
    5. Find the names of the classes such that no ship of that class was in a battle.
    6. Find the names of the classes that had at least two ships launched in the same year.
    7. Produce a sequence of items of the form:
        
          <battle name = x>
            <ship name = y />
            ...
            ...
          <battle>
        
        where x is the name of a battle and y the name of a ship in the battle. There may be more than one ship element in the sequence.Make sure that the queries can execute and produce the correct answers in BaseX. Please place each query in a separate file, s1.xq, s2.xq, s3.xq, s4.xq, s5.xq, s6.xq, and s7.xq.
2. Consider the XML document, [company.xml](http://tinman.cs.gsu.edu/~raj/8711/sp21/p2/company.xml), that contains information about battleships. Write XQuery expressions to solve the following queries:
    1. Retrieve the names and addresses of employees who work for the "Research" department.
    2. For every project located in "Stafford", retrieve the project number, the controlling department number, and the department’s manager’s last name, address, and birth date.
    3. Retrieve the names of all employees who have two or more dependents.
    4. Retrieve the names of managers who have at least one dependent.
    5. Retrieve the names of employees who work on all projects controlled by department "5"Make sure that the queries can execute and produce the correct answers in BaseX. Please place each query in a separate file, c1.xq, c2.xq, c3.xq, c4.xq, and c5.xq.

### XSLT

1. **Data Input Forms:** A data input form consists of one or more form elements that is capable of accepting input from a user. We shall consider 7 types of form elements: textbox, submit, reset, check box, radio buttons, select list, and multiple select list. Each of these form elements except for submit and reset has a datatype (integer, decimal, or string) associated with it. If a datatype is not provided, string would be assumed as the default data type. If a data input form contains at least one multiselect form element or a check box group of two or more check boxes, one or more of the remaining (single valued) form elements must be classified as key elements. This is to facilitate creating a separate relational table for storing the multiple select values. Some of the aspects of data input forms are not relevant for this problem. Here are two examples of data input forms:
    
    [form1.xml](http://tinman.cs.gsu.edu/~raj/8711/sp21/p2/form1.xml)
    
    [form2.xml](http://tinman.cs.gsu.edu/~raj/8711/sp21/p2/form2.xml)
    
    Write an XSL program to transform a data input form into HTML that renders the data input form.
    

#### What to Submit?

The following files:

1. mo.xsd
2. s1.xq, s2.xq, s3.xq, s4.xq, s5.xq, s6.xq, and s7.xq
3. c1.xq, c2.xq, c3.xq, c4.xq, and c5.xq
4. form.xsl
