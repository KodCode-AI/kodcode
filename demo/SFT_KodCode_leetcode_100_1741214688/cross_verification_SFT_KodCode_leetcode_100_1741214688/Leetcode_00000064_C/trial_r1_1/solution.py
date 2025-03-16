class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_in_bst(root: TreeNode, target: int) -> bool:
    """
    Searches for the target value in the BST and returns True if found, False otherwise.
    """
    if not root:
        return False
    if root.val == target:
        return True
    elif target < root.val:
        return find_in_bst(root.left, target)
    else:
        return find_in_bst(root.right, target)

def insert_in_bst(root: TreeNode, val: int) -> TreeNode:
    """
    Inserts a new node with given value into the BST.
    """
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_in_bst(root.left, val)
    elif val > root.val:
        root.right = insert_in_bst(root.right, val)
    # Do not insert duplicate values
    return root