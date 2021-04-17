from linkedlistnode import LinkedListNode    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        """Prints out a basic node -> node -> etc representation of the list"""
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    
    def add_last(self, val):
        """Adds an item at the back of the linked list"""
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
        current = self.head
        while current is not None:
            n.append(current)
            current = current.next
        return iter(n)
    
    def get_item(self, index):
        """Gets the item in a linked list via its index"""
        if ! isinstance(index, int):
            raise ValueError("The index must be a number")
        i = 0
        node = self.head
        while node is not None:
            if i = index:
                return node.data
            node = node.next
            i += 1
        raise ValueError("The specified index does not exist")
    
    
    def search_item(self, value):
        """Searches the linked list to see if the specified item is present"""
        node = self.head
        while node is not None:
            if node.data == value:
                    return True
            node = node.next
        return False

    def insert_front(self, value):
        """Inserts a new node at the front of the linked list"""
        new_node = LinkedListNode(value)
        new_node.next = self.head
        self.head = new_node
    
    def remove_item(self, value):
        """Removes the item at the specified index"""
        node = self.head
        previous = None
        while node.data != value and node is not None:
            previous = node
            node = node.next            
        previous.next = node.next
    
