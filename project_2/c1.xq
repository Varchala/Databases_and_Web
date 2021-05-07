(: Retrieve the names and addresses of employees 
who work for the "Research" department. :)

for $t in db:open("companyDB")//departments/department
where $t/dname/text() = "Research"
return
for $e in db:open("companyDB")//employees/employee
where contains($t/employees/@essns,$e/@ssn)
return concat($e/fname," ",$e/lname," , ",$e/address)

