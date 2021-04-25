class TreeNode:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __init__(self, value, left):
        self.value = value
        self.left = left
        self.right = None
    
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
