class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_in_bst(root: TreeNode, target: int) -> bool:
    """
    Searches for the target value in the BST and returns True if found, False otherwise.
    """
    if root is None:
        return False
    if target == root.val:
        return True
    elif target < root.val:
        return find_in_bst(root.left, target)
    else:
        return find_in_bst(root.right, target)

def insert_in_bst(root: TreeNode, val: int) -> TreeNode:
    """
    Inserts a new node with given value into the BST.
    """
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_in_bst(root.left, val)
    elif val > root.val:
        root.right = insert_in_bst(root.right, val)
    return root