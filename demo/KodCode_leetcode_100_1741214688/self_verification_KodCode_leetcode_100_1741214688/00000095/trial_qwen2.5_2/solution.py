from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def can_partition_bst(root: TreeNode) -> bool:
    """
    Determine if a BST can be partitioned into two subsets with equal sum.
    """
    def sum_of_bst(root: TreeNode) -> int:
        if not root:
            return 0
        return root.val + sum_of_bst(root.left) + sum_of_bst(root.right)
    
    total_sum = sum_of_bst(root)
    if total_sum % 2 != 0:
        return False
    
    target = total_sum // 2
    visited = set()

    def dfs(node: TreeNode, current_sum: int) -> bool:
        if not node:
            return False
        if current_sum == target and node not in visited:
            return True
        visited.add(node)
        return dfs(node.left, current_sum + node.val) or dfs(node.right, current_sum + node.val)
    
    return dfs(root, 0)