from power_set import PowerSet
from typing import Any
from typing import Optional
from typing import List
from typing import Tuple

"""
Задание 10, задача 4: декартово произведение множеств.
"""
class CartesianPowerSet:
    def __init__(self) -> None:
        self.d: dict = {}

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

    def intersection(self, set2: CartesianPowerSet) -> CartesianPowerSet:
        res: CartesianPowerSet = CartesianPowerSet()
        for k in self.d:
            if set2.get(k):
                res.put(k)
        return res

    def union(self, set2: CartesianPowerSet) -> CartesianPowerSet:
        res: CartesianPowerSet = CartesianPowerSet()
        for k in self.d:
            res.put(k)
        for k in set2.d:
            res.put(k)
        return res

    def difference(self, set2: CartesianPowerSet) -> CartesianPowerSet:
        res: CartesianPowerSet = CartesianPowerSet()
        for k in self.d:
            if set2.get(k):
                continue
            res.put(k)    
        return res

    def issubset(self, set2: CartesianPowerSet) -> bool:
        res: CartesianPowerSet = CartesianPowerSet()
        for k in set2.d:
            if self.get(k):
                continue
            return False    
        return True

    def equals(self, set2: CartesianPowerSet) -> bool:
        if self.size() != 0 and self.difference(set2).size() == 0:
            return True
        return False
    
    """
    Сложность алгоритма:
        - временная: O(N*M)
        - пространственная: O(N+M).
    """
    def cartesian(self, set2: CartesianPowerSet) -> CartesianPowerSet:
        res: CartesianPowerSet = CartesianPowerSet()
        for k1 in self.d:
            for k2 in set2.d:
                res.put((k1, k2))
        return res


"""
Задание 10, задача 5: пересечение 3 и более множеств.
Сложность алгоритма:
    - временная: O(K), где K - общее кол-во элементов во всех множествах
    - пространственная: O(L), где L - кол-во уникальных значений среди всех множеств.
"""
def universal_intersection(sets: List[PowerSet]) -> PowerSet:
    res: PowerSet = PowerSet()
    for set in sets:
        for k in set.d:
            res.put(k)
    return res        
    
"""
Задание 10, задача 6: мульти-множество.
"""
class Bag:
    def __init__(self) -> None:
        self.d: dict[Any, int] = {}
    
    """
    Сложность алгоритма:
        - временная: O(1)
        - пространственная: O(1).
    """
    def put(self, value: Any) -> None:
        self.d[value] = self.d.get(value, 0) + 1
    
    """
    Сложность алгоритма:
        - временная: O(N)
        - пространственная: O(N).
    """
    def get(self) -> List[Tuple[Any, int]]:
        res: List[Tuple[Any, int]] = []
        for k, v in self.d.items():
            res.append((k, v))
        return res    
    
    """
    Сложность алгоритма:
        - временная: O(1)
        - пространственная: O(1).
    """
    def remove(self, value: Any) -> bool:
        freq: Optional[int] = self.d.get(value)
        if freq is None:
            return False
        self.d[value] = freq - 1
        if self.d.get(value) == 0:
            self.d.pop(value)
        return True  


"""
рефлексия

Задание 8, задача 3: забыл про композицию и смешал 2 структуры данных в одной:(

Задание 8, задача 5: да, как и упомянуто в предложенном решении, сделал статическую соль, что не есть
хорошо. Я изначально это понимал, но не додумался до идеи хранить пару "ключ-соль".
"""         