class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_left_leaves(root: TreeNode) -> int:
    """
    Returns the sum of all left leaves in the binary tree.
    """
    if not root:
        return 0

    def dfs(node, is_left):
        if not node.left and not node.right:
            return node.val if is_left else 0
        left_sum = 0
        if node.left:
            left_sum += dfs(node.left, True)
        if node.right:
            left_sum += dfs(node.right, False)
        return left_sum

    return dfs(root, False)