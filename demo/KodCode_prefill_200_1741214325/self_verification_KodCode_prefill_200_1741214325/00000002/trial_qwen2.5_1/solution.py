class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth_bst(root: TreeNode) -> int:
    """
    Returns the maximum depth of a binary search tree.
    """
    if not root:
        return 0
    left_depth = max_depth_bst(root.left)
    right_depth = max_depth_bst(root.right)
    return max(left_depth, right_depth) + 1