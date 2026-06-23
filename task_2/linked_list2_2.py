from linked_list2 import Node, LinkedList2
from typing import Any

"""
Задание 2, задача 10: изменение порядка элементов в двусвязном списке на противоположный
Сложность алгоритма:
    - временная: O(N)
    - пространственная: O(1).
"""
def invert(ll: LinkedList2) -> None:
    len: int = ll.len()
    if len < 2:
        return None
    l: Node = ll.head
    r: Node = ll.tail
    for i in range(len // 2):
        _swap(l, r)
        l = l.next
        r = r.prev
        
def _swap(n1: Node, n2: Node) -> None:
    tmp: Any = n1.value
    n1.value = n2.value
    n2.value = tmp
    
"""
Задание 2, задача 11: проверка наличия циклов в двусвязном списке
Сложность алгоритма:
    - временная: O(N)
    - пространственная: O(1).
"""
def is_cycled(ll: LinkedList2) -> bool:
    return _is_cycled_by_next(ll) or _is_cycled_by_prev(ll)
    
def _is_cycled_by_next(ll: LinkedList2) -> bool:
    fst: Node = ll.head
    snd: Node = ll.head
    while snd is not None and snd.next is not None:
        fst = fst.next
        snd = snd.next.next
        if fst == snd:
            return True
    return False        
     
def _is_cycled_by_prev(ll: LinkedList2) -> bool:
    fst: Node = ll.tail
    snd: Node = ll.tail
    while snd is not None and snd.prev is not None:
        fst = fst.prev
        snd = snd.prev.prev
        if fst == snd:
            return True
    return False

"""
Задание 2, задача 12: сортировка двусвязного списка
Сложность алгоритма:
    - временная: O(N^2)
    - пространственная: O(1).
"""
def sort(ll: LinkedList2) -> None:
    len: int = ll.len()
    if len < 2:
        return None
    node: Node = ll.head
    for i in range(len):
        node = ll.head
        while node.next is not None:
            if node.value.__gt__(node.next.value):
                _swap(node, node.next)
            node = node.next
    
"""
Задание 2, задача 13: слияние двух двусвязных списков в один отсортированный
Сложность алгоритма:
    - временная: O(N^2+M^2)
    - пространственная: O(N+M).
"""
def merge(f: LinkedList2, s: LinkedList2) -> LinkedList2:
    sort(f)
    sort(s)
    f_p: Node = f.head
    s_p: Node = s.head
    res: LinkedList2 = LinkedList2()
    while f_p is not None and s_p is not None:
        if f_p.value.__gt__(s_p.value):
            res.add_in_tail(Node(s_p.value))
            s_p = s_p.next
            continue
        res.add_in_tail(Node(f_p.value))
        f_p = f_p.next
    while f_p is not None:
        res.add_in_tail(f_p)
        f_p = f_p.next
    while s_p is not None:
        res.add_in_tail(s_p)
        s_p = s_p.next  
    return res
    
"""
Задание 2, задача 14: реализация двусвязного списка с dummy-узлами
"""
class DummyNode(Node):
    def __init__(self) -> None:
        super().__init__(None)

class DummyLinkedList:
    def __init__(self) -> None:
        self._head = DummyNode()
        self._tail = DummyNode()
        self._head.next = self._tail
        self._tail.prev = self._head
        
    """
    Сложность алгоритма:
    - временная: O(1)
    - пространственная: O(1).
    """
    def add_in_tail(self, item: Node) -> None:
        self.insert(self._tail.prev, item)
    
    """
    Сложность алгоритма:
    - временная: O(1)
    - пространственная: O(1).
    """
    def insert(self, afterNode: Node | None, newNode: Node) -> None:
        if (afterNode is None):
            afterNode = self._define_after_node()
        nxt: Node = afterNode.next
        afterNode.next = newNode
        newNode.prev = afterNode
        newNode.next = nxt
        nxt.prev = newNode
        
    def _define_after_node(self) -> Node:
        if self._head.next == self._tail:
            return self._head
        return self._tail.prev   
        
    """
    Сложность алгоритма:
    - временная: O(N)
    - пространственная: O(1).
    """    
    def delete(self, val: Any, all: bool=False) -> None:
        node: Node = self._head
        while not isinstance(node, DummyNode):
            if node.value == val and all:
                self._delete(node)
                node = node.next
                continue
            if node.value == val:
                self._delete(node)
                break
            node = node.next   
    
    def _delete(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    
"""
рефлексия:
  - Задание 1, задача 8: почему-то в текущем задании не было рекомендуемого алгоритма решения. Сама
  задача тривиальная. Но если задуматься, то элементы связного списка могут быть произвольного типа,
  и просто так сложить их через '+' в реальной жизни не получится.
"""    
    

