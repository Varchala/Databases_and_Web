
distinct-values(for $tt in db:open("shipsDB")//class
return
for $t in $tt/ship/@launched
let $ft := count($tt/ship[@launched eq $t])
let $ftt := $tt/ship[@launched eq $t]
where $ft > 1
return $tt/@name)