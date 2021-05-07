(: For every project located in "Stafford", 
retrieve the project number, the controlling
 department number, and the department’s manager’s 
 last name, address, and birth date. :)

for $t in db:open("companyDB")//projects/project
where $t/plocation/text() = "Stafford"
return
for $e in db:open("companyDB")//employees/employee
where $t/@controllingDepartment = $e/@manages
return concat($t/@pnumber," ,  ",$t/@controllingDepartment," , ",$e/lname," , ",$e/address," , ",$e/dob)



