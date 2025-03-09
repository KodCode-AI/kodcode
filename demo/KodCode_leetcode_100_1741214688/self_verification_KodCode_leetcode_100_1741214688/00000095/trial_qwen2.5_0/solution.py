class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def can_partition_bst(root: TreeNode) -> bool:
    """
    Returns true if the tree can be partitioned into two subsets with equal sum.
    """
    total_sum = sum_node_values(root)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    return can_partition_helper(root, target)

def sum_node_values(node: TreeNode) -> int:
    if node is None:
        return 0
    return node.val + sum_node_values(node.left) + sum_node_values(node.right)

def can_partition_helper(node: TreeNode, target: int) -> bool:
    if node is None:
        return target == 0
    return (can_partition_helper(node.left, target - node.val) or 
            can_partition_helper(node.right, target - node.val))