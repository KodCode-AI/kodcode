class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_valid_sequences(root: TreeNode) -> int:
    """
    Returns the number of valid sequences in the binary search tree.
    """
    def dfs(node, previous_sum, next_sum, min_val, max_val):
        if not node:
            return 0
        if min_val < node.val < next_sum and previous_sum < node.val < max_val:
            return 1 + dfs(node.left, previous_sum + node.val, next_sum, min_val, node.val) + dfs(node.right, previous_sum, next_sum + node.val, node.val, max_val)
        return 0

    return dfs(root, 0, 0, float('-inf'), float('inf'))