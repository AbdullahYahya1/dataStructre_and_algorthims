from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, data=0):
        if not self.head:
            self.head = ListNode(data)
            return
        
        newNode = ListNode(data)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = newNode
        newNode.prev = curr
    
    def prepend(self, data=0):
        newNode = ListNode(data)
        newNode.next = self.head
        if self.head:
            self.head.prev = newNode
        self.head = newNode
    
    def find(self, data):
        curr = self.head
        while curr:
            if curr.val == data:
                return curr
            curr = curr.next
        return None
    
    def delete(self, data):
        node_to_delete = self.find(data)
        if not node_to_delete:
            print('No element with value:', data)
            return

        if node_to_delete.prev:
            node_to_delete.prev.next = node_to_delete.next
        else:
            self.head = node_to_delete.next
            
        if node_to_delete.next:
            node_to_delete.next.prev = node_to_delete.prev
    def addAfter(self  , data , val):
        node_to_add_after = self.find(data)
        if not node_to_add_after:
            print('No element with value:', data)
            return

        newNode=ListNode(val)
        if not node_to_add_after.next:
            node_to_add_after.next =newNode
            newNode.prev=node_to_add_after
            return

        nextNode = node_to_add_after.next
        newNode.prev = node_to_add_after
        newNode.next =nextNode
        node_to_add_after.next = newNode
        nextNode.pre = newNode

        

    def __str__(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        return ' <-> '.join(elements)

# Test the DoublyLinkedList class
L = DoublyLinkedList()
L.append(6)
L.append(2)
L.append(9)
L.prepend(1)
print(L)  # This will display the elements in the doubly linked list
