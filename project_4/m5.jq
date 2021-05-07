(: Get order numbers of orders that took 
longer than 2 days to ship. :)

for $x in json-doc("mo.json").ORDERS[]
where ((date($x.SHIPPEDDATE) - date($x.RECEIVEDDATE)) > dayTimeDuration("P2D"))
return $x.ONO