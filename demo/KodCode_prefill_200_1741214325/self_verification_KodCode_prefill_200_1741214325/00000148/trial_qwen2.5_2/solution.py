class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: TreeNode) -> int:
    """
    Returns the maximum depth of a binary tree.
    """
    if not root:
        return 0
    left_depth = max_depth(root.left) if root.left else 0
    right_depth = max_depth(root.right) if root.right else 0
    return max(left_depth, right_depth) + 1