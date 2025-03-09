class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findClosestLeaf(root: TreeNode, target: int) -> int:
    """
    Finds the value of the closest leaf node to the target in a binary search tree.
    """
    from collections import deque
    
    def dfs(node):
        if not node:
            return None
        if node.val == target:
            return node, 0
        left_result, left_dist = dfs(node.left)
        right_result, right_dist = dfs(node.right)
        if left_result:
            return left_result, left_dist + 1
        if right_result:
            return right_result, right_dist + 1
        return None, None
    
    closest_leaf, _ = dfs(root)
    if closest_leaf:
        closest_leaf_queue = deque([closest_leaf])
        while closest_leaf_queue:
            current = closest_leaf_queue.popleft()
            if not current.left and not current.right:
                return current.val
            if current.left:
                closest_leaf_queue.append(current.left)
            if current.right:
                closest_leaf_queue.append(current.right)
    return -1  # If target is not found