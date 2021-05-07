for $c in distinct-values(db:open("shipsDB")//class/ship/battle/text())
    return
    <battle name="{$c}">
    {
      for $p in db:open("shipsDB")//class/ship
      where $p/battle/text() = $c
      return <ship name="{$p/@name}" />
    }
    </battle>