from collections import defaultdict

def dfs visit(graph, node, visited, rec_stack):
    """
    Helper function to detect cycle using DFS.
    :param graph: Directed graph represented as adjacency list.
    :param node: Current node being processed.
    :param visited: Set of visited nodes.
    :param rec_stack: Stack to keep track of nodes in the current recursion.
    :return: True if cycle is detected, False otherwise.
    """
    if node in rec_stack:
        # Node is in recursion stack, cycle is detected.
        return True
    if node in visited:
        # Node is already visited, no need to explore further.
        return False

    # Mark current node as visited and add to recursion stack.
    visited.add(node)
    rec_stack.add(node)

    # Recur for all the vertices adjacent to this node.
    for neighbor in graph[node]:
        if dfs visit(graph, neighbor, visited, rec_stack):
            return True

    # Remove the node from recursion stack.
    rec_stack.remove(node)
    return False

def detect_cycle(graph):
    """
    Returns True if a cycle is detected in the directed graph, False otherwise.
    :param graph: Directed graph represented as adjacency list.
    :return: True if cycle is detected, False otherwise.
    """
    visited = set()
    rec_stack = set()
    for node in graph:
        if dfs visit(graph, node, visited, rec_stack):
            return True
    return False