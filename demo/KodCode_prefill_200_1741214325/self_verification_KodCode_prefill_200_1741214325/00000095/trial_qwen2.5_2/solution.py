class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def path_sum(root, targetSum):
    """
    Returns all root-to-leaf paths where the sum of the path equals the target sum.
    """
    def dfs(node, path, pathList):
        if not node:
            return
        path.append(node.val)
        if not node.left and not node.right and sum(path) == targetSum:
            pathList.append(path.copy())
        dfs(node.left, path, pathList)
        dfs(node.right, path, pathList)
        path.pop()

    result = []
    dfs(root, [], result)
    return result