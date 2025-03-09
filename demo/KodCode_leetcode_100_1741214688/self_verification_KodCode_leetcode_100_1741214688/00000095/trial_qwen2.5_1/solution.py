class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def can_partition_bst(root: TreeNode) -> bool:
    """
    Determines if a binary search tree with unique values from 1 to n can be partitioned into two subsets
    with equal sum.
    """
    total_sum = 0
    subset_sums = set()

    def inorder_traverse(node: TreeNode):
        nonlocal total_sum
        if not node:
            return
        inorder_traverse(node.left)
        total_sum += node.val
        inorder_traverse(node.right)

    def find_partition(current_sum: int, target: int, node: TreeNode):
        if not node:
            return False
        if current_sum + node.val == target:
            return True
        if find_partition(current_sum + node.val, target, node.left):
            return True
        if find_partition(current_sum + node.val, target, node.right):
            return True
        return False

    inorder_traverse(root)
    half_sum = total_sum / 2
    return find_partition(0, half_sum, root)