from stack import Stack

#4.1
def test_size() -> None:
    s: Stack = Stack()
    for i in range(100):
        s.push(i)
    assert 100 == s.size()
    
def test_size_if_empty() -> None:
    s: Stack = Stack()
    assert 0 == s.size()
    
def test_push_if_empty() -> None:
    s: Stack = Stack()
    s.push("xyz")
    assert "xyz" == s.stack[0]
    
def test_push() -> None:
    s: Stack = Stack()
    for i in range(1500):
        s.push(i)
    for i in range(1500):
        assert i == s.stack[i]
        
def test_pop() -> None:
    s: Stack = Stack()
    s.push(-1)
    s.push(0)
    s.push(1)
    assert 1 == s.pop()
    assert 2 == s.size()
    
def test_pop_if_empty() -> None:
    s: Stack = Stack()
    assert s.pop() is None
    
def test_peek() -> None:
    s: Stack = Stack()
    s.push("x")
    s.push("y")
    s.push("z")
    assert "z" == s.peek()
    assert 3 == s.size()
    
def test_peek_if_empty() -> None:
    s: Stack = Stack()
    assert s.peek() is None 
    
    
