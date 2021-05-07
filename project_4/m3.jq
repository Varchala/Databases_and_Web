(: Get the names of employees who have never 
made a sale to a customer living in their own zipcode. :)

for $x in json-doc("mo.json").EMPLOYEES[]
where count(for $z in json-doc("mo.json").ORDERS[][$x.ENO eq $$.TAKENBY]
where json-doc("mo.json").CUSTOMERS[][$$.CNO eq $z.CUSTOMER].ZIP eq $x.ZIP
return $x.ENAME) eq 0
return $x.ENAME
