class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def max_depth_bst(root: TreeNode) -> int:
    if root is None:
        return 0
    return 1 + max(max_depth_bst(root.left), max_depth_bst(root.right))