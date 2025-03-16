class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mirror_tree(root: TreeNode) -> TreeNode:
    if root is None:
        return None
    mirrored = TreeNode(root.val)
    mirrored.left = mirror_tree(root.right)
    mirrored.right = mirror_tree(root.left)
    return mirrored