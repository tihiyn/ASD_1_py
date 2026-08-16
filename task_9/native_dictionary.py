from typing import Any
from typing import Optional

class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.step = 3
        self.slots = [None] * self.size
        self.values = [None] * self.size

    def hash_fun(self, key: str) -> int:
        h: int = 0
        for ch in key:
            h = (h * 31 + ord(ch)) % (10**9 + 7)
        return h % self.size

    def is_key(self, key: str) -> bool:
        idx: int = self.hash_fun(key)
        for _ in range(self.size):
            if self.slots[idx] is None:
                return False
            if self.slots[idx] == key:
                return True
            idx = (idx + self.step) % self.size    
        return False        

    def put(self, key: str, value: Optional[Any]) -> None:
        idx: int = self.hash_fun(key)
        for _ in range(self.size):
            if self.slots[idx] is None:
                self.slots[idx] = key
                self.values[idx] = value
                return
            if self.slots[idx] == key:
                self.values[idx] = value
                return
            idx = (idx + self.step) % self.size
        self.slots[idx] = key
        self.values[idx] = value    
        

    def get(self, key: str) -> Optional[Any]:
        idx: int = self.hash_fun(key)
        for _ in range(self.size):
            if self.slots[idx] is None:
                return None
            if self.slots[idx] == key:
                return self.values[idx]
            idx = (idx + self.step) % self.size    
        return None
        
    
    