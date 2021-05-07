### Csc 8711, Databases and the Web - Project 3

**Due**: Sunday, March 21st  
Teams of 2 (please email me the team memberships as soon as possible)

#########################################################################
#
Contributors:
#
Varchaleswari Ganugapati, email : vganugapati1@student.gsu.edu
Bhagirath Tallapragada, email : btallapragada1@student.gsu.edu
#
#########################################################################

### JSON Parsing

In this project, you will write a Python program that processes JSON files containing information about data input forms. The Python program takes as command line input a JSON file name and produces as output the following five files:

1. An HTML file that contains code to display the data input form on a browser.
2. Javascript file (to go along with the HTML file) to perform some basic validation such as data type checking for text box input as well as check for required fields. In addition, a Javascript function, called submitData, that sends the form data to a backend service for storing in a MySQL database.
3. A MySQL script file that contains create table statements to create relational table(s) that can accept data submitted from the data input form.
4. A backend Python RESTful API (not GraphQL) program with two endpoints:
    - /webforms/insert  
        This endpoint processes data submitted by the user using the data input form. The endpoint should simply insert the data into the database table(s).
    - /webforms/display  
        This endpoint simply returns the contents of the entire database, including table names, table schemas, and table contents.
5. An HTML file that contains a button; upon click the page should display the contents of the database (basically a dump of all the tables in the database); The Javascript function, called displayData, that reacts to the button click can be included in the earlier Javascript file itself.

The output files should be named after the "name" field of the data input form. For example, for form2.json, you will produce the following files:

interests.html
interests.js
interests.sql
interests.py
interests\_display.html

### Data Input Forms

A data input form consists of one or more form elements that is capable of accepting input from a user. We shall consider 7 types of form elements: textbox, submit, reset, check box, radio buttons, select list, and multiple select list. Each of these form elements except for submit and reset has a datatype (integer or string) associated with it.

If a data input form contains at least one multiselect form element or a checkbox group, one or more of the remaining (single valued) form elements must be classified as key elements. This is to facilitate creating a separate relational table for storing the multiple select values.

The data input form is described in JSON. Some sample forms are shown below:

- [form1.json](http://tinman.cs.gsu.edu/~raj/8711/sp21/p3/form1.json).
- [form2.json](http://tinman.cs.gsu.edu/~raj/8711/sp21/p3/form2.json).

### MySQL Database

The data input form is intended to collect data from users. This data needs to be stored in a MySQL database. If there are no "checkbox" or "multiselectlist" elements in the form, all of the data can be stored in a row of a main table. However, if there are any "checkbox" or "multiselect" elements in the data input form then we would need a separate table, one for each such element, to store the multiple values that are being submitted by the user. So, the number of MySQL tables you would have to create would be n+1, where n is the number of checkbox and multiselectlist elements.

### JSON Schema for Data Input Forms

Some comments on the JSON schema for data input forms (Note: You do not have to write a JSON Schema for this!, although it would be nice to do so and validate the data input form JSON files):

- Every data input form has "id", "name", and "caption" fields that are self explanatory. The "id" field is ignored in this project.
- The data form also contains a "backendURL" field that points to the backend endpoint. It also contains credentials to a MySQL database.
- The most important field in the data input form is "elements", which contains an array of an arbitrary number of form elements, each of which is one of 7 types: textbox, selectlist, radiobutton, selectlist, checkbox, multiselectlist, submit, and reset. We can assume that there is exactly one submit and one reset element, however there can any number of any of the other element types.
- the example data input forms contain examples of each of the 7 element types and are self explanatory.

### No Syntactic and Semantic Checks to be implemented

In this assignment, we will assume that the JSON file is well formed, both syntactically and semantically. However you can imagine that it may have to conform to a JSON Schema. In addition, it may have to satisfy certain semantic checks which the JSON schema cannot capture. If you have time, you may complete these checks for extra credit.

### What to Submit?

1. Your Python program (under the name WebForms.py); You may include other Python files, but the main program should be in WebForms.py
2. A short report documenting the project including contributions of group members. (1-2 pages in pdf).
