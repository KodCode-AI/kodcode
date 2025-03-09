class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root, low, high):
    """
    Calculate the sum of values of all nodes with values within the range [low, high] in a BST.
    """
    def dfs(node):
        if not node:
            return 0
        if node.val < low:
            return dfs(node.right)
        elif node.val > high:
            return dfs(node.left)
        else:
            return node.val + dfs(node.right) + dfs(node.left)
    
    return dfs(root)