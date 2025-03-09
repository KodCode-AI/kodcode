from typing import List

def count_valid_sequences(root: 'TreeNode') -> int:
    """
    Returns the number of valid sequences of node values in a BST.
    """
    def dfs(node):
        if not node:
            return [0, 1]
        left = dfs(node.left)
        right = dfs(node.right)
        
        # Calculate the sum of left and right children's values
        left_sum = node.val + left[0]
        right_sum = node.val + right[0]
        
        # Count valid sequences for the current node
        if left[1] != 0 and right[1] != 0:
            count = 1
            for x in range(left[1]):
                if left[0][x] < left_sum and right_sum < right[0][x]:
                    count += 1
            return [left_sum, count]
        elif left[1] != 0:
            count = sum(1 for x in left[0] if x < left_sum)
            return [left_sum, count]
        elif right[1] != 0:
            count = sum(1 for x in right[0] if right_sum < x)
            return [right_sum, count]
        else:
            return [node.val, 1]

    return dfs(root)[1]