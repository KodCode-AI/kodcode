class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def insert(self, key):
        if self.key:
            if key < self.key:
                if self.left is None:
                    self.left = TreeNode(key)
                else:
                    self.left.insert(key)
            elif key > self.key:
                if self.right is None:
                    self.right = TreeNode(key)
                else:
                    self.right.insert(key)
        else:
            self.key = key


def mirror_tree(root):
    """
    Returns the mirror image of a binary tree by swapping the left and right children of every node.
    """
    if root is not None:
        # Swap the left and right children
        root.left, root.right = root.right, root.left
        # Recursively call the function for the left subtree
        mirror_tree(root.left)
        # Recursively call the function for the right subtree
        mirror_tree(root.right)