class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth_bst(root: TreeNode) -> int:
    """
    Returns the maximum depth of a binary search tree.
    """
    if root is None:
        return 0
    return 1 + max(max_depth_bst(root.left), max_depth_bst(root.right))