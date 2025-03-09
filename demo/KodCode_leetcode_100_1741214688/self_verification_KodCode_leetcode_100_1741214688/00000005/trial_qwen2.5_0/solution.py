class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root: TreeNode) -> int:
    """
    Returns the sum of all root-to-leaf numbers in the tree.
    """
    def dfs(node, current_number):
        if not node:
            return 0
        current_number = current_number * 10 + node.val
        if not node.left and not node.right:  # it's a leaf
            return current_number
        return dfs(node.left, current_number) + dfs(node.right, current_number)
    
    return dfs(root, 0)