class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def contains_BST(root, target):
    if root is None:
        return False
    if target == root.value:
        return True
    elif target < root.value:
        return contains_BST(root.left, target)
    else:
        return contains_BST(root.right, target)

def insert_BST(root, value):
    if root is None:
        return Node(value)
    if value == root.value:
        return root
    elif value < root.value:
        root.left = insert_BST(root.left, value)
    else:
        root.right = insert_BST(root.right, value)
    return root