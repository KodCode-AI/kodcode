class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def diameterOfBinaryTree(root):
    max_nodes = [0]  # Using a list to allow modification inside nested function

    def helper(node):
        if node is None:
            return 0
        left = helper(node.left)
        right = helper(node.right)
        # Calculate the diameter through the current node
        current = left + right + 1
        if current > max_nodes[0]:
            max_nodes[0] = current
        # Return the height of the subtree rooted at this node (number of nodes)
        return 1 + max(left, right)
    
    if not root:
        return 0
    helper(root)
    # The diameter is the maximum number of nodes minus one (convert to edges)
    return max_nodes[0] - 1 if max_nodes[0] > 0 else 0