# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    """
    Return the max depth of a binary tree.
    """
    if root is None:
        return 0
    else:
        left_depth = max_depth(root.left)
        right_depth = max_depth(root.right)
        return max(left_depth, right_depth) + 1