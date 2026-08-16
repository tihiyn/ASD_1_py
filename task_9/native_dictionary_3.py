from native_dictionary import NativeDictionary

def test_put() -> None:
    d: NativeDictionary = NativeDictionary(19)
    d.put("a", 1)
    d.put("abc", "xyz")
    assert 1 == d.get("a")
    assert "xyz" == d.get("abc")
    
def test_put_if_empty() -> None:
    d: NativeDictionary = NativeDictionary(19)
    d.put("a", 1)
    assert "a" == d.slots[2]
    assert 1 == d.values[2]

def test_put_if_key_exist() -> None:
    d: NativeDictionary = NativeDictionary(19)
    d.put("a", 1)
    d.put("a", 2)
    assert 2 == d.get("a")
    assert "a" == d.slots[2]
    assert 2 == d.values[2]

def test_put_if_collision() -> None:
    d: NativeDictionary = NativeDictionary(19)
    d.put("g", "G")
    d.put("z", "Z")
    assert "g" == d.slots[8]
    assert "G" == d.values[8]
    assert "z" == d.slots[11]
    assert "Z" == d.values[11]

def test_put_if_key_exist_and_collision() -> None:
    d: NativeDictionary = NativeDictionary(19)
    d.put("g", "G")
    d.put("z", "Z")
    d.put("z", "zzz")
    assert "zzz" == d.get("z")
    assert "zzz" == d.values[11]
    assert "G" == d.get("g")

def test_put_none_value() -> None:
    d: NativeDictionary = NativeDictionary(19)
    d.put("a", None)
    assert "a" == d.slots[2]
    assert d.values[2] is None

def test_put_if_empty_key() -> None:
    d: NativeDictionary = NativeDictionary(19)
    d.put("", "empty")
    assert "" == d.slots[0]
    assert "empty" == d.values[0]

def test_put_if_full() -> None:
    d: NativeDictionary = NativeDictionary(19)
    for i in range(19):
        d.put(str(i), i)
    d.put("zzz", 99)
    assert "zzz" == d.slots[2]
    assert 99 == d.values[2]


def test_is_key_if_empty() -> None:
    d: NativeDictionary = NativeDictionary(19)
    assert d.is_key("a") is False

def test_is_key_if_exists() -> None:
    d: NativeDictionary = NativeDictionary(19)
    d.put("a", 1)
    assert d.is_key("a") is True

def test_is_key_if_not_exist() -> None:
    d: NativeDictionary = NativeDictionary(19)
    d.put("a", 1)
    assert d.is_key("b") is False

def test_is_key_if_collision() -> None:
    d: NativeDictionary = NativeDictionary(19)
    d.put("g", "G")
    d.put("z", "Z")
    assert d.is_key("g") is True
    assert d.is_key("z") is True

def test_is_key_if_full_and_not_exist() -> None:
    d: NativeDictionary = NativeDictionary(19)
    for i in range(19):
        d.put(str(i), i)
    assert d.is_key("zzz") is False

def test_is_key_after_put_existing_key() -> None:
    d: NativeDictionary = NativeDictionary(19)
    d.put("a", 1)
    d.put("a", 2)
    assert d.is_key("a") is True


def test_get_if_empty() -> None:
    d: NativeDictionary = NativeDictionary(19)
    assert d.get("a") is None

def test_get_if_exists() -> None:
    d: NativeDictionary = NativeDictionary(19)
    d.put("a", 1)
    assert 1 == d.get("a")

def test_get_if_not_exist() -> None:
    d: NativeDictionary = NativeDictionary(19)
    d.put("a", 1)
    assert d.get("b") is None

def test_get_if_collision() -> None:
    d: NativeDictionary = NativeDictionary(19)
    d.put("g", "G")
    d.put("z", "Z")
    assert "G" == d.get("g")
    assert "Z" == d.get("z")

def test_get_after_put_existing_key() -> None:
    d: NativeDictionary = NativeDictionary(19)
    d.put("a", 1)
    assert 1 == d.get("a")
    d.put("a", 2)
    assert 2 == d.get("a")

def test_get_if_full_and_not_exist() -> None:
    d: NativeDictionary = NativeDictionary(19)
    for i in range(19):
        d.put(str(i), i)
    assert d.get("zzz") is None

def test_get_if_none_value() -> None:
    d: NativeDictionary = NativeDictionary(19)
    d.put("a", None)
    assert d.get("a") is None



