for $t in db:open("shipsDB")//class
let $ft := count($t/ship/battle)
where $ft = 0
return $t/@name