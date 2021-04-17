class LinkedListNode:
    def __init__(self, val=None): 
        self.data = val
        self.next = None
        self.previous = None
    
    @property
    def HasNext(self):
        return self.next != None