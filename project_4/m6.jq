(: Get order number and total price for each order. :)

for $x in json-doc("mo.json").ORDERS[]

return {"ONO":$x.ONO,"total":sum(for $y in $x.ITEMS[] return for $z in json-doc("mo.json").PARTS[][$y.PARTNUMBER eq $$.PNO]
return $z.PRICE*$y.QUANTITY)}