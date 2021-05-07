(: Retrieve the names of employees who work on all 
projects controlled by department "5"
M :)
distinct-values(let $c:=count(db:open("companyDB")//projects/project[@controllingDepartment = "5"])
return
for $t in db:open("companyDB")//projects
return 
for $v in $t/project[@controllingDepartment = "5"]/workers/worker
where count($t/project[@controllingDepartment = "5"]/workers/worker[@essn eq $v/@essn]) = $c
return concat(db:open("companyDB")//employees/employee[@ssn eq $v/@essn]/fname," ",db:open("companyDB")//employees/employee[@ssn eq $v/@essn]/lname))
(: return 
concat(db:open("companyDB")//employees/employee[@ssn eq $v/@essn]/@ssn,
" ",$c," ",
count($t/project[@controllingDepartment = "4"]/workers/worker[@essn eq $v/@essn])) :)