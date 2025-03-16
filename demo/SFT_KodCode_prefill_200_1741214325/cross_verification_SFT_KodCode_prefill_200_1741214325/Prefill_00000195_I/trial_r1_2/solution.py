class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def mirror_tree(root):
    if root is None:
        return None
    new_node = Node(root.value)
    new_node.left = mirror_tree(root.right)
    new_node.right = mirror_tree(root.left)
    return new_node