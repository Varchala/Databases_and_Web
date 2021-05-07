for $t in db:open("shipsDB")//class/ship
where $t/battle/@outcome = "sunk"
return $t/@name