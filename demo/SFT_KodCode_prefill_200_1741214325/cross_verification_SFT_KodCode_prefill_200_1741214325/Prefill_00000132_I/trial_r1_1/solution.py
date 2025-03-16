class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def diameterOfBinaryTree(root):
    if not root:
        return 0
    max_diameter = [1]  # Stores the maximum number of nodes in the longest path

    def depth(node):
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        current = left + right + 1
        if current > max_diameter[0]:
            max_diameter[0] = current
        return max(left, right) + 1

    depth(root)
    return max_diameter[0] - 1  # Convert to number of edges