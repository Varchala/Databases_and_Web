(: For each employee, find a list of Order 
Numbers they have taken :)
for $x in json-doc("mo.json").EMPLOYEES[]
let $k := for $z in json-doc("mo.json").ORDERS[][$x.ENO eq $$.TAKENBY] return $z.ONO
where count($k) > 0
return {"eno":$x.ENO,"ono":[$k]}
