class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
    """
    Returns the sum of values of all nodes in the BST with values in the range [low, high].
    """
    if root is None:
        return 0
    
    sum_ = 0
    if root.val >= low and root.val <= high:
        sum_ += root.val
    if root.val > low:
        sum_ += rangeSumBST(root.left, low, high)
    if root.val < high:
        sum_ += rangeSumBST(root.right, low, high)
    
    return sum_