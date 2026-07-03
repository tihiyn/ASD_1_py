from stack import Stack
from typing import Any
from typing import List

"""
Задание 4, задача 2: реализация стека, которая работает с головой списка как с вершиной стека
"""
class StackReverse:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)
    
    def pop(self) -> Any:
        if self.size() == 0:
            return None
        return self.stack.pop(0)

    def push(self, value: Any) -> None:
        self.stack.insert(0, value)

    def peek(self) -> Any:
        if self.size() == 0:
            return None
        return self.stack[0]

"""
Задание 4, задача 3: что выведет код

Если стек пуст -> ничего не будет напечатано.
Если в стеке нечётное кол-во элементов -> все элементы стека и None
Если в стеке чётное кол-во элментов -> все элементы стека
"""
       
"""
Задание 4, задача 4: оценить меру сложности операций push и pop из задачи 2

push - O(N), pop - O(N)
"""      

"""
Задание 4, задача 5: сбалансирована ли строка из скобок
Сложность алгоритма:
    - временная: O(N)
    - пространственная: O(N).
"""
def is_balanced(s: str) -> bool:
    stack: Stack = Stack()
    for ch in s:
        if ch == '(':
            stack.push(ch)
            continue
        br: str = stack.pop()
        if br is None:
            return False
    return stack.size() == 0
    
"""
Задание 4, задача 6: сбалансирована ли строка из скобок разного типа
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
    
"""
Задание 4, задача 7: минимальный элемент стека за O(1)
Сложность метода min:
    - временная: O(1)
    - пространственная: O(1).
"""
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
Задание 4, задача 8: среднее значение элементов стека за O(1)
Сложность метода avg:
    - временная: O(1)
    - пространственная: O(1).
"""
class StackAvg:
    def __init__(self) -> None:
        self.stack: List[int | float] = []
        self.sum: int | float = 0

    def size(self) -> int:
        return len(self.stack)
    
    def pop(self) -> int | float | None:
        if self.size() == 0:
            return None
        res: int | float = self.stack.pop(-1)
        self.sum -= res
        return res

    def push(self, value: int | float) -> None:
        self.stack.append(value)
        self.sum += value

    def peek(self) -> int | float | None:
        if self.size() == 0:
            return None
        return self.stack[-1]
    
    def avg(self) -> float:
        return self.sum / self.size()   

"""
Задание 4, задача 9: сложение и умножение в постфиксной записи
Сложность алгоритма:
    - временная: O(N)
    - пространственная: O(N).
"""  
def calc_postfix(stack: Stack) -> int:
    d: dict = {"+": lambda a, b: a + b, "*": lambda a, b: a * b}
    operands: Stack = Stack()
    while stack.size() > 0:
        x: str | int = stack.pop()
        if x in d:
            operands.push(d[x](operands.pop(), operands.pop()))
            continue
        operands.push(x)
    return operands.pop()    
    
    
"""
рефлексия

Задание 2, задача 9:
Интересное решение! Я менял местами значения узлов, а тут меняем связи. Этот вариант даже эффективнее
моего, так как в моём решении нужно знать длину списка, а в текущей реализации эта операция стоит O(N).

Задание 2, задача 10:
Мне тоже такое решение первым пришло в голову, но мне кажется, что оно неверно по следующим причинам:
    - чтобы узнать длину списка, нужно пройтись по всему списку. Если в нём есть циклы, то метод 
    никогда не завершиться. Эту проблему можно решить, храня отдельное поле с размером, но тогда
    придётся изменить реализацию некоторых методов класса;
    - циклы могут быть не только в прямом направлении, но и в обратном.

Задание 2, задача 11:
Как раз и реализовал сортировку пузырьком. Радует, что написал её по памяти.

Задание 2, задача 12:
Всё сделал правильно. Про обобщённый вариант помнил с прошлого курса, но не стал здесь усложнять,
так как задание этого не требовало.

Задание 2, задача 13:
Реализовать проблем не составило. Но вспоминая курс по ООАП-2, проверять тип полиморфного объекта - 
ну такое) Лучше, конечно, чем флажок. С другой стороны, а как тут по-другому...
"""


