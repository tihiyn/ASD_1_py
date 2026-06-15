from linked_list import Node, LinkedList

"""
Задание 1, задача 8: сложение двух связных списков.
Сложность алгоритма:
    - временная: O(N)
    - пространственная: O(N).
"""
def sum(l1, l2):
    res = LinkedList()
    if (l1.len() != l2.len() or l1.head is None):
        return res
    n1 = l1.head
    n2 = l2.head
    while n1 is not None:
        res.add_in_tail(Node(n1.value + n2.value))
        n1 = n1.next
        n2 = n2.next
    return res
    
    
