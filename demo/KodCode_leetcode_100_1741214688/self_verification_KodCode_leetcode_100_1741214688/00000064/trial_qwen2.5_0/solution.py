class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_in_bst(root: TreeNode, target: int) -> bool:
    """
    Returns True if the target is found in the BST, False otherwise.
    """
    current = root
    while current:
        if current.val == target:
            return True
        elif target < current.val:
            current = current.left
        else:
            current = current.right
    return False

def insert_into_bst(root: TreeNode, val: int) -> TreeNode:
    """
    Inserts a new node with the given value into the BST while maintaining its properties.
    """
    if not root:
        return TreeNode(val)
    
    current = root
    while True:
        if val < current.val:
            if current.left is None:
                current.left = TreeNode(val)
                break
            current = current.left
        else:
            if current.right is None:
                current.right = TreeNode(val)
                break
            current = current.right
    return root