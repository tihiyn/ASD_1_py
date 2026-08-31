from typing import Optional
from typing import Any

class NativeCache:
    def __init__(self, sz: int) -> None:
        self.size: int = sz
        self.count: int = 0
        self.step: int = 3
        self.slots: list[Optional[str]] = [None] * self.size
        self.values: list[Optional[Any]] = [None] * self.size
        self.hits: list[int] = [0] * self.size
    
    def hash_fun(self, key: str) -> int:
        h: int = 0
        for ch in key:
            h = (h * 31 + ord(ch)) % (10**9 + 7)
        return h % self.size
    
    def put(self, key: str, value: Optional[Any]) -> None:
        if self.count == self.size:
            min_idx = min(range(self.size), key = lambda i: self.hits[i])
            self.slots[min_idx] = None
            self.values[min_idx] = None
            self.hits[min_idx] = 0
            self.count -= 1
        idx: int = self.hash_fun(key)
        for _ in range(self.size):
            if self.slots[idx] is None:
                self.slots[idx] = key
                self.values[idx] = value
                self.count += 1
                return
            idx = (idx + self.step) % self.size
    
    def get(self, key: str) -> Optional[Any]:
        idx: int = self.hash_fun(key)
        for _ in range(self.size):
            if self.slots[idx] == key:
                self.hits[idx] += 1
                return self.values[idx]
            idx = (idx + self.step) % self.size
        return None    
        
    def remove(self, key: str) -> bool:
        idx: int = self.hash_fun(key)
        for _ in range(self.size):
            if self.slots[idx] == key:
                self.slots[idx] = None
                self.values[idx] = None
                self.hits[idx] = 0
                return True
            idx = (idx + self.step) % self.size
        return False
        

        