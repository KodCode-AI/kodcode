from collections import defaultdict, deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def vertical_order(root):
    """
    Returns the vertical order traversal of its nodes' values.
    """
    if not root:
        return []
    
    column_table = defaultdict(list)
    queue = deque([(root, 0)])  # (node, column_index)
    min_col = 0
    max_col = 0
    
    while queue:
        node, col = queue.popleft()
        if node:
            column_table[col].append(node.val)
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            queue.append((node.left, col - 1))
            queue.append((node.right, col + 1))
    
    return [column_table[i] for i in range(min_col, max_col + 1)]