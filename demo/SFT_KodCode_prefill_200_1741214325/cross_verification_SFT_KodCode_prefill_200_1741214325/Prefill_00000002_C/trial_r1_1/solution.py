class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def max_depth_bst(root: TreeNode) -> int:
    """Returns the maximum depth of a binary search tree."""
    if not root:
        return 0
    left_depth = max_depth_bst(root.left)
    right_depth = max_depth_bst(root.right)
    return 1 + max(left_depth, right_depth)