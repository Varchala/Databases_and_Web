(: xquery /ships/class[@numGuns>=10]/@name :)

for $t in db:open("shipsDB")//class[@numGuns>=10]/@name
return $t