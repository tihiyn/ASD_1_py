from typing import List
from typing import Any
from typing import Optional
from typing import Tuple

"""
Задание 9, задача 5: словарь с использованием упорядоченного списка по ключу
"""
class SortedNativeDictionary:
    def __init__(self, asc: bool) -> None:
        self.__ascending: bool = asc
        self.slots: List[str] = []
        self.values: List[Optional[Any]] = []
        
    def compare(self, k1: str, k2: str) -> int:
        s1: str = k1.strip()
        s2: str = k2.strip()
        if s1 < s2:
            return -1
        if s1 > s2:
            return 1  
        return 0  
        
    def _search(self, key: str) -> Tuple[int, bool]:
        left: int = 0
        right: int = len(self.slots)
        while left < right:
            med: int =  left + (right - left) // 2
            if self.compare(key, self.slots[med]) == 0:
                return med, True
            if self.__ascending == (self.compare(key, self.slots[med]) < 0):
                right = med
                continue
            left = med + 1    
        return left, False    

    """
    Сложность алгоритма:
        - временная: O(log2(N))
        - пространственная: O(1).
    """
    def is_key(self, key: str) -> bool:
        idx, fnd = self._search(key)
        return fnd

    """
    Сложность алгоритма:
        - временная: O(N)
        - пространственная: O(1).
    """
    def put(self, key: str, value: Optional[Any]) -> None:
        idx, fnd = self._search(key)
        if fnd:
            self.values[idx] = value
            return
        self.slots.insert(idx, key)
        self.values.insert(idx, value)    
                

    """
    Сложность алгоритма:
        - временная: O(log2(N))
        - пространственная: O(1).
    """
    def get(self, key: str) -> Optional[Any]:
        idx, fnd = self._search(key)
        if fnd:
            return self.values[idx]
        return None    
        
    """
    Сложность алгоритма:
        - временная: O(N)
        - пространственная: O(1).
    """
    def delete(self, key: str) -> bool:
        idx, fnd = self._search(key)
        if not fnd:
            return False
        self.slots.pop(idx)    
        self.values.pop(idx)
        return True
        
"""
Задание 9, задача 6: словарь, в котором ключи представлены битовыми строками фиксированной длины.
Сложность:
    - временная: O(1)
    - пространственная: O(2^L), где L - длина ключа.
"""
class BitStringNativeDictionary:
    def __init__(self, ks: int) -> None:
        self.__key_size: int = ks
        self.size: int = 1 << ks
        self.slots: List[Optional[str]] = [None] * self.size
        self.values: List[Optional[Any]] = [None] * self.size

    def _index(self, key: str) -> Optional[int]:
        if len(key) != self.__key_size:
            return None
        idx: int = 0
        for ch in key:
            bit: int = ord(ch) - ord("0")
            if bit & ~1:
                return None
            idx = (idx << 1) | bit
        return idx

    def is_key(self, key: str) -> bool:
        idx: Optional[int] = self._index(key)
        if idx is None:
            return False
        return self.slots[idx] is not None

    def put(self, key: str, value: Optional[Any]) -> None:
        idx: Optional[int] = self._index(key)
        if idx is None:
            return
        self.slots[idx] = key
        self.values[idx] = value

    def get(self, key: str) -> Optional[Any]:
        idx: Optional[int] = self._index(key)
        if idx is None or self.slots[idx] is None:
            return None
        return self.values[idx]

    def delete(self, key: str) -> bool:
        idx: Optional[int] = self._index(key)
        if idx is None or self.slots[idx] is None:
            return False
        self.slots[idx] = None
        self.values[idx] = None
        return True

"""
рефлексия

Задание 7, задача 9: да, решение аналогично задаче из предыдущего занятия.

Задание 7, задача 10: из упорядоченности списка вытекает множество возможных оптимизаций и ранних прерываний. Правда, не понятно, 
как ориентироваться на размер оставшейся части, так как индексации нет. Про бинарный поиск аналогично.

Задание 7, задача 11: решение совпадает с предложенным.

Задание 7, задача 12: тут меня запутало условие, в котором говорилось, что нужно именно добавить новый метод в уже существующий 
класс. А на самом деле, нужно было переписать полностью класс на другой структуре данных, чтобы появилась возможность индексации ->
бинарного поиска. С индексами действительно нужно аккуратно) Пока не написал все возможные тесты, алгоритм содержал ошибки.
""" 


