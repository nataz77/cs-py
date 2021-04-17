from ll import LinkedList, LinkedListNode

class GraphNode:
    """Represents a graph node"""
    def __init__(self, id):
        self.ID = id
        self.Discovered = False
        self.neightbours = LinkedList()
        
    
    def mark_discovered(self):
        """Marks the node as discovered"""
        self.Discovered = True

    def add_neighbour(self, n):
        """Adds a neightbour to the current node"""
        # I could pass in a list or a single element
        if isinstance(n, list):
            for i in n:
                self.neightbours.add_last(i)
        else:
            self.neightbours.add_last(n)