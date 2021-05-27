from typing import Any
from .linkedlistnode import LinkedListNode


class Deque:
    """Implementation of a double ended queue using a doubly linked list
       TODO: this is yet to be finished and tested.
    """

    def __init__(self):
        self.front = None
        self.back = None
        self.len = 0

    def enqueue_front(self, value) -> None:
        NewNode = LinkedListNode(value)
        NewNode.next = self.front
        NewNode.previous = None
        self.front.previous = NewNode
        self.front = NewNode
        self.len += 1

    # TODO: fix this
    def enqueue_back(self, value) -> None:
        NewNode = LinkedListNode(value)
        if self.front is None:
            pass
        if self.back is None:
            NewNode.previous = None
            self.back = NewNode
        else:
            NewNode.previous = self.back
            self.back.next = NewNode
        self.back = NewNode
        self.len += 1

    def dequeue_front(self) -> Any:
        if self.is_empty():
            raise IndexError("The queue is empty")
        val = self.front.data
        self.front = self.front.next
        self.count -= 1
        return val

    # TODO: fix this
    def deque_back(self):
        if self.is_empty():
            raise IndexError("The queue is empty")
        

    def peek_front(self) -> None:
        if self.front is None:
            raise IndexError("The deque is empty")
        return self.front.data

    def peek_back(self) -> None:
        if self.back is None:
            raise IndexError("The deque is empty")
        return self.back.data
