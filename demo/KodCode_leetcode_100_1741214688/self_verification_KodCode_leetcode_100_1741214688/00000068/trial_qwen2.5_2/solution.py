class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(node):
    """
    Returns the height of the given tree node.
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

def find_min_balance_factor(root):
    """
    Traverses the tree to find the minimum balance factor of all nodes.
    """
    min_bal = 0
    stack = [root]
    visited = set()
    while stack:
        cur_node = stack.pop()
        if cur_node not in visited:
            visited.add(cur_node)
            min_bal = min(min_bal, balance_factor(cur_node))
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
    return min_bal