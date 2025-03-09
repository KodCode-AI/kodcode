class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def min_balance_factor(root):
    if not root:
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)
    current_balance = left_height - right_height
    
    left_min_balance = min_balance_factor(root.left)
    right_min_balance = min_balance_factor(root.right)
    
    return min(current_balance, left_min_balance, right_min_balance)