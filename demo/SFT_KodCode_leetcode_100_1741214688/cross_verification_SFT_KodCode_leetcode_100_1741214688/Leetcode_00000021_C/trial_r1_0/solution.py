class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def kth_smallest(root: TreeNode, k: int) -> int:
    elements = []
    
    def in_order(node):
        if not node:
            return
        in_order(node.left)
        elements.append(node.val)
        in_order(node.right)
    
    in_order(root)
    
    return elements[k-1]