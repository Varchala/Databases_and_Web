for $t in db:open("shipsDB")//class
let $ft := count($t/ship)
where $ft > 2
return $t/@name