# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sum_numbers(root):
    """
    Returns the sum of all root-to-leaf numbers in the binary tree.
    """
    return _sum_numbers(root, 0)
    
def _sum_numbers(node, current_number):
    if not node:
        return 0
    current_number = current_number * 10 + node.val
    if not node.left and not node.right:  # It's a leaf node
        return current_number
    return _sum_numbers(node.left, current_number) + _sum_numbers(node.right, current_number)