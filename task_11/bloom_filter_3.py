from bloom_filter import BloomFilter
from typing import List

def test_bloom_filter() -> None:
    bf: BloomFilter = BloomFilter(32)
    bf.add("xyz")
    assert bf.is_value("xyz")
        
def test_bloom_filter_not_value() -> None:
    bf: BloomFilter = BloomFilter(32)
    assert not bf.is_value("wfvedv")
    
def test_bloom_filter_example() -> None:
    s1: str = "0123456789"
    s2: str = "1234567890"
    s3: str = "2345678901"
    s4: str = "3456789012"
    s5: str = "4567890123"
    s6: str = "5678901234"
    s7: str = "6789012345"
    s8: str = "7890123456"
    s9: str = "8901234567"
    s10: str = "9012345678"
    strs: List[str] = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
    bf: BloomFilter = BloomFilter(32)
    for s in strs:
        bf.add(s)
    for s in strs:
        assert bf.is_value(s)    
    
def test_bloom_filter_if_false_positive_error() -> None:
    bf: BloomFilter = BloomFilter(8)
    bf.add("cje")
    assert bf.is_value("wjy")


        