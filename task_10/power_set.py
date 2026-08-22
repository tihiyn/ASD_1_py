from __future__ import annotations
from typing import Any
from typing import Optional

class PowerSet:

    def __init__(self) -> None:
        self.d: dict[Any, None] = {}

    def size(self) -> int:
        return len(self.d)

    def put(self, value: Any) -> None:
        self.d[value] = None

    def get(self, value: Any) -> bool:
        if value in self.d:
            return True
        return False

    def remove(self, value: Any) -> bool:
        if self.get(value):
            self.d.pop(value)
            return True
        return False

    def intersection(self, set2: PowerSet) -> PowerSet:
        res: PowerSet = PowerSet()
        for k in self.d:
            if set2.get(k):
                res.put(k)
        return res

    def union(self, set2: PowerSet) -> PowerSet:
        res: PowerSet = PowerSet()
        for k in self.d:
            res.put(k)
        for k in set2.d:
            res.put(k)
        return res

    def difference(self, set2: PowerSet) -> PowerSet:
        res: PowerSet = PowerSet()
        for k in self.d:
            if set2.get(k):
                continue
            res.put(k)    
        return res

    def issubset(self, set2: PowerSet) -> bool:
        res: PowerSet = PowerSet()
        for k in set2.d:
            if self.get(k):
                continue
            return False    
        return True

    def equals(self, set2: PowerSet) -> bool:
        if self.size() != 0 and self.difference(set2).size() == 0:
            return True
        return False



        