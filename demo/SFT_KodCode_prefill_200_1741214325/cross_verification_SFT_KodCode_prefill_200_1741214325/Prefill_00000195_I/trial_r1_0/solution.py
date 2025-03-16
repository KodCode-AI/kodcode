class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mirror_tree(root):
    if root is None:
        return None
    # Swap left and right children
    root.left, root.right = root.right, root.left
    # Recursively mirror the left and right subtrees
    mirror_tree(root.left)
    mirror_tree(root.right)
    return root