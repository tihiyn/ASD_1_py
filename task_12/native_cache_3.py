from native_cache import NativeCache

def test_put_if_empty() -> None:
    c: NativeCache = NativeCache(7)
    c.put("abc", 123)
    assert 123 == c.get("abc")
    
def test_put() -> None:
    c: NativeCache = NativeCache(7)
    c.put("abc", 123)
    c.put("xyz", 456)
    assert 456 == c.get("xyz")
    
def test_put_if_full() -> None:
    c: NativeCache = NativeCache(5)
    c.put("a", 1)
    c.get("a")
    c.put("b", 2)
    c.get("b")
    c.put("c", 3)
    c.put("d", 4)
    c.get("d")
    c.put("e", 5)
    c.get("e")
    c.put("f", 6)
    assert 6 == c.get("f")
    assert c.get("c") is None
    
def test_get_if_empty() -> None:
    c: NativeCache = NativeCache(5)
    assert c.get("ewbefv") is None
    
def test_get() -> None:
    c: NativeCache = NativeCache(5)
    c.put("a", "fff")
    assert "fff" == c.get("a")
    assert 1 == c.hits[2]
    
def test_get_if_many_hits() -> None:
    c: NativeCache = NativeCache(5)
    c.put("a", "fff")
    for _ in range(10):
        c.get("a")
    assert 10 == c.hits[2]
    
def test_get_if_not_exists() -> None:
    c: NativeCache = NativeCache(5)
    c.put("a", "fff")
    assert c.get("b") is None
    
def test_get_if_full() -> None:
    c: NativeCache = NativeCache(5)
    c.put("a", 1)
    c.put("b", 2)
    c.put("c", 3)
    c.put("d", 4)
    c.put("e", 5)
    assert 2 == c.get("b")
    assert 1 == c.hits[3]
    
def test_remove_if_empty() -> None:
    c: NativeCache = NativeCache(5)
    assert not c.remove("a")
    
def test_remove() -> None:
    c: NativeCache = NativeCache(5)
    c.put("a", 123)
    assert c.remove("a")
    assert c.get("a") is None
    
def test_remove_if_not_exists() -> None:
    c: NativeCache = NativeCache(5)
    c.put("a", 123)
    assert not c.remove("b")   
    
def test_remove_and_reset_hits() -> None:
    c: NativeCache = NativeCache(5)
    c.put("a", 123)
    for _ in range(10):
        c.get("a")
    assert 10 == c.hits[2]
    assert c.remove("a")
    assert 0 == c.hits[2]
    
def test_remove_if_full() -> None:
    c: NativeCache = NativeCache(5)
    c.put("a", 1)
    c.put("b", 2)
    c.put("c", 3)
    c.put("d", 4)
    c.put("e", 5)
    assert c.remove("b")
    assert 0 == c.hits[3]    


    