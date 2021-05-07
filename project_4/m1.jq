(: Get the names of customers who have ordered parts from employees living in Wichita. :)
(:spark-submit %SPARK_HOME%\BIN\spark-rumble-1.11.0.jar --shell yes:)
distinct-values(for $x in json-doc("mo.json").ORDERS[]
return
for $y in json-doc("mo.json").EMPLOYEES[]
where $x.TAKENBY eq $y.ENO and $y.CITY eq "Wichita"
return
for $z in json-doc("mo.json").CUSTOMERS[]
where $z.CNO eq $x.CUSTOMER 
return $z.CNAME)
