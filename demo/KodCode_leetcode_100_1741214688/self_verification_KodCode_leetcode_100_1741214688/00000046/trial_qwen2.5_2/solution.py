from collections import defaultdict

def build_tree(node_values):
    """
    Builds a tree from the given node_values, where each node has a unique value.
    :param node_values: List of lists representing the tree.
    :return: A dictionary where the key is the node value, and the value is the Node object.
    """
    # Assuming the tree is binary for simplicity, each node has at most two children
    tree = defaultdict(list)
    nodes = {value: i for i, value in enumerate(node_values[0]) if value is not None}
    root = nodes[1]

    for level in node_values[1:]:
        parent_i = 0
        for value in level:
            if value is not None:
                parent = node_values[parent_i][0] if parent_i in nodes else None
                child = nodes[value] if value in nodes else None
                tree[parent].append(child)
                tree[child].append(parent)
            parent_i += 1

    return tree, root

def find_path_from_root(tree, root, value):
    """
    Finds the path from the root to the node with the given value.
    :param tree: The tree structure.
    :param root: The root node value.
    :param value: The target node value.
    :return: A list of node values from root to the target node, or None if the node is not found.
    """
    stack = [(root, [root])]
    while stack:
        node, path = stack.pop()
        if node == value:
            return path
        for child in tree[node]:
            if child in path:
                continue
            stack.append((child, path + [child]))
    return None

def lowest_common_ancestor(tree, path1, path2):
    """
    Finds the LCA of two paths.
    :param tree: The tree structure.
    :param path1: Path from root to the first node.
    :param path2: Path from root to the second node.
    :return: The LCA node value, or -1 if either node does not exist in the tree.
    """
    for i in range(min(len(path1), len(path2))):
        if path1[i] != path2[i]:
            return path1[i-1]
    return path1[len(path1) - 1] if len(path1) > len(path2) else path2[len(path2) - 1]

def findLCA(query, node_values):
    """
    Finds the LCA for each query.
    :param query: A list of queries.
    :param node_values: List of lists representing the tree.
    :return: A list of LCA node values for each query.
    """
    tree, root = build_tree(node_values)
    results = []
    for start, dest in query:
        if start in tree and dest in tree:
            path_start = find_path_from_root(tree, root, start)
            path_dest = find_path_from_root(tree, root, dest)
            results.append(lowest_common_ancestor(tree, path_start, path_dest))
        else:
            results.append(-1)
    return results