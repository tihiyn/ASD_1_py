from ordered_list import OrderedList
from ordered_list import Node
from typing import Any

"""
Задание 7, задача 8: удаление дубликатов из упорядоченного списка
Сложность алгоритма:
    - временная: O(N)
    - пространственная: O(1).
"""
def remove_duplicates(ol: OrderedList) -> None:
    if ol.head is None or ol.head == ol.tail:
        return
    cur: Node = ol.head
    while cur.next is not None:
        if cur.value.__eq__(cur.next.value):
            remove_duplicate(ol, cur)
            continue
        cur = cur.next    
    
def remove_duplicate(ol: OrderedList, n: Node) -> None:
    if n.next.next is None:
        n.next = None
        ol.tail = n
        return
    n.next.next.prev = n
    n.next = n.next.next
    
"""
Задание 7, задача 9: слияние двух упорядоченных списков в один
Сложность алгоритма:
    - временная: O(N + M)
    - пространственная: O(N + M).
"""    
def merge(f: OrderedList, s: OrderedList) -> OrderedList:    
    res: OrderedList = OrderedList(f._OrderedList__ascending)
    if f._OrderedList__ascending != s._OrderedList__ascending:
        return res
    f_p: Node = f.head
    s_p: Node = s.head
    while f_p is not None and s_p is not None:
        if f._OrderedList__ascending == (f.compare(f_p.value, s_p.value) > 0):
            append(res, s_p.value)
            s_p = s_p.next
            continue
        append(res, f_p.value)
        f_p = f_p.next
    while f_p is not None:
        append(res, f_p.value)
        f_p = f_p.next
    while s_p is not None:
        append(res, s_p.value)
        s_p = s_p.next  
    return res
    
def append(res: OrderedList, value: Any) -> None:
    n = Node(value)
    n.prev = res.tail
    if res.tail is None:
        res.head = n
        res.tail = n 
        return
    res.tail.next = n
    res.tail = n   
    
"""
Задание 7, задача 10: проверка наличия заданного упорядоченного под-списка в текущем списке
Сложность алгоритма:
    - временная: O(N * M)
    - пространственная: O(1).
"""
def contains_sublist(self, sub: OrderedList) -> bool:
    if sub.head is None:
        return True
    if self.__ascending != sub.__ascending:
        return False
    outer: Node = self.head
    while outer is not None:
        cur_self: Node = outer
        cur_sub: Node = sub.head
        while cur_sub is not None and cur_self is not None and self.compare(cur_self.value, cur_sub.value) == 0:
            cur_self = cur_self.next
            cur_sub = cur_sub.next
        if cur_sub is None:
            return True
        if self.__ascending == self.compare(outer.value, sub.head.value) > 0:
            break
        outer = outer.next
    return False    
    
"""
Задание 7, задача 11: наиболее часто встречающееся значение в списке
Сложность алгоритма:
    - временная: O(N)
    - пространственная: O(1).
"""    
def most_frequent_value(self) -> Any | None:
    if self.head is None:
        return None
    most_frequent_value: Any = self.head.value
    max_frequency: int = 1
    cur_value: Any = self.head.value
    cur_frequency: int = 1
    node: Node | None = self.head.next
    while node is not None:
        if self.compare(node.value, cur_value) != 0:
            cur_value = node.value
            cur_frequency = 1
            node = node.next
            continue
        cur_frequency += 1
        if cur_frequency > max_frequency:
            max_frequency = cur_frequency
            most_frequent_value = cur_value
        node = node.next
    return most_frequent_value

"""
Задание 7, задача 12: найти индекс элемента в списке
Сложность алгоритма:
    - временная: o(log N)
    - пространственная: O(1).
"""    
def get_index(self, val: Any) -> int | None:
    if self.head is None:
        return None
    begin: int = 0
    end: int = self.len() - 1
    node: Node = self.head
    while begin <= end:
        step: int = (end - begin) // 2
        mid_node: Node = self._move(node, step)
        comparing: int = self.compare(mid_node.value, val)
        if comparing == 0:
            return begin + step
        if (comparing < 0) == self.__ascending:
            begin = begin + step + 1
            node = mid_node.next
            continue
        end = begin + step - 1
    return None

def _move(self, node: Node, step: int) -> Node:
    for _ in range(step):
        node = node.next
    return node
    
"""
рефлексия

Задание 5, задача 3:
Решение соответствует предложенному.

Задание 5, задача 4:
Логику с двумя стеками переливаниями реализовал верно.

Задание 5, задача 5:
Решение соответствует предложенному, главное было не запутаться с порядком элементов в стеке и 
очереди.

Задание 5, задача 6:
Всё сделал правильно. Ключевой момент был в том, чтобы верно реализовать переход между границами.
Верно подмечено, что важно различать состояния "пусто" и "полно". Проверку на полноту реализовал 
по-другому и не стал оставлять одну пустую ячейку между head и tail, так как всегд известно кол-во
элементов.
"""    

