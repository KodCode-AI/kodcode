# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_numbers(root: TreeNode) -> int:
    """
    Returns the sum of all root-to-leaf numbers in the binary tree.
    """
    def helper(node, path_sum):
        if not node:
            return 0
        path_sum = path_sum * 10 + node.val
        if not node.left and not node.right:
            return path_sum
        return helper(node.left, path_sum) + helper(node.right, path_sum)
    
    return helper(root, 0)