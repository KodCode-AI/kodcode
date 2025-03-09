class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findClosestLeaf(root: TreeNode, target: int) -> int:
    closest_leaf_val = None
    min_distance = float('inf')
    
    def dfs(node):
        nonlocal closest_leaf_val, min_distance
        if not node:
            return 0, False

        left_distance, left_is_leaf = dfs(node.left)
        right_distance, right_is_leaf = dfs(node.right)
        
        if left_is_leaf and right_is_leaf:
            return min(left_distance, right_distance) + 1, False  # Node is an internal node
        elif not left_is_leaf and not right_is_leaf:
            return min(left_distance, right_distance) + 1, True
        else:
            distance = left_distance + right_distance + 1
            if distance < min_distance:
                min_distance = distance
                closest_leaf_val = node.val
            return min(left_distance, right_distance) + 1, False

        return 0, False

    dfs(root)
    return closest_leaf_val


This function performs a depth-first search (DFS) on the BST to find the closest leaf node to the target. It maintains the distance to the closest leaf node and updates it if a closer leaf is found. The function returns the value of the closest leaf node.