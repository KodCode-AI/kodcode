class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: TreeNode, k: int) -> int:
    """
    Find the kth smallest element in a binary search tree without modifying the tree.
    """
    def inorder(node: TreeNode):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    return inorder(root)[k - 1]