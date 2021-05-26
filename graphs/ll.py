from typing import Iterable


class LinkedListNode:
    def __init__(self, val=None):
        self.data = val
        self.next = None
        self.previous = None

    @property
    def HasNext(self) -> bool:
        return self.next is not None


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add_last(self, val) -> None:
        NewNode = LinkedListNode(val)
        if self.head is None:
            self.head = NewNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = NewNode

    def __iter__(self) -> Iterable:
        n = []
        printval = self.head
        while printval is not None:
            n.append(printval)
            printval = printval.next
        return iter(n)
