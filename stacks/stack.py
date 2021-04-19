from linkedlistnode import LinkedListNode
class Stack:
    """Implementation of a stack"""
    def __init__(self):
        self.head = None
        self.count = 0
    
    def peek(self):
        if self.is_empty():
            raise Exception("Unable to peek value: the stack is empty")
        return self.head.data

    def is_empty(self):       
        return self.count == 0
    
    def push(self, value):
        node = LinkedListNode(value)
        if self.is_empty():
            self.head = node
            self.count += 1
            return
        node = LinkedListNode(value)
        node.next = self.head
        self.head = node
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise Exception("There are no values in the stack")
        val = self.head.data
        self.head = self.head.next
        self.count -= 1
        return val