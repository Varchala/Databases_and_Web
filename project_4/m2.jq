(: Get the names of customers who have ordered all parts costing less than 20.00. :)
distinct-values(
for $x in json-doc("mo.json").ORDERS[]
return
let $text :=count(json-doc("mo.json").PARTS[][$$.PRICE < 20])
return
for $z in json-doc("mo.json").CUSTOMERS[]
where count(for $z in json-doc("mo.json").PARTS[]
return $x.ITEMS[][$z.PNO eq $$.PARTNUMBER and $z.PRICE < 20]) eq $text and $z.CNO eq $x.CUSTOMER 
return $z.CNAME)