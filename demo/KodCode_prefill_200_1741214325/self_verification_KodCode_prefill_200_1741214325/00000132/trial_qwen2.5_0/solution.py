class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(root: TreeNode) -> int:
    """
    Returns the diameter of the binary tree.
    """
    def height(node: TreeNode) -> int:
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))
    
    if not root:
        return 0
    max_diameter = 0
    def dfs(node: TreeNode) -> int:
        nonlocal max_diameter
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        max_diameter = max(max_diameter, left_height + right_height)
        return 1 + max(left_height, right_height)
    
    dfs(root)
    return max_diameter