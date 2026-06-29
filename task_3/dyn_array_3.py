from dyn_array import DynArray
import pytest

#1.1
def test_insert() -> None:
    a: DynArray = DynArray()
    a.append('a')
    a.append('b')
    a.append('d')
    a.append('e')
    a.append('f')
    
    a.insert(2, 'c')
    assert 'c' == a.__getitem__(2)
    assert 6 == a.__len__()
    assert 16 == a.capacity
    
def test_insert_first() -> None:
    a: DynArray = DynArray()
    a.append(2)
    a.append(3)
    a.append(4)
    
    a.insert(0, 1)
    assert 1 == a.__getitem__(0)
    assert 4 == a.__len__()
    assert 16 == a.capacity
    
def test_insert_last() -> None:
    a: DynArray = DynArray()
    a.append(1)
    a.append(2)
    a.append(3)
    
    a.insert(3, 4)
    assert 4 == a.__getitem__(3)
    assert 4 == a.__len__()
    assert 16 == a.capacity
    
def test_insert_in_empty() -> None:
    a: DynArray = DynArray()
    
    a.insert(0, 1)
    assert 1 == a.__getitem__(0)
    assert 1 == a.__len__()
    assert 16 == a.capacity
    
def test_insert_out_of_left_bound() -> None:
    a: DynArray = DynArray()
    a.append(-1)
    a.append(2)
    a.append(-3)
    
    with pytest.raises(IndexError, match="Index is out of bounds"):
        a.insert(-1, 4)
    assert 3 == a.__len__()
    assert 16 == a.capacity    
        
def test_insert_out_of_right_bound() -> None:
    a: DynArray = DynArray()
    a.append('x')
    a.append('y')
    a.append('z')
    
    with pytest.raises(IndexError, match="Index is out of bounds"):
        a.insert(4, 'w')
    assert 3 == a.__len__()
    assert 16 == a.capacity    
        
def test_insert_with_resize() -> None:
    a: DynArray = DynArray()
    for i in range(a.capacity):
        a.append(i)
    
    a.insert(16, 16)
    assert 16 == a.__getitem__(16)
    assert 17 == a.__len__()
    assert 32 == a.capacity
    
#1.2
def test_delete() -> None:
    a: DynArray = DynArray()
    a.append('a')
    a.append('b')
    a.append('c')
    a.append('e')
    a.append('d')
    
    a.delete(3)
    assert 'd' == a.__getitem__(3)
    assert 4 == a.__len__()
    assert 16 == a.capacity
    
def test_delete_first() -> None:
    a: DynArray = DynArray()
    a.append('a')
    a.append('b')
    a.append('c')
    a.append('e')
    a.append('d')
    
    a.delete(0)
    assert 'b' == a.__getitem__(0)
    assert 4 == a.__len__()
    assert 16 == a.capacity
    
def test_delete_last() -> None:
    a: DynArray = DynArray()
    a.append('a')
    a.append('b')
    a.append('c')
    a.append('e')
    a.append('d')
    
    a.delete(4)
    assert 4 == a.__len__()
    assert 16 == a.capacity
    
def test_delete_if_single() -> None:
    a: DynArray = DynArray()
    a.append('a')
    
    a.delete(0)
    assert 0 == a.__len__()
    assert 16 == a.capacity  
    
def test_delete_out_of_left_bound() -> None:
    a: DynArray = DynArray()
    a.append('a')
    a.append('b')
    a.append('c')
    a.append('e')
    a.append('d')
    
    with pytest.raises(IndexError, match="Index is out of bounds"):
        a.delete(-5)
    assert 5 == a.__len__()
    assert 16 == a.capacity    
        
def test_delete_out_of_right_bound() -> None:
    a: DynArray = DynArray()
    a.append('a')
    a.append('b')
    a.append('c')
    a.append('e')
    a.append('d')
    
    with pytest.raises(IndexError, match="Index is out of bounds"):
        a.delete(5)
    assert 5 == a.__len__()
    assert 16 == a.capacity    
        
def test_insert_with_resize() -> None:
    a: DynArray = DynArray()
    for i in range(33):
        a.append(i)
    
    a.delete(4)
    a.delete(4)
    assert 6 == a.__getitem__(4)
    assert 31 == a.__len__()
    assert 42 == a.capacity        
       
def test_insert_with_resize_to_min_capacity() -> None:
    a: DynArray = DynArray()
    for i in range(17):
        a.append(i)
    for i in range(6):
        a.delete(0)
        
    a.delete(0)    
    assert 7 == a.__getitem__(0)
    assert 10 == a.__len__()
    assert 16 == a.capacity          
        
        
        