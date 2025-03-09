class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    """
    Returns the k-th smallest element in a binary search tree.
    """
    def inorder_traversal(node):
        return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right) if node else []
    
    return inorder_traversal(root)[k-1]