class BloomFilter:
    def __init__(self, f_len: int) -> None:
        self.filter_len: int = f_len
        self.filter: int = 0

    def hash1(self, str1: str) -> int:
        h: int = 0
        for c in str1:
            code: int = ord(c)
            h = h * 17 + code
        return h % self.filter_len

    def hash2(self, str1: str) -> int:
        h: int = 0
        for c in str1:
            code: int = ord(c)
            h = h * 223 + code
        return h % self.filter_len

    def add(self, str1: str) -> None:
        h1: int = self.hash1(str1)
        h2: int = self.hash2(str1)
        self.filter = self.filter | 2 ** h1
        self.filter = self.filter | 2 ** h2

    def is_value(self, str1: str) -> bool:
        h1: int = self.hash1(str1)
        h2: int = self.hash2(str1)
        return (2 ** h1 & self.filter != 0) and (2 ** h2 & self.filter != 0)
        
          