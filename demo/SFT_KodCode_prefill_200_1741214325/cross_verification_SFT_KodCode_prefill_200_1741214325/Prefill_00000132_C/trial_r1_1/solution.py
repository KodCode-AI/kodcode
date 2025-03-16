class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

def diameter_of_binary_tree(root: TreeNode) -> int:
    if not root:
        return 0
    
    max_diameter = [0]  # Using a list to allow modifying the variable inside nested function
    
    def helper(node):
        if not node:
            return 0
        left_depth = helper(node.left)
        right_depth = helper(node.right)
        current_diameter = left_depth + right_depth
        if current_diameter > max_diameter[0]:
            max_diameter[0] = current_diameter
        return max(left_depth, right_depth) + 1
    
    helper(root)
    return max_diameter[0]