class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        nodes = []
        node = self.head
        while node is not None:
            if node.value == val:
                nodes.append(node)
            node = node.next
        return nodes    

    def delete(self, val, all=False):
        if (self.head is None):
            return
        if (not all):
            self._delete_first(val)
            return
        self._delete_all(val)    
    
    def _delete_first(self, val):
        if (self.head.value == val):
            self._delete_head()
            return
        node = self.head
        while node.next is not None:
            if (node.next.value == val):
                self._delete(node)
                break
            node = node.next  
            
    def _delete_all(self, val):
        while self.head is not None and self.head.value == val:
            self._delete_head()
        if (self.head is None):
            return
        node = self.head
        while node.next is not None:
            if (node.next.value == val):
                self._delete(node)
                continue;
            node = node.next 
                
    def _delete_head(self):
        self.head = self.head.next
        if (self.head is None):
            self.tail = None
    
    def _delete(self, node):
        node.next = node.next.next
        if (node.next is None):
            self.tail = node

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        ctr = 0;
        node = self.head
        while node is not None:
            ctr += 1
            node = node.next
        return ctr

    def insert(self, afterNode, newNode):
        if (self.head is None):
            self.head = newNode
            newNode.next = None
            self.tail = newNode
            return
        if (afterNode is None):
            newNode.next = self.head
            self.head = newNode
            return
        newNode.next = afterNode.next
        afterNode.next = newNode
        if (newNode.next is None):
            self.tail = newNode
            
            
