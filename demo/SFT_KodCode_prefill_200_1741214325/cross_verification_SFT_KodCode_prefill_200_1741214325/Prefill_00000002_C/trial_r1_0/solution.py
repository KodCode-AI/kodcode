class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def max_depth_bst(root: TreeNode) -> int:
    if root is None:
        return 0
    left_depth = max_depth_bst(root.left)
    right_depth = max_depth_bst(root.right)
    return 1 + max(left_depth, right_depth)