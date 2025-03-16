class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(root: TreeNode) -> int:
    max_diameter = 0

    def helper(node):
        nonlocal max_diameter
        if node is None:
            return 0
        left_depth = helper(node.left)
        right_depth = helper(node.right)
        current_diameter = left_depth + right_depth
        if current_diameter > max_diameter:
            max_diameter = current_diameter
        return 1 + max(left_depth, right_depth)

    helper(root)
    return max_diameter