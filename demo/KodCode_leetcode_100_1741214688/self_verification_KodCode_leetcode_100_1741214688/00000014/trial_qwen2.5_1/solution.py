class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_odd_parent_nodes(root):
    """
    Returns the sum of values of all nodes that have an odd-valued parent.
    If there are no such nodes, returns 0.
    """
    def dfs(node, is_odd):
        if node is None:
            return 0
        if is_odd and node.left:
            left_sum = node.left.val
        else:
            left_sum = dfs(node.left, node.val % 2 != 0)
        if is_odd and node.right:
            right_sum = node.right.val
        else:
            right_sum = dfs(node.right, node.val % 2 != 0)
        return left_sum + right_sum
    
    return dfs(root, root.val % 2 != 0)