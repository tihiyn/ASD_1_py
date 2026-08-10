class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value: str) -> int:
        h: int = 0
        for ch in value:
            h = (h * 31 + ord(ch)) % (10**9 + 7)
        return h % self.size

    def seek_slot(self, value: str) -> int | None:
        idx: int = self.hash_fun(value)
        for _ in range(self.size):
            if self.slots[idx] is None or self.slots[idx] == value:
                return idx
            idx = (idx + self.step) % self.size
        return None

    def put(self, value: str) -> int | None:
        idx: int | None = self.seek_slot(value)
        if idx is None:
            return None
        self.slots[idx] = value
        return idx

    def find(self, value: str) -> int | None:
        idx: int = self.hash_fun(value)
        for _ in range(self.size):
            if self.slots[idx] is None:
                return None
            if self.slots[idx] == value:
                return idx
            idx = (idx + self.step) % self.size  
        return None
        

        