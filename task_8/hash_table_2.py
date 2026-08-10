import ctypes
import random
from typing import Any
from typing import List

"""
Задание 8, задача 3: динамическая хэш-таблица
"""
class DynHashTable:
    def __init__(self, sz: int, stp: int, threshold: float = 0.75) -> None:
        self.size: int = sz
        self.step: int = stp
        self.threshold: float = threshold
        self.count: int = 0
        self.slots: ctypes.Array = self.make_array(self.size)

    def make_array(self, new_size: int) -> ctypes.Array:
        new_slots: ctypes.Array = (new_size * ctypes.py_object)()
        for i in range(new_size):
            new_slots[i] = None
        return new_slots

    def hash_fun(self, value: str) -> int:
        h: int = 0
        for ch in value:
            h = (h * 31 + ord(ch)) % (10**9 + 7)
        return h % self.size

    def seek_slot(self, value: str) -> int | None:
        idx: int = self.hash_fun(value)
        for _ in range(self.size):
            if self.slots[idx] is None or self.slots[idx] == value:
                return idx
            idx = (idx + self.step) % self.size
        return None

    """
    Сложность алгоритма:
    - временная: O(N)
    - пространственная: O(N).
    """
    def resize(self) -> None:
        old_slots: ctypes.Array = self.slots
        old_size: int = self.size
        self.size = old_size * 2
        self.slots = self.make_array(self.size)
        for i in range(old_size):
            if old_slots[i] is None:
                continue
            self.slots[self._seek_free_slot(old_slots[i])] = old_slots[i]

    def _seek_free_slot(self, value: str) -> int:
        idx: int = self.hash_fun(value)
        while self.slots[idx] is not None:
            idx = (idx + self.step) % self.size
        return idx

    """
    Сложность алгоритма:
    - временная: o(1) (амортизированная)
    - пространственная: o(1) (амортизированная)
    """
    def put(self, value: str) -> int | None:
        if self.count + 1 > self.threshold * self.size:
            self.resize()
        idx: int | None = self.seek_slot(value)
        if idx is None:
            return None
        if self.slots[idx] is None:
            self.count += 1
        self.slots[idx] = value
        return idx

    def find(self, value: str) -> int | None:
        idx: int = self.hash_fun(value)
        for _ in range(self.size):
            if self.slots[idx] is None:
                return None
            if self.slots[idx] == value:
                return idx
            idx = (idx + self.step) % self.size
        return None


"""
Задание 8, задача 4: хэш-таблица с двойным хэшированием

Дано:
    - хэш-таблица на 1099 слотов;
    - заолненность 75%.
    
Цена коллизии - среднее количество просмотренных слотов таблицы на одну операцию        
1. Цена коллизии на произвольных ключах:
    a. Успешный поиск: DHT - 1.99, HT - 2.60
    b. Неуспешный поиск: DHT - 4.18, HT - 9.61
    
2. Цена коллизии на почти последовательных ключах:
    a. Успешный поиск: DHT - 1.91, HT - 68.73
    b. Неуспешный поиск: DHT - 5.44, HT - 326.34
    
3. Среднее время выполнения метода find (мкс):
    a. На произвольных ключах: DHT - 1.26, HT - 0.71
    b. На почти последовательных ключах: DHT - 0.73, HT - 3.18  
"""
class DoubleHashTable:
    def __init__(self, sz: int) -> None:
        self.size: int = sz
        self.count: int = 0
        self.slots: List[Any] = [None] * self.size

    def hash_fun1(self, value: str) -> int:
        h: int = 0
        for ch in value:
            h = (h * 31 + ord(ch)) % (10**9 + 7)
        return h % self.size

    def hash_fun2(self, value: str) -> int:
        h: int = 0
        for ch in value:
            h = (h * 131 + ord(ch)) % (10**9 + 9)
        return 1 + h % (self.size - 1)

    """
    Сложность алгоритма:
    - временная: o(1)
    - пространственная: O(1).
    """
    def seek_slot(self, value: str) -> int | None:
        idx: int = self.hash_fun1(value)
        step: int = self.hash_fun2(value)
        for _ in range(self.size):
            if self.slots[idx] is None or self.slots[idx] == value:
                return idx
            idx = (idx + step) % self.size
        return None

    """
    Сложность алгоритма:
    - временная: o(1)
    - пространственная: O(1).
    """
    def put(self, value: str) -> int | None:
        idx: int | None = self.seek_slot(value)
        if idx is None:
            return None
        if self.slots[idx] is None:
            self.count += 1
        self.slots[idx] = value
        return idx

    """
    Сложность алгоритма:
    - временная: o(1)
    - пространственная: O(1).
    """
    def find(self, value: str) -> int | None:
        idx: int = self.hash_fun1(value)
        step: int = self.hash_fun2(value)
        for _ in range(self.size):
            if self.slots[idx] is None:
                return None
            if self.slots[idx] == value:
                return idx
            idx = (idx + step) % self.size
        return None


"""
Задание 8, задача 5: ddos-атака и хэш-таблица с солью
"""

COLLISION_BLOCKS: List[str] = ["aa", "bB"]

def generate_ddos_keys(count: int) -> List[str]:
    keys: List[str] = [""]
    while len(keys) < count:
        new_keys: List[str] = []
        for key in keys:
            for block in COLLISION_BLOCKS:
                new_keys.append(key + block)
        keys = new_keys
    return keys[:count]


class SaltedHashTable:
    def __init__(self, sz: int, stp: int) -> None:
        self.size: int = sz
        self.step: int = stp
        self.salt: int = random.randrange(1, 10**9 + 7)
        self.base: int = random.randrange(2, 10**9 + 7)
        self.slots: List[Any] = [None] * self.size

    def hash_fun(self, value: str) -> int:
        h: int = self.salt
        for ch in value:
            h = (h * self.base + ord(ch)) % (10**9 + 7)
        return h % self.size

    def seek_slot(self, value: str) -> int | None:
        idx: int = self.hash_fun(value)
        for _ in range(self.size):
            if self.slots[idx] is None or self.slots[idx] == value:
                return idx
            idx = (idx + self.step) % self.size
        return None

    def put(self, value: str) -> int | None:
        idx: int | None = self.seek_slot(value)
        if idx is None:
            return None
        self.slots[idx] = value
        return idx

    def find(self, value: str) -> int | None:
        idx: int = self.hash_fun(value)
        for _ in range(self.size):
            if self.slots[idx] is None:
                return None
            if self.slots[idx] == value:
                return idx
            idx = (idx + self.step) % self.size
        return None


"""
рефлексия

Задание 6, задача 4: решение соответсвует предложенному.

Задание 6, задача 5: эта задача у меня вызвала затруднение ещё при первом прохождении курса. Сначала
я тоже пытался решить задачу с использованием доп. деки, но потом мне пришла идея использовать 2
объекта класса StackMin (стек, который возвращает минимум за O(1)) из задания про стек. Первый стек
отвечал за начало деки, второй - за конец, а при удалении используется механизм "переливания" из
одного стека в другой. 

Задание 6, задача 6: успешно применил композицию (дин.массив в очереди).
""" 


