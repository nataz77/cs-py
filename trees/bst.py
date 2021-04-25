from node import TreeNode


class BST:
    def __init__(self):
        self.root = None

    def create_bst(self):
        return self.root

    def bst_insert(self, val, t):
        self.root = insert_node(t.root, val)

    def insert_node(self, node, new_node_value):
        if node is None:
            node = TreeNode(new_node_value)
        elif new_node_value < node.value:
            node.left = self.insert_node(node.left, new_node_value)
        elif new_node_value > node.value:
            node.right = self.insert_node(node.right, new_node_value)
        return node
