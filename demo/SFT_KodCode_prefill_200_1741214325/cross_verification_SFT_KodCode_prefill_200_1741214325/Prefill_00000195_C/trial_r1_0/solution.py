class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mirror_tree(root: TreeNode) -> TreeNode:
    if not root:
        return None
    new_root = TreeNode(root.val)
    new_root.left = mirror_tree(root.right)
    new_root.right = mirror_tree(root.left)
    return new_root