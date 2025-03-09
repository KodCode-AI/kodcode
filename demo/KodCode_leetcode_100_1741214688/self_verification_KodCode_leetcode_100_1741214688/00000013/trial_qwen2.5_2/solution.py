class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_left_leaves(root):
    """
    Returns the sum of all left leaves in a binary tree.
    """
    def dfs(node, is_left):
        if not node:
            return 0
        if not node.left and not node.right and is_left:
            return node.val
        return dfs(node.left, True) + dfs(node.right, False)
    
    return dfs(root, False)