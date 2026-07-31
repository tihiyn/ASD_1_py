from typing import Any

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if v1.__lt__(v2):
            return -1;
        if v1.__gt__(v2):
            return 1; 
        return 0

    def add(self, value):
        n: Node = Node(value)
        if self.head is None and self.tail is None:
            self.head = n
            self.tail = n
            return
        cur: Node = self.head
        while cur is not None:
            if self.__ascending == (self.compare(value, cur.value) < 0):
                self._add(cur, n)
                return
            cur = cur.next
        self.tail.next = n
        n.prev = self.tail
        self.tail = n
        
    def _add(self, old: Node, new: Node) -> None:
        if old.prev is None:
            old.prev = new
            new.next = old
            self.head = new
            return
        old.prev.next = new
        new.prev = old.prev
        new.next = old
        old.prev = new   

    '''
    Сложность поиска не изменилась и осталась O(N), так как нет возможности применить бинарный поиск
    из-за отсутствия индексации
    '''
    def find(self, val):
        if self.head is None and self.tail is None:
            return None
        if self.__ascending and (self.compare(val, self.head.value) < 0 or self.compare(val, self.tail.value) > 0):
            return None
        if (not self.__ascending) and (self.compare(val, self.head.value) > 0 or self.compare(val, self.tail.value) < 0):
            return None   
        node: Node = self.head
        while node != None:
            if node.value == val:
                return node
            node = node.next    
        return None    

    def delete(self, val):
        n: Node = self.find(val)
        if n is None:
            return
        if n.prev is None and n.next is None:
            self.head = None
            self.tail = None
            return
        if n.prev is None:
            n.next.prev = None
            self.head = n.next
            return
        if n.next is None:
            n.prev.next = None
            self.tail = n.prev
            return
        n.prev.next = n.next
        n.next.prev = n.prev

    def clean(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def len(self):
        ctr: int = 0;
        node: Node = self.head
        while node is not None:
            ctr += 1
            node = node.next
        return ctr

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        s1: str = v1.strip()
        s2: str = v2.strip()
        if s1 < s2:
            return -1
        if s1 > s2:
            return 1  
        return 0
        
        
        