from typing import Any
from typing import List

class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)
    
    """
    В худшем случае - O(N) (если будет сжатие массива),
    амортизированное время - O(1)
    """
    def pop(self) -> Any:
        if self.size() == 0:
            return None
        return self.stack.pop(-1)

    """
    В худшем случае - O(N) (если будет расширение массива),
    амортизированное время - O(1)
    """
    def push(self, value: Any) -> None:
        self.stack.append(value)

    def peek(self) -> Any:
        if self.size() == 0:
            return None
        return self.stack[-1]



