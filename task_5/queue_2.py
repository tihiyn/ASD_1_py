from queue import Queue
from typing import Any
from typing import List

"""
Задание 5, задача 2: оценить меру сложности для операций enqueue() и dequeue()

enqueue():
    - временная сложность O(N)
    - пространственная сложность O(1)
dequeue():
    - временная сложность O(1)
    - пространственная сложность O(1)   
"""

"""
Задание 5, задача 3: вращение очереди на N элементов

Сложность алгоритма:
    - временная: O(N)
    - пространственная: O(1)
"""
def cycle(q: Queue, N: int) -> None:
    if q.size() == 0:
        return None
    for i in range(N):
        q.enqueue(q.dequeue())
        
"""
Задание 5, задача 4: очередь на 2 стеках
"""
class QueueDoubleStack:
    def __init__(self) -> None:
        self.enq_st: Stack = Stack()
        self.deq_st: Stack = Stack()
        self.len: int = 0
    
    """
    Сложность алгоритма:
        - временная: O(N)
        - пространственная: O(1)
    """
    def enqueue(self, item: Any) -> None:
        if self.enq_st.size() == 0 and self.deq_st.size() > 0:
            for i in range(self.len):
                self.enq_st.push(self.deq_st.pop())
        self.enq_st.push(item)
        self.len += 1
        
    """
    Сложность алгоритма:
        - временная: O(N)
        - пространственная: O(1)
    """
    def dequeue(self) -> Any:
        if self.size() == 0:
            return None
        if self.deq_st.size() == 0:
            for i in range(self.len):
                self.deq_st.push(self.enq_st.pop())
        self.len -= 1
        return self.deq_st.pop()

    """
    Сложность алгоритма:
        - временная: O(1)
        - пространственная: O(1)
    """
    def size(self) -> int:
        return self.len
        
class Stack:
    def __init__(self) -> None:
        self.stack: List[Any] = []

    def size(self) -> int:
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
Задание 5, задача 5: поменять порядок элементов в очереди на обратный

Сложность алгоритма:
    - временная: O(N)
    - пространственная: O(N)
"""
def reverse(q: Queue) -> None:
    s: Stack = Stack()
    for i in range(q.size()):
        s.push(q.dequeue())
    for i in range(s.size()):
        q.enqueue(s.pop())

"""
Задание 5, задача 6: круговая очередь
"""
class CycleQueue:
    def __init__(self, capacity: int) -> None:
        self.storage: List[Any] = []
        self.start: int = 0
        self.finish: int = 0
        self.capacity: int = capacity
    
    """
    Сложность алгоритма:
        - временная: O(1)
        - пространственная: O(1)
    """
    def enqueue(self, item: Any) -> None:
        if self.is_full():
            return
        self.storage.insert(self.start, item)
        self.start = (self.start - 1 + self.capacity) % self.capacity
    
    """
    Сложность алгоритма:
        - временная: O(1)
        - пространственная: O(1)
    """
    def dequeue(self) -> Any:
        if len(self.storage) == 0:
            return None
        res: Any = self.storage.pop(self.finish)
        self.finish = (self.finish - 1 + self.capacity) % self.capacity
        return res
    
    """
    Сложность алгоритма:
        - временная: O(1)
        - пространственная: O(1)
    """
    def is_full(self) -> bool:
        return self.start == self.finish and len(self.storage) > 0
        
"""
рефлексия

Задание 3, задача 6: интересная задача, правда реализовал логику с балансом только для метода 
append(), а про метод delete() забыл. А так, идея понятна.

Задание 3, задача 7: про представление многомерного массива в виде плоского догадался (а когда 
проходил курс первый раз, нет). Просто добавление реализовать было не сложно. Но вот реализовать 
динмическое расширение... Ведь увеличиватся должны все массивы в соответствующей плоскости. Не уверен,
что мой код работает кооректно, да и с оценкой сложности были проблемы.
"""



        