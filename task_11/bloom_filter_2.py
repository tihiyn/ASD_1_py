from bloom_filter import BloomFilter
from typing import List

"""
Задание 11, задача 2: слияние нескольких фильтров Блюма
Сложность алгоритма:
    - временная: O(filter_len)
    - пространственная: O(filter_len)
Вероятность ложного срабатывания для итогового фильтра увеличится    
"""
def merge(bfs: List[BloomFilter]) -> BloomFilter:
    res: BloomFilter = BloomFilter(bfs[0].filter_len)
    res.filter = -1
    for bf in bfs:
        res.filter = res.filter & bf.filter
    return res

"""
Задание 11, задача 3: фильтр Блюма с поддержкой удаления
"""    
class RemoveBloomFilter:
    def __init__(self, f_len: int) -> None:
        self.filter_len: int = f_len
        self.filter: List[int] = [0] * f_len

    def hash1(self, str1: str) -> int:
        h: int = 0
        for c in str1:
            code: int = ord(c)
            h = h * 17 + code
        return h % self.filter_len

    def hash2(self, str1: str) -> int:
        h: int = 0
        for c in str1:
            code: int = ord(c)
            h = h * 223 + code
        return h % self.filter_len

    def add(self, str1: str) -> None:
        h1: int = self.hash1(str1)
        h2: int = self.hash2(str1)
        self.filter[h1] += 1
        self.filter[h2] += 1
    
    """
    Сложность алгоритма:
    - временная: O(filter_len)
    - пространственная: O(filter_len)
    """
    def remove(self, str1: str) -> None:
        h1: int = self.hash1(str1)
        h2: int = self.hash2(str1)
        self.filter[h1] = max(0, self.filter[h1] - 1)
        self.filter[h2] = max(0, self.filter[h2] - 1)

    def is_value(self, str1: str) -> bool:
        h1: int = self.hash1(str1)
        h2: int = self.hash2(str1)
        return self.filter[h1] > 0 and self.filter[h2] > 0
        
"""
Задание 11, задача 4: восстановить исходные данные по конфигурации фильтра Блюма

Схема работы алгоритма: кажется, что нужно перебирать все возможные пары единиц битового массива (не
забыть, что коммутативности нет). Но как потом, даже зная хэш-функцию, восстановить символы - 
непонятно. Ведь уравнение idx = h % f_len имеет бесконечное ко-во решений. Как результат, мы, возможно, 
и получим множество всех исходных значений, но будет ещё и много ошибочных значений.
"""      

"""
рефлексия

Задание 9, задача 5: не понял, зачем добавлять значения в конец списка значений, а не "напротив" ключа.
Ведь для этого вместо ключа нужно хранить пару <ключ, индекс значения> и переопределять операцию 
сравнения. Кажется, что всего этого можно избежать, если индексы ключа и значения будут совпадать.
Про производительность согласен, тоже сразу после прочтения задания в голове была мысль использовать
деревья.
"""