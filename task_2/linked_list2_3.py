from linked_list2 import Node, LinkedList2
from typing import List

#2.1
def test_find() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(2)
    n4: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    assert n3 == ll.find(2)
    
def test_find_first() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(3)
    n4: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    assert n2 == ll.find(3)
    
def test_find_head() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(2)
    n4: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    assert n1 == ll.find(1)  
    
def test_find_tail() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(2)
    n4: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    assert n4 == ll.find(4)   
    
def test_find_if_not_exist() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(2)
    n4: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    assert ll.find(5) is None
    
def test_find_if_single() -> None:
    n1: Node = Node(1)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    assert n1 == ll.find(1)
    
def test_find_if_single_and_not_exist() -> None:
    n1: Node = Node(1)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    assert ll.find(2) is None
    
#2.2
def test_find_all() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(2)
    n4: Node = Node(3)
    n5: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    res: List[Node] = ll.find_all(3)
    assert len(res) == 2
    assert res[0] == n2
    assert res[1] == n4
    
def test_find_all_if_in_row() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(3)
    n4: Node = Node(3)
    n5: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    res: List[Node] = ll.find_all(3)
    assert len(res) == 3
    assert res[0] == n2
    assert res[1] == n3    
    assert res[2] == n4   
    
def test_find_all_if_single() -> None:
    n1: Node = Node(1)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    res: List[Node] = ll.find_all(1)
    assert len(res) == 1
    assert res[0] == n1   
    
def test_find_all_if_single_not_exist() -> None:
    n1: Node = Node(1)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    res: List[Node] = ll.find_all(2)
    assert len(res) == 0   
    
def test_find_all_if_not_exist() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(3)
    n4: Node = Node(3)
    n5: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    res: List[Node] = ll.find_all(5)
    assert len(res) == 0 
    
def test_find_all_all() -> None:
    n1: Node = Node(3)
    n2: Node = Node(3)
    n3: Node = Node(3)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    res: List[Node] = ll.find_all(3)
    assert len(res) == 3
    assert res[0] == n1
    assert res[1] == n2
    assert res[2] == n3
    
#2.3
def test_delete_first() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(2)
    n4: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.delete(3)
    assert n1.next == n3
    
def test_delete_first_if_head() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(2)
    n4: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.delete(1)
    assert ll.head == n2
    
def test_delete_first_if_tail() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(2)
    n4: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.delete(4)
    assert ll.tail == n3 
    
def test_delete_first_if_empty() -> None:
    ll: LinkedList2 = LinkedList2()
    ll.delete(-3)
    assert ll.head is None
    assert ll.tail is None

def test_delete_first_if_single() -> None:
    n1: Node = Node(1)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.delete(1)
    assert ll.head is None
    assert ll.tail is None

def test_delete_first_if_not_found() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(2)
    n4: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.delete(5)
    assert ll.len() == 4

#2.4
def test_delete_all() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(2)
    n4: Node = Node(3)
    n5: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    ll.delete(3, True)
    assert ll.len() == 3
    assert n1.next == n3
    assert n3.next == n5

def test_delete_all_all() -> None:
    n1: Node = Node(1)
    n2: Node = Node(1)
    n3: Node = Node(1)
    n4: Node = Node(1)
    n5: Node = Node(1)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    ll.delete(1, True)
    assert ll.head is None
    assert ll.tail is None

def test_delete_all_if_head() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(5)
    n4: Node = Node(3)
    n5: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    ll.delete(1, True)
    assert ll.head == n2
    
def test_delete_all_if_in_row() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(3)
    n4: Node = Node(3)
    n5: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    ll.delete(3, True)
    assert ll.len() == 2
    assert n1.next == n5

def test_delete_all_if_tail() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(5)
    n4: Node = Node(3)
    n5: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    ll.delete(4, True)
    assert ll.tail == n4

def test_delete_all_first_if_single() -> None:
    n1: Node = Node(1)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.delete(1, True)
    assert ll.head is None
    assert ll.tail is None

def test_delete_all_first_if_not_found() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(2)
    n4: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.delete(5, True)
    assert ll.len() == 4
    
#2.5
def test_insert() -> None:
    n1: Node = Node(1)
    n2: Node = Node(2)
    n3: Node = Node(3)
    n4: Node = Node(4)
    n5: Node = Node(5)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    n6: Node = Node(6)
    ll.insert(n3, n6)
    assert ll.len() == 6
    assert n3.next == n6
    assert n6.next == n4   
    
def test_insert_if_empty() -> None:
    ll: LinkedList2 = LinkedList2()
    n1: Node = Node(1)
    ll.insert(None, n1)
    assert ll.len() == 1
    assert ll.head == n1
    assert ll.tail == n1
    
def test_insert_in_tail() -> None:
    n1: Node = Node(1)
    n2: Node = Node(2)
    n3: Node = Node(3)
    n4: Node = Node(4)
    n5: Node = Node(5)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    n6: Node = Node(6)
    ll.insert(n5, n6)
    assert ll.len() == 6
    assert ll.tail == n6
    assert n5.next == n6    
    assert n6.next is None
    
def test_insert_in_tail_if_single() -> None:
    n1: Node = Node(1)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    n2: Node = Node(2)
    ll.insert(n1, n2)
    assert ll.len() == 2
    assert ll.tail == n2
    assert n1.next == n2   
    assert n2.next is None
    
def test_insert_in_tail_if_single_and_after_node_is_none() -> None:
    n1: Node = Node(1)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    n2: Node = Node(2)
    ll.insert(None, n2)
    assert ll.len() == 2
    assert ll.tail == n2
    assert n1.next == n2   
    assert n2.next is None  
    
#2.6
def test_add_in_head() -> None:
    n1: Node = Node(1)
    n2: Node = Node(2)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    n0: Node = Node(0)
    ll.add_in_head(n0)
    assert n0 == ll.head
    assert n0.next == n1
    assert n0.prev == None
    assert n0 == n1.prev
    
def test_add_in_head_if_single() -> None:
    n1: Node = Node(1)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    n0: Node = Node(0)
    ll.add_in_head(n0)
    assert n0 == ll.head
    assert n0.next == n1
    assert n0.prev == None
    assert n0 == n1.prev
    assert n1 == ll.tail
    
def test_add_in_head_if_empty() -> None:
    ll: LinkedList2 = LinkedList2()
    n0: Node = Node(0)
    ll.add_in_head(n0)
    assert n0 == ll.head
    assert n0 == ll.tail
    assert n0.next == None
    assert n0.prev == None
    
#2.7
def test_clean() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(2)
    n4: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.clean()
    assert ll.head is None
    assert ll.tail is None

def test_clean_if_empty() -> None:
    ll: LinkedList2 = LinkedList2()
    ll.clean()
    assert ll.head is None
    assert ll.tail is None

#2.8
def test_len() -> None:
    n1: Node = Node(1)
    n2: Node = Node(3)
    n3: Node = Node(3)
    n4: Node = Node(3)
    n5: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    assert ll.len() == 5
    
def test_len_if_empty() -> None:
    ll: LinkedList2 = LinkedList2()
    assert ll.len() == 0
    
def test_len_if_single() -> None:
    n1: Node = Node(1)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    assert ll.len() == 1
    

