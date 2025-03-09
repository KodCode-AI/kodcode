from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_order(root):
    """
    Returns the vertical order traversal of the tree nodes' values.
    """
    if not root:
        return []
    
    column_table = defaultdict(list)
    queue = deque([(root, 0)])  # (node, column_index)
    
    while queue:
        node, column_index = queue.popleft()
        column_table[column_index].append(node.val)
        
        if node.left:
            queue.append((node.left, column_index - 1))
        if node.right:
            queue.append((node.right, column_index + 1))
    
    # Sort column keys and then return the nodes in the order of columns
    return [column_table[k] for k in sorted(column_table)]