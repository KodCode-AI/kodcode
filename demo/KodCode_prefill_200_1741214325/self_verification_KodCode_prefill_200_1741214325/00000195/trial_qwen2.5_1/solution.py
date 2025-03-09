class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mirror_tree(root):
    """
    Returns the mirror image of the given binary tree.
    """
    if root is not None:
        root.left, root.right = mirror_tree(root.right), mirror_tree(root.left)
    return root