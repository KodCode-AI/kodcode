from collections import defaultdict

def dfs(graph, current_node, visited, recursion_stack):
    """
    Returns True if a cycle is detected in the graph using DFS.
    """
    visited[current_node] = True
    recursion_stack[current_node] = True

    # Check all the adjacent nodes
    for neighbor in graph[current_node]:
        if not visited[neighbor]:
            if dfs(graph, neighbor, visited, recursion_stack):
                return True
        elif recursion_stack[neighbor]:
            return True

    recursion_stack[current_node] = False
    return False

def detect_cycle_in_directed_graph(graph):
    """
    Returns True if the graph contains a cycle.
    """
    num_nodes = len(graph)
    visited = [False] * num_nodes
    recursion_stack = [False] * num_nodes

    for node in range(num_nodes):
        if not visited[node]:
            if dfs(graph, node, visited, recursion_stack):
                return True

    return False