from collections import defaultdict

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def vertical_order_traversal(root):
    """
    Returns the vertical order traversal of the tree nodes' values.
    """
    if not root:
        return []
    
    column_table = defaultdict(list)
    min_column = max_column = 0
    
    def dfs(node, row, column):
        nonlocal min_column, max_column
        if node:
            column_table[column].append((row, node.val))
            min_column = min(min_column, column)
            max_column = max(max_column, column)
            dfs(node.left, row + 1, column - 1)
            dfs(node.right, row + 1, column + 1)
    
    dfs(root, 0, 0)
    
    # Sort by row first, then by node value
    vertical_order_list = []
    for col in range(min_column, max_column + 1):
        column_table[col].sort(key=lambda x: x[0])
        vertical_order_list.append([val for row, val in column_table[col]])
    
    return vertical_order_list