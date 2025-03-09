class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
    """
    Returns the sum of values of nodes with values in the given range.
    """
    def dfs(node):
        if not node:
            return 0
        result = 0
        if low <= node.val <= high:
            result += node.val
        if low < node.val:
            result += dfs(node.left)
        if node.val < high:
            result += dfs(node.right)
        return result

    return dfs(root)