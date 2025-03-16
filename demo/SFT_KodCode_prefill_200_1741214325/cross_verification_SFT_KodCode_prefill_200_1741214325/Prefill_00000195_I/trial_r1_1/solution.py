class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def mirror_tree(root):
    if root is None:
        return
    # Swap the left and right children
    root.left, root.right = root.right, root.left
    # Recursively mirror the left and right subtrees
    mirror_tree(root.left)
    mirror_tree(root.right)