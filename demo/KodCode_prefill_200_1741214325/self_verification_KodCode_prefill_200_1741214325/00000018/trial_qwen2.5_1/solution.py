class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minimal_path_sum(root: TreeNode) -> int:
    """
    Returns the minimal path sum from top to bottom in a binary tree.
    """
    def dfs(node):
        if not node:
            return 0, float('inf')
        if not node.left and not node.right:
            return 1, node.val
        left_depth, left_sum = dfs(node.left)
        right_depth, right_sum = dfs(node.right)
        current_depth = max(left_depth, right_depth) + 1
        current_sum = min(left_sum, right_sum) + node.val
        return current_depth, current_sum
    
    _, result = dfs(root)
    return result