from typing import Any
from typing import List

class Queue:
    def __init__(self) -> None:
        self.storage: List[Any] = []

    # O(N)
    def enqueue(self, item: Any) -> None:
        self.storage.insert(0, item)
    
    # O(1)
    def dequeue(self) -> Any:
        if self.size() == 0:
            return None
        return self.storage.pop(-1)    

    def size(self) -> int:
        return len(self.storage)



