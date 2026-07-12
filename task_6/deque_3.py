from deque import Deque

def test_add_front_if_empty() -> None:
    d: Deque = Deque()
    d.addFront('g')
    assert 1 == d.size()
    assert 'g' == d.storage[0]
    
def test_add_front() -> None:
    d: Deque = Deque()
    for i in range(10000):
        d.addFront(i)
    assert 10000 == d.size()
    for i in range(10000):
        assert i == d.storage[d.size() - i - 1]
        
def test_add_tail_if_empty() -> None:
    d: Deque = Deque()
    d.addTail("abc")
    assert 1 == d.size()
    assert "abc" == d.storage[0]
    
def test_add_tail() -> None:
    d: Deque = Deque()
    for i in range(77777):
        d.addTail(i)
    assert 77777 == d.size()
    for i in range(77777):
        assert i == d.storage[i]    

def test_remove_front_if_empty() -> None:
    d: Deque = Deque()
    assert d.removeFront() is None
    assert 0 == d.size()
        
def test_remove_front() -> None:
    d: Deque = Deque()
    for i in range(10000):
        d.addFront(i)
    assert 10000 == d.size()
    for i in range(9999, -1, -1):
        assert i == d.removeFront()
        
def test_remove_tail_if_empty() -> None:
    d: Deque = Deque()
    assert d.removeTail() is None
    assert 0 == d.size()
    
def test_remove_tail() -> None:
    d: Deque = Deque()
    for i in range(10000):
        d.addTail(i)
    assert 10000 == d.size()
    for i in range(9999, -1, -1):
        assert i == d.removeTail()
        

        