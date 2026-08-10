from hash_table import HashTable
from typing import List

def test_hash_fun() -> None:
    h: HashTable = HashTable(19, 3)
    assert 2 == h.hash_fun("a")

def test_hash_fun_if_empty_string() -> None:
    h: HashTable = HashTable(19, 3)
    assert 0 == h.hash_fun("")

def test_hash_fun_in_range() -> None:
    h: HashTable = HashTable(19, 3)
    for i in range(10000):
        idx: int = h.hash_fun(str(i))
        assert 0 <= idx
        assert idx < 19

def test_hash_fun_is_deterministic() -> None:
    h: HashTable = HashTable(19, 3)
    assert h.hash_fun("abcdef") == h.hash_fun("abc" + "def")
    assert h.hash_fun("abcdef") == h.hash_fun("abcdef")

def test_hash_fun_if_single_slot() -> None:
    h: HashTable = HashTable(1, 1)
    assert 0 == h.hash_fun("a")
    assert 0 == h.hash_fun("abc")
    assert 0 == h.hash_fun("")

def test_hash_fun_if_permutation() -> None:
    h: HashTable = HashTable(19, 3)
    assert 8 == h.hash_fun("ab")
    assert 0 == h.hash_fun("ba")

def test_seek_slot_if_empty() -> None:
    h: HashTable = HashTable(19, 3)
    assert 8 == h.seek_slot("g")
    assert 2 == h.seek_slot("a")

def test_seek_slot_if_exists() -> None:
    h: HashTable = HashTable(19, 3)
    h.put("g")
    h.put("z")
    assert 8 == h.seek_slot("g")
    assert 11 == h.seek_slot("z")

def test_seek_slot_with_collision() -> None:
    h: HashTable = HashTable(19, 3)
    h.put("g")
    assert 11 == h.seek_slot("z")
    h.put("z")
    assert 14 == h.seek_slot("ab")

def test_seek_slot_with_wrap_around() -> None:
    h: HashTable = HashTable(19, 3)
    h.put("p")
    assert 1 == h.seek_slot("ak")

def test_seek_slot_if_full() -> None:
    h: HashTable = HashTable(3, 1)
    h.put("a")
    h.put("b")
    h.put("c")
    assert h.seek_slot("d") is None

def test_seek_slot_if_full_and_exists() -> None:
    h: HashTable = HashTable(3, 1)
    h.put("a")
    h.put("b")
    h.put("c")
    assert 1 == h.seek_slot("a")
    assert 2 == h.seek_slot("b")
    assert 0 == h.seek_slot("c")

def test_seek_slot_if_step_not_coprime() -> None:
    h: HashTable = HashTable(4, 2)
    h.put("d")
    h.put("h")
    assert h.seek_slot("l") is None
    assert h.slots[1] is None
    assert h.slots[3] is None

def test_seek_slot_does_not_modify_slots() -> None:
    h: HashTable = HashTable(19, 3)
    h.put("g")
    h.seek_slot("z")
    assert "g" == h.slots[8]
    assert 18 == h.slots.count(None)

def test_put_if_empty() -> None:
    h: HashTable = HashTable(19, 3)
    assert 2 == h.put("a")
    assert "a" == h.slots[2]
    assert 18 == h.slots.count(None)

def test_put_with_collision() -> None:
    h: HashTable = HashTable(19, 3)
    assert 8 == h.put("g")
    assert 11 == h.put("z")
    assert 14 == h.put("ab")
    assert "g" == h.slots[8]
    assert "z" == h.slots[11]
    assert "ab" == h.slots[14]

def test_put_duplicate() -> None:
    h: HashTable = HashTable(19, 3)
    assert 8 == h.put("g")
    assert 8 == h.put("g")
    assert 1 == h.slots.count("g")
    assert 18 == h.slots.count(None)

def test_put_if_full() -> None:
    h: HashTable = HashTable(3, 1)
    h.put("a")
    h.put("b")
    h.put("c")
    assert h.put("d") is None
    assert "c" == h.slots[0]
    assert "a" == h.slots[1]
    assert "b" == h.slots[2]

def test_put_with_wrap_around() -> None:
    h: HashTable = HashTable(19, 3)
    assert 17 == h.put("p")
    assert 1 == h.put("ak")
    assert "p" == h.slots[17]
    assert "ak" == h.slots[1]

def test_put_many() -> None:
    h: HashTable = HashTable(1000, 1)
    indexes: List[int] = []
    idx: int | None = None
    for i in range(1000):
        idx = h.put(str(i))
        if idx is not None:
            indexes.append(idx)
    assert 1000 == len(set(indexes))
    assert 0 == h.slots.count(None)

def test_find() -> None:
    h: HashTable = HashTable(19, 3)
    h.put("a")
    h.put("hello")
    assert 2 == h.find("a")
    assert 11 == h.find("hello")

def test_find_if_empty() -> None:
    h: HashTable = HashTable(19, 3)
    assert h.find("a") is None

def test_find_if_not_exist() -> None:
    h: HashTable = HashTable(19, 3)
    h.put("a")
    h.put("hello")
    assert h.find("b") is None
    assert h.find("Hello") is None

def test_find_with_collision() -> None:
    h: HashTable = HashTable(19, 3)
    h.put("g")
    h.put("z")
    h.put("ab")
    assert 8 == h.find("g")
    assert 11 == h.find("z")
    assert 14 == h.find("ab")

def test_find_if_full_and_not_exist() -> None:
    h: HashTable = HashTable(3, 1)
    h.put("a")
    h.put("b")
    h.put("c")
    assert h.find("d") is None

def test_find_after_many_puts() -> None:
    h: HashTable = HashTable(1000, 1)
    indexes: List[int] = []
    idx: int | None = None
    for i in range(1000):
        idx = h.put(str(i))
        if idx is not None:
            indexes.append(idx)
    for i in range(1000):
        assert indexes[i] == h.find(str(i))

