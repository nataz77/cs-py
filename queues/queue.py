from typing import Any
from .linkedlistnode import LinkedListNode


class Queue:
    def __init__(self):
        self.front = None
        self.back = None
        self.len = 0

    def peek(self) -> Any:
        if self.is_empty():
            raise Exception("The queue is empty")
        else:
            return self.front.data

    def is_empty(self) -> bool:
        return self.front is None

    def enqueue(self, value) -> None:
        NewNode = LinkedListNode(value)
        if self.front is None and self.back is None:
            self.head = NewNode
        else:
            self.back.next = NewNode
        self.back = NewNode
        self.len += 1

    def dequeue(self) -> Any:
        if self.is_empty():
            raise Exception("The queue is empty")
        val = self.front.data
        self.front = self.front.next
        self.count -= 1
        return val
