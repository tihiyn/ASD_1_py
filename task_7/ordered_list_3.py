from ordered_list import OrderedList

def test_add_empty_asc() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(1)
    assert 1 == ol.head.value
    assert 1 == ol.tail.value
    
def test_add_empty_desc() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(1)
    assert 1 == ol.head.value
    assert 1 == ol.tail.value
    
def test_add_first_asc() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(1)
    ol.add(0)
    assert 0 == ol.head.value
    assert 1 == ol.tail.value
    
def test_add_first_desc() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(0)
    ol.add(1)
    assert 1 == ol.head.value
    assert 0 == ol.tail.value   
    
def test_add_last_asc() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(0)
    ol.add(1)
    assert 0 == ol.head.value
    assert 1 == ol.tail.value
    
def test_add_last_desc() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(1)
    ol.add(0)
    assert 1 == ol.head.value
    assert 0 == ol.tail.value      
    
def test_add_asc() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    assert 0 == ol.head.value
    assert 2 == ol.head.next.value
    assert 4 == ol.head.next.next.value
    assert 7 == ol.tail.value
    
def test_add_desc() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    assert 7 == ol.head.value
    assert 4 == ol.head.next.value
    assert 2 == ol.head.next.next.value
    assert 0 == ol.tail.value
    
def test_delete_asc() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    ol.delete(4)
    assert 3 == ol.len()
    assert ol.find(4) is None
    
def test_delete_desc() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    ol.delete(2)
    assert 3 == ol.len()
    assert ol.find(2) is None
    
def test_delete_asc_if_empty() -> None:
    ol: OrderedList = OrderedList(True)
    ol.delete(4)
    assert 0 == ol.len()
    
def test_delete_desc_if_empty() -> None:
    ol: OrderedList = OrderedList(False)
    ol.delete(10)
    assert 0 == ol.len()
    
def test_delete_asc_if_single() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(5)
    ol.delete(5)
    assert 0 == ol.len()
    assert ol.find(5) is None
    
def test_delete_desc_if_single() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(5)
    ol.delete(5)
    assert 0 == ol.len()
    assert ol.find(5) is None
    
def test_delete_first_asc() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    ol.delete(0)
    assert 3 == ol.len()
    assert ol.find(0) is None
    assert 2 == ol.head.value
    
def test_delete_first_desc() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    ol.delete(7)
    assert 3 == ol.len()
    assert ol.find(7) is None
    assert 4 == ol.head.value   
    
def test_delete_last_asc() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    ol.delete(7)
    assert 3 == ol.len()
    assert ol.find(7) is None
    assert 4 == ol.tail.value    
    
def test_delete_last_desc() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    ol.delete(0)
    assert 3 == ol.len()
    assert ol.find(0) is None
    assert 2 == ol.tail.value 
    
def test_delete_asc_if_not_exist() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    ol.delete(10)
    assert 4 == ol.len()  
    
def test_delete_desc_if_not_exist() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    ol.delete(10)
    assert 4 == ol.len()  
    
def test_delete_asc_if_repeat() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(3)
    ol.add(4)
    ol.add(4)
    ol.add(5)
    ol.delete(4)
    assert 3 == ol.len()   
    
def test_delete_desc_if_repeat() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(4)
    ol.add(4)
    ol.add(4)
    ol.add(4)
    ol.delete(4)
    assert 3 == ol.len()      
    
def test_find_asc() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    assert 2 == ol.find(2).value
    
def test_find_desc() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    assert 2 == ol.find(2).value    
    
def test_find_first_asc() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(0)
    ol.add(-3)
    ol.add(0)
    ol.add(5)
    assert 0 == ol.find(0).value
    assert 0 == ol.find(0).next.value
    
def test_find_first_desc() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(0)
    ol.add(-3)
    ol.add(0)
    ol.add(5)
    assert 0 == ol.find(0).value
    assert 0 == ol.find(0).next.value    
    
def test_find_head_asc() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    assert 0 == ol.find(0).value 
    
def test_find_head_desc() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    assert 7 == ol.find(7).value     
    
def test_find_tail_asc() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    assert 7 == ol.find(7).value   
    
def test_find_tail_desc() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    assert 0 == ol.find(0).value       
    
def test_find_asc_if_not_exist() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    assert ol.find(5) is None
    
def test_find_desc_if_not_exist() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    assert ol.find(5) is None    
    
def test_find_if_lt_head_asc() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    assert ol.find(-1) is None    
    
def test_find_if_gt_tail_asc() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    assert ol.find(9) is None  
    
def test_find_if_gt_head_desc() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    assert ol.find(9) is None    
    
def test_find_if_lt_tail_desc() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(4)
    ol.add(0)
    ol.add(7)
    ol.add(2)
    assert ol.find(-5) is None       
    
def test_find_asc_if_single() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(4)
    assert 4 == ol.find(4).value
    
def test_find_desc_if_single() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(4)
    assert 4 == ol.find(4).value    
    
def test_find_asc_if_single_and_not_exist() -> None:
    ol: OrderedList = OrderedList(True)
    ol.add(4)
    assert ol.find(5) is None
    
def test_find_desc_if_single_and_not_exist() -> None:
    ol: OrderedList = OrderedList(False)
    ol.add(4)
    assert ol.find(5) is None    
    
def test_find_asc_if_empty() -> None:
    ol: OrderedList = OrderedList(True)
    assert ol.find(5) is None
    
def test_find_desc_if_empty() -> None:
    ol: OrderedList = OrderedList(False)
    assert ol.find(5) is None    
    
    
    