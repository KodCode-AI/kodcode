To solve this problem, we need to traverse the BST and find the closest leaf node to the target. A leaf node is a node that has no children. The solution involves performing a BFS (Breadth-First Search) traversal starting from the root and tracking the distance to the target node. We stop at the first leaf node we encounter at the shallowest level that is closest to the target.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findClosestLeaf(root: TreeNode, target: int) -> int:
    from collections import deque
    
    if not root:
        return None
    
    queue = deque([root])
    target_node = None
    level = 0
    
    while queue:
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.popleft()
            
            if node.val == target:
                target_node = node
                break
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        if target_node:
            break
    
    # When target_node is found, perform a BFS to find the closest leaf node
    if target_node:
        queue = deque([target_node])
        visited = set([target_node])
        
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                node = queue.popleft()
                
                if not node.left and not node.right:  # node is a leaf
                    return node.val
                
                if node.left and node.left not in visited:
                    queue.append(node.left)
                    visited.add(node.left)
                
                if node.right and node.right not in visited:
                    queue.append(node.right)
                    visited.add(node.right)

# Example usage
# Constructing a simple BST for testing
#         3
#        / \
#       1   4
#          / \
#         2   5
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4, TreeNode(2), TreeNode(5))

# Find the closest leaf node to the target value 3
print(findClosestLeaf(root, 3))  # Output: 4