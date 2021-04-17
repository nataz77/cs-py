from linkedlistnode import LinkedListNode    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def add_last(self, val):
        NewNode = LinkedListNode(val)
        if self.head is None:
            self.head = NewNode
            return   
        last = self.head
        while last.next:
            last = last.next
        last.next = NewNode

    def __iter__(self):        
        n = []
        printval = self.head
        while printval is not None:
            n.append(printval)
            printval = printval.next
        return iter(n)
    
    def get_item(self, index):
        if ! isinstance(index, int):
            raise ValueError("The index must be a number")
        i = 0
        node = self.head
        while i <= index:
            if i = index:
                return node.data
            else:
                node = node.next
                i += 1
    
    def search_item(self, value):
        node = self.head
        while node.data != value and node is not None:
            node = node.next
        return node.value

    def insert_front(self, value):
        new_node = LinkedListNode(value)
        new_node.next = self.head
        self.head = new_node
    
    def remove_item(self, value):
        node = self.head
        previous = None
        while node.data != value and node is not None:
            previous = node
            node = node.next            
        previous.next = node.next
    
