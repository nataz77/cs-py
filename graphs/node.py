from ll import LinkedList, LinkedListNode

class GraphNode:

    def __init__(self, id):
        self.ID = id
        self.Discovered = False
        self.neightbours = LinkedList()
        
    
    def mark_discovered(self):
        self.Discovered = True

    def add_neighbour(self, n):
        # I could pass in a list or a single element
        if isinstance(n, list):
            for i in n:
                self.neightbours.add_last(i)
        else:
            self.neightbours.add_last(n)