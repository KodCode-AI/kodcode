class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_valid_sequences(root: TreeNode) -> int:
    """
    Returns the number of valid node value sequences in a binary search tree.
    """
    def traverse(node: TreeNode, prefix_sum: int, suffix_sum: int, min_val: int, max_val: int, is_valid: bool, memo):
        if not node:
            return 1 if is_valid else 0
        
        current_val = node.val
        new_prefix_sum = prefix_sum + current_val
        new_min_val = min_val
        new_max_val = max_val
        
        if (prefix_sum, suffix_sum, new_min_val, new_max_val, is_valid, current_val) in memo:
            return memo[(prefix_sum, suffix_sum, new_min_val, new_max_val, is_valid, current_val)]
        
        left_count = traverse(node.left, new_prefix_sum, suffix_sum + current_val, new_min_val, max(new_max_val, current_val), False, memo)
        right_count = traverse(node.right, prefix_sum + current_val, suffix_sum, current_val, max_val, False, memo)
        
        if current_val > prefix_sum and current_val < suffix_sum and new_min_val < current_val < new_max_val and is_valid:
            left_count += traverse(node.left, new_prefix_sum, suffix_sum + current_val, new_min_val, max(new_max_val, current_val), True, memo)
            right_count += traverse(node.right, prefix_sum + current_val, suffix_sum, current_val, max_val, True, memo)
        
        memo[(prefix_sum, suffix_sum, new_min_val, new_max_val, is_valid, current_val)] = left_count + right_count
        return left_count + right_count
    
    return traverse(root, 0, 0, float('-inf'), float('inf'), False, {})