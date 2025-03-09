class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i, n = 1, len(lst)
    while i < n:
        node = queue.pop(0)
        if i < n:
            node.left = TreeNode(lst[i]) if lst[i] is not None else None
            queue.append(node.left)
            i += 1
            if i < n and lst[i] is not None:
                node.right = TreeNode(lst[i])
                queue.append(node.right)
                i += 1
    return root

def find_node(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)

def find_lca(root, p, q):
    if not root:
        return None
    if root.val == p.val or root.val == q.val:
        return root
    left_lca = find_lca(root.left, p, q)
    right_lca = find_lca(root.right, p, q)
    if left_lca and right_lca:
        return root
    return left_lca if left_lca else right_lca

def lca_in_binary_tree(tree_str, queries):
    tree = build_tree_from_list(tree_str)
    results = []
    for p_val, q_val in queries:
        p_node = find_node(tree, p_val)
        q_node = find_node(tree, q_val)
        if not p_node or not q_node:
            results.append(-1)
        else:
            lca_node = find_lca(tree, p_node, q_node)
            results.append(lca_node.val)
    return results