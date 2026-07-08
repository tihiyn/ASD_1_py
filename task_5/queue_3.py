from queue import Queue

def test_size() -> None:
    q: Queue = Queue()
    for i in range(-500, 500):
        q.enqueue(i)
    assert 1000 == q.size()    
    
def test_size_if_empty() -> None:
    q: Queue = Queue()
    assert 0 == q.size()
    
def test_enqueue() -> None:
    q: Queue = Queue()
    for i in range(200):
        q.enqueue(i)
    for i in range(199, -1, -1):
        assert i == q.storage[q.size() - 1 - i]
        
def test_enqueue_if_empty() -> None:
    q: Queue = Queue()
    q.enqueue("xyz")
    assert "xyz" == q.storage[0]
    
def test_dequeue() -> None:
    q: Queue = Queue()
    for i in range(1000):
        q.enqueue(i)
    for i in range(1000):
        q.dequeue()
    assert q.size() == 0
    
def test_dequeue_if_empty() -> None:
    q: Queue = Queue()
    assert q.dequeue() is None
    
    
