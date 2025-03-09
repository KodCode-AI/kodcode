class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def height(node):
    """
    Returns the height of the given node.
    """
    if node is None:
        return -1
    return 1 + max(height(node.left), height(node.right))

def balance_factor(node):
    """
    Returns the balance factor of the given node.
    """
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return abs(left_height - right_height)

def min_balance_factor(root):
    """
    Returns the minimum balance factor of all nodes in the tree.
    """
    if root is None:
        return 0
    min_factor = [balance_factor(root)]
    stack = [root]
    while stack:
        node = stack.pop()
        if node.left:
            min_factor.append(balance_factor(node.left))
            stack.append(node.left)
        if node.right:
            min_factor.append(balance_factor(node.right))
            stack.append(node.right)
    return min(min_factor)

# Example tree creation
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4))
root.right = TreeNode(3)

# Function call to get the minimum balance factor
result = min_balance_factor(root)
print(result)  # Expected output: 0