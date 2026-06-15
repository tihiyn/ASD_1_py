from linked_list import Node, LinkedList
from sum_linked_list import sum

def test_sum():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    l1 = LinkedList()
    l1.add_in_tail(n1)
    l1.add_in_tail(n2)
    l1.add_in_tail(n3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    l2 = LinkedList()
    l2.add_in_tail(n4)
    l2.add_in_tail(n5)
    l2.add_in_tail(n6)
    res = sum(l1, l2)
    assert res.len() == 3
    assert res.head.value == 5 
    assert res.head.next.value == 7 
    assert res.head.next.next.value == 9
    
def test_sum_if_negative():
    n1 = Node(-1)
    n2 = Node(2)
    n3 = Node(-3)
    l1 = LinkedList()
    l1.add_in_tail(n1)
    l1.add_in_tail(n2)
    l1.add_in_tail(n3)
    n4 = Node(4)
    n5 = Node(-5)
    n6 = Node(6)
    l2 = LinkedList()
    l2.add_in_tail(n4)
    l2.add_in_tail(n5)
    l2.add_in_tail(n6)
    res = sum(l1, l2)
    assert res.len() == 3
    assert res.head.value == 3 
    assert res.head.next.value == -3 
    assert res.head.next.next.value == 3
    
def test_sum_if_diff_len():
    n1 = Node(-1)
    n2 = Node(2)
    l1 = LinkedList()
    l1.add_in_tail(n1)
    l1.add_in_tail(n2)
    n4 = Node(4)
    n5 = Node(-5)
    n6 = Node(6)
    l2 = LinkedList()
    l2.add_in_tail(n4)
    l2.add_in_tail(n5)
    l2.add_in_tail(n6)
    res = sum(l1, l2)
    assert res.len() == 0
    
def test_sum_if_both_empty():
    l1 = LinkedList()
    l2 = LinkedList()
    res = sum(l1, l2)
    assert res.len() == 0     
    
