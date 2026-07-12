from typing import Any

class Deque:
    def __init__(self):
        self.storage = []

    # Временная сложность - O(N), так как необходимо сдвигать все элементы массива
    def addFront(self, item: Any) -> None:
        self.storage.insert(0, item)
    
    # Временная сложность - o(1), так как это добавление элемента в конец массива
    def addTail(self, item: Any) -> None:
        self.storage.append(item)
    
    # Временная сложность - O(N), так как необходимо сдвигать все элементы массива
    def removeFront(self) -> Any | None:
        if self.size() == 0:
            return None
        return self.storage.pop(0)

    # Временная сложность - o(1), так как это удаление элемента из конца массива
    def removeTail(self) -> Any | None:
        if self.size() == 0:
            return None
        return self.storage.pop(-1)    

    def size(self) -> int:
        return len(self.storage)



        