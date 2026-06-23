from typing import List
from typing import Any

class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val: Any) -> Node:
        node: Node = self.head
        while node != None:
            if node.value == val:
                return node
            node = node.next    
        return None        

    def find_all(self, val: Any) -> List[Node]:
        res: List[Node] = [] 
        node: Node = self.head
        while node != None:
            if node.value == val:
                res.append(node)
            node = node.next    
        return res 

    def delete(self, val: Any, all: bool=False) -> None:
        node: Node = self.head
        while node is not None:
            if node.value == val and all:
                self._delete(node)
                node = node.next
                continue
            if node.value == val:
                self._delete(node)
                break
            node = node.next   
    
    def _delete(self, node: Node) -> None:
        if node.prev is None and node.next is None:
            self.head = None
            self.tail = None
            return None
        if node.prev is None:
            node.next.prev = node.prev
            self.head = node.next
            return None
        if node.next is None:
            node.prev.next = node.next
            self.tail = node.prev
            return None
        node.prev.next = node.next
        node.next.prev = node.prev
        

    def clean(self) -> None:
        self.head = None
        self.tail = None

    def len(self) -> int:
        ctr: int = 0;
        node: Node = self.head
        while node is not None:
            ctr += 1
            node = node.next
        return ctr

    def insert(self, afterNode: Node | None, newNode: Node) -> None:
        if self.head is None:
            self.head = newNode
            newNode.next = None
            newNode.prev = None
            self.tail = newNode
            return None
        if afterNode is None:
            afterNode = self.tail
        newNode.next = afterNode.next
        newNode.prev = afterNode
        afterNode.next = newNode
        if newNode.next is None:
            self.tail = newNode
            return None
        newNode.next.prev = newNode    

    def add_in_head(self, newNode: Node) -> None:
        if self.head is None:
            newNode.prev = None
            newNode.next = None
            self.head = newNode
            self.tail = newNode
            return None
        newNode.next = self.head
        self.head.prev = newNode
        newNode.prev = None
        self.head = newNode
            

