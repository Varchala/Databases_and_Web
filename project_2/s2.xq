 (:xquery /ships/class[@numGuns>=10]/ship/@name:)

for $t in db:open("shipsDB")//class[@numGuns>=10]/ship/@name
return $t