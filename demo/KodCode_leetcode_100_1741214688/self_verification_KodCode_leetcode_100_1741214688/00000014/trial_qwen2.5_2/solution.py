from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sum_of_odd_parent_nodes(root):
    """
    Returns the sum of values of all nodes that have an odd-valued parent.
    """
    if not root:
        return 0
    
    queue = deque([(root, None)])  # (node, parent)
    total_sum = 0
    
    while queue:
        node, parent = queue.popleft()
        
        if parent and parent.val % 2 != 0:
            total_sum += node.val
        
        if node.left:
            queue.append((node.left, node))
        if node.right:
            queue.append((node.right, node))
    
    return total_sum