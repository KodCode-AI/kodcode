class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root: TreeNode, k: int) -> int:
    """
    Returns the kth smallest element in the given binary search tree.
    """
    def inorder_traversal(node: TreeNode):
        return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right) if node else []
    
    return inorder_traversal(root)[k-1]