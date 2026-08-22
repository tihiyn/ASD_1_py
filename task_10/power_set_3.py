from power_set import PowerSet
import time


def test_put() -> None:
    s: PowerSet = PowerSet()
    s.d = {1: None, 2: None}
    s.put(3)
    assert s.get(3)
    
def test_put_if_exists() -> None:
    s: PowerSet = PowerSet()
    s.d = {1: None, 2: None}
    s.put(2)
    assert s.get(2)
    
def test_put_if_empty() -> None:
    s: PowerSet = PowerSet()
    s.put("a")
    assert s.get("a")
    
def test_put_performance() -> None:
    s: PowerSet = PowerSet()
    start: float = time.perf_counter()
    for i in range(50000):
        s.put(i)
    end: float = time.perf_counter()
    assert end - start < 2
    

def test_remove() -> None:
    s: PowerSet = PowerSet()
    s.d = {1: None, 2: None}
    assert s.remove(1)
    assert not s.get(1)
    
def test_remove_if_not_exists() -> None:
    s: PowerSet = PowerSet()
    s.d = {1: None, 2: None}
    assert not s.remove(3) 
    
def test_remove_if_empty() -> None:
    s: PowerSet = PowerSet()
    assert not s.remove(5.25) 
    
def test_remove_performance() -> None:
    s: PowerSet = PowerSet()
    for i in range(30000):
        s.put(i)
    start: float = time.perf_counter()
    for i in range(50000):
        s.remove(i)    
    end: float = time.perf_counter()
    assert end - start < 2   
    
    
def test_get() -> None:
    s: PowerSet = PowerSet()
    s.d = {1: None, 2: None}
    assert s.get(1)
    
def test_get_if_not_exists() -> None:
    s: PowerSet = PowerSet()
    s.d = {1: None, 2: None}
    assert not s.get(3) 
    
def test_get_if_empty() -> None:
    s: PowerSet = PowerSet()
    assert not s.get(5.25) 
    
def test_get_performance() -> None:
    s: PowerSet = PowerSet()
    for i in range(30000):
        s.put(i)
    start: float = time.perf_counter()
    for i in range(50000):
        s.get(i)    
    end: float = time.perf_counter()
    assert end - start < 2      
    
    
def test_intersection() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(2)
    s2.put(3)
    s2.put(4)
    
    exp: PowerSet = PowerSet()
    exp.put(2)
    exp.put(3)
    act: PowerSet = s1.intersection(s2)
    assert exp.equals(act)
    
def test_intersection_if_not_inetrsect() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(4)
    s2.put(5)
    s2.put(6)

    res: PowerSet = s1.intersection(s2)
    assert res.size() == 0    
    
def test_intersection_if_subset() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(2)
    s2.put(3)
    
    res: PowerSet = s1.intersection(s2)
    assert s2.equals(res)    
    
def test_intersection_if_equals() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(1)
    s2.put(2)
    s2.put(3)
    
    res: PowerSet = s1.intersection(s2)
    assert s1.equals(res)   
    assert s2.equals(res)   
    
def test_intersection_if_left_empty() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s2.put(1)
    s2.put(2)
    s2.put(3)
    
    res: PowerSet = s1.intersection(s2)
    assert res.size() == 0    
    
def test_intersection_if_right_empty() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    
    res: PowerSet = s1.intersection(s2)
    assert res.size() == 0    
    
def test_intersection_performance() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    for i in range(20000):
        s1.put(i)
    for i in range(30000):
        s2.put(i)    

    start: float = time.perf_counter()
    act: PowerSet = s1.intersection(s2)
    end: float = time.perf_counter()    
    assert end - start < 2   
    
    
def test_union() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(2)
    s2.put(3)
    s2.put(4)
    
    exp: PowerSet = PowerSet()
    exp.put(1)
    exp.put(2)
    exp.put(3)
    exp.put(4)
    act: PowerSet = s1.union(s2)
    assert exp.equals(act)
    
def test_union_if_not_inetrsect() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(4)
    s2.put(5)
    s2.put(6)

    exp: PowerSet = PowerSet()
    exp.put(1)
    exp.put(2)
    exp.put(3)
    exp.put(4)
    exp.put(5)
    exp.put(6)
    act: PowerSet = s1.union(s2)
    assert exp.equals(act)    
    
def test_union_if_subset() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(2)
    s2.put(3)
    
    res: PowerSet = s1.union(s2)
    assert s1.equals(res)    
    
def test_union_if_equals() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(1)
    s2.put(2)
    s2.put(3)
    
    res: PowerSet = s1.union(s2)
    assert s1.equals(res)   
    assert s2.equals(res)   
    
def test_union_if_left_empty() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s2.put(1)
    s2.put(2)
    s2.put(3)
    
    res: PowerSet = s1.union(s2)
    assert s2.equals(res)   
    
def test_union_if_right_empty() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    
    res: PowerSet = s1.union(s2)
    assert s1.equals(res)  

def test_union_performance() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    for i in range(20000):
        s1.put(i)
    for i in range(30000):
        s2.put(i)    

    start: float = time.perf_counter()
    act: PowerSet = s1.union(s2)
    end: float = time.perf_counter()    
    assert end - start < 2  
    
    
def test_difference() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(2)
    s2.put(3)
    s2.put(4)
    
    exp: PowerSet = PowerSet()
    exp.put(1)
    act: PowerSet = s1.difference(s2)
    assert exp.equals(act)
    
def test_difference_if_not_inetrsect() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(4)
    s2.put(5)
    s2.put(6)

    exp: PowerSet = PowerSet()
    exp.put(1)
    exp.put(2)
    exp.put(3)
    act: PowerSet = s1.difference(s2)
    assert exp.equals(act)    
    
def test_difference_if_subset() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(2)
    s2.put(3)
    
    exp: PowerSet = PowerSet()
    exp.put(1)
    act: PowerSet = s1.difference(s2)
    assert exp.equals(act)    
    
def test_difference_if_equals() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(1)
    s2.put(2)
    s2.put(3)
    
    res: PowerSet = s1.difference(s2)
    assert res.size() == 0  
    
def test_difference_if_left_empty() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s2.put(1)
    s2.put(2)
    s2.put(3)
    
    res: PowerSet = s1.difference(s2)
    assert res.size() == 0    
    
def test_difference_if_right_empty() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    
    res: PowerSet = s1.difference(s2)
    assert s1.equals(res)
    
def test_differrence_performance() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    for i in range(20000):
        s1.put(i)
    for i in range(30000):
        s2.put(i)    

    start: float = time.perf_counter()
    act: PowerSet = s1.difference(s2)
    end: float = time.perf_counter()    
    assert end - start < 2      
    
    
def test_issubset_if_intersect() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(2)
    s2.put(3)
    s2.put(4)
    
    assert not s1.issubset(s2)
    
def test_issubset_if_not_inetrsect() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(4)
    s2.put(5)
    s2.put(6)

    assert not s1.issubset(s2)   
    
def test_issubset_if_subset() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(2)
    s2.put(3)
    
    assert s1.issubset(s2)   
    
def test_issubset_if_equals() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(1)
    s2.put(2)
    s2.put(3)
    
    assert s1.issubset(s2)
    
def test_issubset_if_left_empty() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s2.put(1)
    s2.put(2)
    s2.put(3)
    
    assert not s1.issubset(s2)  
    
def test_issubset_if_right_empty() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    
    assert s1.issubset(s2)
    
def test_issubset_performance() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    for i in range(70000):
        s1.put(i)
    for i in range(50000):
        s2.put(i)    

    start: float = time.perf_counter()
    s1.issubset(s2)
    end: float = time.perf_counter()    
    assert end - start < 2      
    
    
def test_equals_if_intersect() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(2)
    s2.put(3)
    s2.put(4)
    
    assert not s1.equals(s2)
    
def test_equals_if_not_inetrsect() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(4)
    s2.put(5)
    s2.put(6)

    assert not s1.equals(s2)   
    
def test_equals_if_subset() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(2)
    s2.put(3)
    
    assert not s1.equals(s2)   
    
def test_equals_if_equals() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    s2.put(1)
    s2.put(2)
    s2.put(3)
    
    assert s1.equals(s2)
    
def test_equals_if_left_empty() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s2.put(1)
    s2.put(2)
    s2.put(3)
    
    assert not s1.equals(s2)  
    
def test_equals_if_right_empty() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    s1.put(1)
    s1.put(2)
    s1.put(3)
    
    assert not s1.equals(s2)
    
def test_equals_performance() -> None:
    s1: PowerSet = PowerSet()
    s2: PowerSet = PowerSet()
    for i in range(50000):
        s1.put(i)
    for i in range(50000):
        s2.put(i)    

    start: float = time.perf_counter()
    s1.equals(s2)
    end: float = time.perf_counter()    
    assert end - start < 2      
        
    
    