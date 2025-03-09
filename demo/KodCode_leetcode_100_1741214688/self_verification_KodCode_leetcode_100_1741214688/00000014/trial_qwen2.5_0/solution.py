class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_odd_parent_nodes(root: TreeNode) -> int:
    """
    Returns the sum of values of all nodes that have an odd-valued parent.
    If there are no such nodes, returns 0.
    """
    def dfs(node: TreeNode, is_odd_parent: bool) -> int:
        if not node:
            return 0
        if is_odd_parent:
            return node.val + dfs(node.left, node.val % 2 != 0) + dfs(node.right, node.val % 2 != 0)
        else:
            return dfs(node.left, node.val % 2 != 0) + dfs(node.right, node.val % 2 != 0)
    return dfs(root, root.val % 2 != 0)