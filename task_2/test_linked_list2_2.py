from linked_list2 import Node, LinkedList2
from linked_list2_2 import invert
from linked_list2_2 import is_cycled
from linked_list2_2 import sort
from linked_list2_2 import merge

#2.10
def test_invert_if_odd() -> None:
    n1: Node = Node(1)
    n2: Node = Node(2)
    n3: Node = Node(3)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    invert(ll)
    assert n1.value == 3
    assert n2.value == 2
    assert n3.value == 1
    
def test_invert_if_not_odd() -> None:
    n1: Node = Node(1)
    n2: Node = Node(2)
    n3: Node = Node(3)
    n4: Node = Node(4)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    invert(ll)
    assert n1.value == 4
    assert n2.value == 3
    assert n3.value == 2    
    assert n4.value == 1 
    
def test_invert_if_empty() -> None:
    ll: LinkedList2 = LinkedList2()
    invert(ll)
    assert ll.head is None
    assert ll.tail is None
    
def test_invert_if_single() -> None:
    n1: Node = Node(1)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    invert(ll)
    assert n1.value == 1
    assert n1.next == None
    assert n1.prev == None
    assert ll.head == n1
    assert ll.tail == n1
    
#2.11
def test_is_cycled_by_next() -> None:
    n1: Node = Node(1)
    n2: Node = Node(2)
    n3: Node = Node(3)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    n3.next = n1
    assert is_cycled(ll)

def test_is_cycled_by_prev() -> None:
    n1: Node = Node(1)
    n2: Node = Node(2)
    n3: Node = Node(3)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    n2.prev = n3
    assert is_cycled(ll)
    
def test_is_not_cycled() -> None:
    n1: Node = Node(1)
    n2: Node = Node(2)
    n3: Node = Node(3)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    assert not is_cycled(ll)  
    
def test_is_cycled_if_single_by_next() -> None:
    n1: Node = Node(1)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    n1.next = n1
    assert is_cycled(ll)    
    
def test_is_cycled_if_single_by_prev() -> None:
    n1: Node = Node(1)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    n1.prev = n1
    assert is_cycled(ll)    
    
def test_is_not_cycled_if_empty() -> None:
    ll: LinkedList2 = LinkedList2()
    assert not is_cycled(ll)     
    
def test_is_cycled_by_next_and_prev() -> None:
    n1: Node = Node(1)
    n2: Node = Node(2)
    n3: Node = Node(3)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    n2.prev = n3
    n3.next = n1
    assert is_cycled(ll)
    
#2.12
def test_sort() -> None:
    n1: Node = Node(5)
    n2: Node = Node(7)
    n3: Node = Node(3)
    n4: Node = Node(4)
    n5: Node = Node(8)
    n6: Node = Node(1)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    ll.add_in_tail(n6)
    sort(ll)
    assert n1.value == 1   
    assert n2.value == 3   
    assert n3.value == 4   
    assert n4.value == 5   
    assert n5.value == 7   
    assert n6.value == 8   
    
def test_sort_with_negative() -> None:
    n1: Node = Node(5)
    n2: Node = Node(0)
    n3: Node = Node(3)
    n4: Node = Node(-9)
    n5: Node = Node(-4)
    n6: Node = Node(1)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    ll.add_in_tail(n4)
    ll.add_in_tail(n5)
    ll.add_in_tail(n6)
    sort(ll)
    assert n1.value == -9   
    assert n2.value == -4  
    assert n3.value == 0   
    assert n4.value == 1   
    assert n5.value == 3   
    assert n6.value == 5
    
def test_sort_if_two() -> None:
    n1: Node = Node(5)
    n2: Node = Node(0)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    sort(ll)
    assert n1.value == 0   
    assert n2.value == 5
    
def test_sort_if_sorted() -> None:
    n1: Node = Node(1)
    n2: Node = Node(2)
    n3: Node = Node(3)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    ll.add_in_tail(n2)
    ll.add_in_tail(n3)
    sort(ll)
    assert n1.value == 1   
    assert n2.value == 2  
    assert n3.value == 3  

def test_sort_if_single() -> None:
    n1: Node = Node(5)
    ll: LinkedList2 = LinkedList2()
    ll.add_in_tail(n1)
    sort(ll)
    assert n1.value == 5

def test_sort_if_empty() -> None:
    ll: LinkedList2 = LinkedList2()
    sort(ll)
    assert ll.head is None
    assert ll.tail is None

#2.13
def test_merge() -> None:
    n1: Node = Node(5)
    n2: Node = Node(7)
    n3: Node = Node(3)
    f: LinkedList2 = LinkedList2()
    f.add_in_tail(n1)
    f.add_in_tail(n2)
    f.add_in_tail(n3)
    s: LinkedList2 = LinkedList2()
    n4: Node = Node(4)
    n5: Node = Node(8)
    n6: Node = Node(1)
    s.add_in_tail(n4)
    s.add_in_tail(n5)
    s.add_in_tail(n6)
    res: LinkedList2 = merge(f, s)
    assert res.head.value == 1
    assert res.head.next.value == 3
    assert res.head.next.next.value == 4
    assert res.head.next.next.next.value == 5
    assert res.head.next.next.next.next.value == 7
    assert res.head.next.next.next.next.next.value == 8
    
def test_merge_if_all_in_f_lt_all_in_s() -> None:
    n1: Node = Node(5)
    n2: Node = Node(7)
    n3: Node = Node(3)
    f: LinkedList2 = LinkedList2()
    f.add_in_tail(n1)
    f.add_in_tail(n2)
    f.add_in_tail(n3)
    s: LinkedList2 = LinkedList2()
    n4: Node = Node(9)
    n5: Node = Node(8)
    n6: Node = Node(12)
    s.add_in_tail(n4)
    s.add_in_tail(n5)
    s.add_in_tail(n6)
    res: LinkedList2 = merge(f, s)
    assert res.head.value == 3
    assert res.head.next.value == 5
    assert res.head.next.next.value == 7
    assert res.head.next.next.next.value == 8
    assert res.head.next.next.next.next.value == 9
    assert res.head.next.next.next.next.next.value == 12   

def test_merge_if_all_in_f_gt_all_in_s() -> None:
    n1: Node = Node(9)
    n2: Node = Node(8)
    n3: Node = Node(12)
    f: LinkedList2 = LinkedList2()
    f.add_in_tail(n1)
    f.add_in_tail(n2)
    f.add_in_tail(n3)
    s: LinkedList2 = LinkedList2()
    n4: Node = Node(5)
    n5: Node = Node(7)
    n6: Node = Node(3)
    s.add_in_tail(n4)
    s.add_in_tail(n5)
    s.add_in_tail(n6)
    res: LinkedList2 = merge(f, s)
    assert res.head.value == 3
    assert res.head.next.value == 5
    assert res.head.next.next.value == 7
    assert res.head.next.next.next.value == 8
    assert res.head.next.next.next.next.value == 9
    assert res.head.next.next.next.next.next.value == 12  
    
def test_merge_if_both_single() -> None:
    n1: Node = Node(9)
    f: LinkedList2 = LinkedList2()
    f.add_in_tail(n1)
    s: LinkedList2 = LinkedList2()
    n4: Node = Node(5)
    s.add_in_tail(n4)
    res: LinkedList2 = merge(f, s)
    assert res.head.value == 5
    assert res.head.next.value == 9 
    
def test_merge_if_both_empty() -> None:
    f: LinkedList2 = LinkedList2()
    s: LinkedList2 = LinkedList2()
    res: LinkedList2 = merge(f, s)
    assert res.head is None
    assert res.tail is None
    
    

    