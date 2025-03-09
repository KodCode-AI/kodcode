class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_path_sum(root: TreeNode) -> int:
    """
    Returns the minimal path sum from the root to any leaf node in the binary tree.
    """
    if not root:
        return 0
    stack = [(root, root.val)]
    min_sum = float('inf')
    
    while stack:
        node, current_sum = stack.pop()
        if not node.left and not node.right:
            min_sum = min(min_sum, current_sum)
        if node.left:
            stack.append((node.left, current_sum + node.left.val))
        if node.right:
            stack.append((node.right, current_sum + node.right.val))
    return min_sum