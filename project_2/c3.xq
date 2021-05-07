(: Retrieve the names of all employees who have two or more dependents :)

for $t in db:open("companyDB")//employees/employee
where count($t/dependents/dependent[string(.)])>1
return concat($t/fname," ",$t/lname)