from deque import Deque
from typing import Any
from typing import List
import ctypes

"""
Задание 6, задача 3: является ли строка палиндромом

Сложность алгоритма:
    - временная: O(N)
    - пространственная: O(N)
"""
def is_palindrom(s: str) -> bool:
    d: Deque = Deque()
    for ch in s:
        d.addTail(ch)    
    for i in range(d.size() // 2):
        if not(d.removeFront() == d.removeTail()):
            return False
    return True

"""
Задание 6, задача 4: минимальный элемент деки за O(1)
"""  
class DequeMin:
    def __init__(self):
        self.front = StackMin()
        self.tail = StackMin()
    
    def addFront(self, item: Any) -> None:
        self.front.push(item)
    
    def addTail(self, item: Any) -> None:
        self.tail.push(item)
    
    def removeFront(self) -> Any | None:
        if self.size() == 0:
            return None
        if self.front.size() == 0:
            for i in range(self.tail.size()):
                self.front.push(self.tail.pop())
        return self.front.pop()
        
    def removeTail(self) -> Any | None:
        if self.size() == 0:
            return None
        if self.tail.size() == 0:
            for i in range(self.front.size()):
                self.tail.push(self.front.pop())
        return self.tail.pop()
    
    """
    Сложность алгоритма:
        - временная: O(1)
        - пространственная: O(1)
    """
    def min(self) -> Any:
        if self.front.min().__lt__(self.tail.min()):
            return self.front.min()
        return self.tail.min()

    def size(self) -> int:
        return self.front.size() + self.tail.size()
        
class StackMin:
    def __init__(self) -> None:
        self.stack: List[Any] = []
        self.min_stack: Stack = Stack()

    def size(self) -> int:
        return len(self.stack)
    
    def pop(self) -> Any:
        if self.size() == 0:
            return None
        res: Any = self.stack.pop(-1)
        if res == self.min_stack.peek():
            self.min_stack.pop()
            return res
        tmp: Any = self.min_stack.pop()
        self.min_stack.pop()
        self.min_stack.push(tmp)
        return res

    def push(self, value: Any) -> None:
        self.stack.append(value)
        if self.min_stack.size() == 0 or value.__lt__(self.min_stack.peek()):
            self.min_stack.push(value)
            return
        tmp: Any = self.min_stack.pop()
        self.min_stack.push(value)
        self.min_stack.push(tmp)

    def peek(self) -> Any:
        if self.size() == 0:
            return None
        return self.stack[-1]
    
    def min(self) -> Any:
        return self.min_stack.peek()

"""
Задание 6, задача 3: двусторонняя очередь на динамическом массиве. Методы добавления и удаления 
элементов с обоих концов деки - o(1)
"""
class AmortizedDeque:
    def __init__(self) -> None:
        self.capacity: int = 8
        self.storage: DynamicArray = DynamicArray(self.capacity)
        self.start_pointer: int = 0
        self.end_pointer: int = 0
        self.count: int = 0
    
    """
    Сложность алгоритма:
        - временная: o(1)
        - пространственная: O(1)
    """
    def add_front(self, item: Any) -> None:
        self.start_pointer = self._move_left(self.start_pointer)
        self.storage.set_item(self.start_pointer, item)
        self.count += 1
        if self.capacity != self.storage.get_capacity():
            self._reboot_pointers()
    
    """
    Сложность алгоритма:
        - временная: o(1)
        - пространственная: O(1)
    """
    def add_tail(self, item: Any) -> None:
        self.storage.set_item(self.end_pointer, item)
        self.end_pointer = self._move_right(self.end_pointer)
        self.count += 1
        if self.capacity != self.storage.get_capacity():
            self._reboot_pointers()
    
    """
    Сложность алгоритма:
        - временная: o(1)
        - пространственная: O(1)
    """
    def remove_front(self) -> Any | None:
        if self.count == 0:
            return None
        self.start_pointer = self._move_right(self.start_pointer)
        self.count -= 1
        return self.storage.get_item(self._move_left(self.start_pointer))
    
    """
    Сложность алгоритма:
        - временная: o(1)
        - пространственная: O(1)
    """
    def remove_tail(self) -> Any | None:
        if self.count == 0:
            return None
        self.end_pointer = self._move_left(self.end_pointer)
        self.count -= 1
        return self.storage.get_item(self.end_pointer)

    def _move_left(self, pointer: int) -> int:
        return (pointer - 1 + self.storage.get_capacity()) % self.storage.get_capacity()

    def _move_right(self, pointer: int) -> int:
        return (pointer + 1) % self.storage.get_capacity()

    def _reboot_pointers(self) -> None:
        self.capacity = self.storage.get_capacity()
        self.start_pointer = self.capacity - 1
        self.end_pointer = self.count - 1

    def size(self) -> int:
        return self.count

class DynamicArray:
    def __init__(self, init_capacity: int) -> None:
        self.capacity: int = init_capacity
        self.size: int = 0
        self.storage: ctypes.Array[ctypes.py_object] = self._make_array(init_capacity)

    def get_item(self, index: int) -> Any:
        self.size -= 1
        return self.storage[index]

    def set_item(self, index: int, value: Any) -> None:
        if self.size == self.capacity:
            self._resize(index)
            self.storage[self.capacity - 1] = value
            self.size += 1
            return
        self.storage[index] = value
        self.size += 1

    def get_capacity(self) -> int:
        return self.capacity

    def _resize(self, start_pointer: int) -> None:
        new_capacity: int = self.capacity * 2
        new_storage: ctypes.Array[ctypes.py_object] = self._make_array(new_capacity)
        for i in range(self.capacity):
            new_storage[i] = self.storage[(start_pointer + 1 + i) % self.capacity]
        self.storage = new_storage
        self.capacity = new_capacity
        
    def _make_array(self, capacity: int) -> ctypes.Array[ctypes.py_object]:
        return (ctypes.py_object * capacity)() 

"""
Задание 6, задача 6: сбалансирована ли строка из скобок разного типа
Сложность алгоритма:
    - временная: O(N)
    - пространственная: O(N).
"""    
def is_balanced_diff(s: str) -> bool:
    d: dict = {"(": ")", "{": "}", "[": "]"}
    stack: Stack = Stack()
    for ch in s:
        if ch in d:
            stack.push(d.get(ch))
            continue
        if stack.peek() is None or not(stack.peek == ch):
            return False
        stack.pop()    
    return stack.size()
    
class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)
    
    def pop(self) -> Any:
        if self.size() == 0:
            return None
        return self.stack.pop(-1)

    def push(self, value: Any) -> None:
        self.stack.append(value)

    def peek(self) -> Any:
        if self.size() == 0:
            return None
        return self.stack[-1]    
        
 
"""
рефлексия

Задание 4, задача 4-5: сделал всё так, как в рекомендации. Для разных типов скобок использовал 
словарь.

Задание 4, задача 6: интересная мысль, что в стек минимумов нужно добавлять элемент только, если 
стек минимумов пуст или новый элемент <= текущему минимуму. Это позволит немного сэкономить на памяти. 
В своём решении в стеке минимумов я хранил все элементы. 

Задание 4, задача 7: решение совпадает с предложенным. Только забыл учесть деление на 0, когда стек 
пуст.

Задание 4, задача 7: полезное замечание про то, чтобы не полагаться на порядок вычислений, учту в
будущем. Реализовал хранение операций в словаре.
""" 


