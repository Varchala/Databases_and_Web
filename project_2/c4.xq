(: Retrieve the names of managers who have at least one dependent. :)

for $t in db:open("companyDB")//employees/employee
where count($t/dependents/dependent[string(.)])>0 and count($t[@manages])>0
return concat($t/fname," ",$t/lname)