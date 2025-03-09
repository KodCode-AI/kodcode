class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(root: TreeNode) -> int:
    """
    Returns the diameter of a binary tree.
    """
    def height(node):
        if not node:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        nonlocal diameter
        diameter = max(diameter, left_height + right_height)
        return max(left_height, right_height) + 1

    diameter = 0
    height(root)
    return diameter