from collections import defaultdict, deque

def build_tree(level_order):
    if not level_order:
        return None
    root = TreeNode(level_order[0][0])
    parent_dict = defaultdict(TreeNode)
    parent_dict[None] = None
    queue = deque([root])
    for level in level_order[1:]:
        while queue and len(queue[0].children) == len(level):
            queue.popleft()
        while queue:
            parent = queue[0]
            for val in level:
                if val:
                    node = TreeNode(val)
                    parent.children.append(node)
                    parent_dict[val] = parent
                    if len(parent.children) == len(level):
                        queue.popleft()
                        queue.append(node)
                else:
                    queue.popleft()
                    break
    return root, parent_dict

def find_node(node, val, parent_dict):
    if not node or not val in parent_dict:
        return None
    if node.val == val:
        return node
    for child in node.children:
        found = find_node(child, val, parent_dict)
        if found:
            return found
    return None

def lowest_common_ancestor(root, p, q, parent_dict):
    if not root or not p or not q:
        return -1
    if p.val == q.val:
        return p.val
    path_p = set()
    while p:
        path_p.add(p.val)
        p = parent_dict[p.val]
    while q:
        if q.val in path_p:
            return q.val
        q = parent_dict[q.val]
    return -1

def find_lca_in_tree(level_order, queries):
    root, parent_dict = build_tree(level_order)
    answers = []
    for query in queries:
        p = find_node(root, query[0], parent_dict)
        q = find_node(root, query[1], parent_dict)
        if not p or not q:
            answers.append(-1)
        else:
            answers.append(lowest_common_ancestor(root, p, q, parent_dict))
    return answers

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []

# Example:
level_order = [
    [1],
    [2, 3],
    [4, 5, 6, 7]
]
queries = [[4, 7], [3, 5]]

print(find_lca_in_tree(level_order, queries))