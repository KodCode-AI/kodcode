class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def contains(root, target):
    if root is None:
        return False
    if root.value == target:
        return True
    elif target < root.value:
        return contains(root.left, target)
    else:
        return contains(root.right, target)

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root