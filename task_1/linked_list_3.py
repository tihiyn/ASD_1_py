from linked_list import Node, LinkedList

# 1.1
def test_delete_first():
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(2)
    n4 = Node(4)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.delete(3)
    assert n1.next == n3
    
def test_delete_first_if_head():
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(2)
    n4 = Node(4)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.delete(1)
    assert ll.head == n2
    
def test_delete_first_if_tail():
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(2)
    n4 = Node(4)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.delete(4)
    assert ll.tail == n3 
    
def test_delete_first_if_empty():
    ll = LinkedList()
    ll.delete(-3)
    assert ll.head is None
    assert ll.tail is None

def test_delete_first_if_single():
    n1 = Node(1)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.delete(1)
    assert ll.head is None
    assert ll.tail is None

def test_delete_first_if_not_found():
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(2)
    n4 = Node(4)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.delete(5)
    assert ll.len() == 4
    
#1.2
def test_delete_all():
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(2)
    n4 = Node(3)
    n5 = Node(4)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    ll.delete(3, True)
    assert ll.len() == 3
    assert n1.next == n3
    assert n3.next == n5

def test_delete_all_all():
    n1 = Node(1)
    n2 = Node(1)
    n3 = Node(1)
    n4 = Node(1)
    n5 = Node(1)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    ll.delete(1, True)
    assert ll.head is None
    assert ll.tail is None

def test_delete_all_if_head():
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(5)
    n4 = Node(3)
    n5 = Node(4)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    ll.delete(1, True)
    assert ll.head == n2
    
def test_delete_all_if_in_row():
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(3)
    n4 = Node(3)
    n5 = Node(4)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    ll.delete(3, True)
    assert ll.len() == 2
    assert n1.next == n5

def test_delete_all_if_tail():
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(5)
    n4 = Node(3)
    n5 = Node(4)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    ll.delete(4, True)
    assert ll.tail == n4

def test_delete_all_first_if_single():
    n1 = Node(1)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.delete(1, True)
    assert ll.head is None
    assert ll.tail is None

def test_delete_all_first_if_not_found():
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(2)
    n4 = Node(4)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.delete(5, True)
    assert ll.len() == 4

#1.3
def test_clean():
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(2)
    n4 = Node(4)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.clean()
    assert ll.head is None
    assert ll.tail is None

def test_clean_if_empty():
    ll = LinkedList()
    ll.clean()
    assert ll.head is None
    assert ll.tail is None

#1.4
def test_find_all():
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(2)
    n4 = Node(3)
    n5 = Node(4)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    res = ll.find_all(3)
    assert len(res) == 2
    assert res[0] == n2
    assert res[1] == n4
    
def test_find_all_if_in_row():
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(3)
    n4 = Node(3)
    n5 = Node(4)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    res = ll.find_all(3)
    assert len(res) == 3
    assert res[0] == n2
    assert res[1] == n3    
    assert res[2] == n4   
    
def test_find_all_if_single():
    n1 = Node(1)
    ll = LinkedList()
    ll.add_in_tail(n1)
    res = ll.find_all(1)
    assert len(res) == 1
    assert res[0] == n1   
    
def test_find_all_if_single_not_exist():
    n1 = Node(1)
    ll = LinkedList()
    ll.add_in_tail(n1)
    res = ll.find_all(2)
    assert len(res) == 0   
    
def test_find_all_if_not_exist():
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(3)
    n4 = Node(3)
    n5 = Node(4)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    res = ll.find_all(5)
    assert len(res) == 0 
    
def test_find_all_all():
    n1 = Node(3)
    n2 = Node(3)
    n3 = Node(3)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    res = ll.find_all(3)
    assert len(res) == 3
    assert res[0] == n1
    assert res[1] == n2
    assert res[2] == n3
    
#1.5
def test_len():
    n1 = Node(1)
    n2 = Node(3)
    n3 = Node(3)
    n4 = Node(3)
    n5 = Node(4)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    assert ll.len() == 5
    
def test_len_if_empty():
    ll = LinkedList()
    assert ll.len() == 0
    
def test_len_if_single():
    n1 = Node(1)
    ll = LinkedList()
    ll.add_in_tail(n1)
    assert ll.len() == 1
    
#1.6
def test_insert():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    n6 = Node(6)
    ll.insert(n3, n6)
    assert ll.len() == 6
    assert n3.next == n6
    assert n6.next == n4
    
def test_insert_in_head():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    n6 = Node(6)
    ll.insert(None, n6)
    assert ll.len() == 6
    assert ll.head == n6
    assert n6.next == n1
    
def test_insert_in_head_if_single():
    n1 = Node(1)
    ll = LinkedList()
    ll.add_in_tail(n1)
    n2 = Node(2)
    ll.insert(None, n2)
    assert ll.len() == 2
    assert ll.head == n2
    assert n2.next == n1    
    
def test_insert_in_head_if_empty():
    ll = LinkedList()
    n1 = Node(1)
    ll.insert(None, n1)
    assert ll.len() == 1
    assert ll.head == n1
    assert ll.tail == n1
    
def test_insert_in_tail():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    ll = LinkedList()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    n6 = Node(6)
    ll.insert(n5, n6)
    assert ll.len() == 6
    assert ll.tail == n6
    assert n5.next == n6    
    assert n6.next is None
    
def test_insert_in_tail_if_single():
    n1 = Node(1)
    ll = LinkedList()
    ll.add_in_tail(n1)
    n2 = Node(2)
    ll.insert(n1, n2)
    assert ll.len() == 2
    assert ll.tail == n2
    assert n1.next == n2   
    assert n2.next is None   
    
    
