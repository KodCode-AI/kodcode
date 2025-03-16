class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_bst(root, target):
    if not root:
        return False
    if root.value == target:
        return True
    elif target < root.value:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)

def insert_bst(root, value):
    if not root:
        return Node(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root