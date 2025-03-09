from collections import defaultdict

def has_cycle_dfs(graph, vertex, visited, rec_stack):
    """
    This function uses Depth First Search to detect if there is a cycle in a directed graph.
    It uses a dictionary to store visited and recursion stack status for each vertex.
    :param graph: adjacency list representation of the graph
    :param vertex: current vertex
    :param visited: set of visited vertices
    :param rec_stack: set to keep track of vertices in the current recursion stack
    :return: True if a cycle is detected, False otherwise
    """
    visited[vertex] = True
    rec_stack[vertex] = True

    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            if has_cycle_dfs(graph, neighbor, visited, rec_stack):
                return True
        elif rec_stack[neighbor]:
            return True

    rec_stack[vertex] = False
    return False

def detect_cycle(graph):
    """
    Returns True if the graph contains a cycle, False otherwise.
    """
    visited = defaultdict(bool)
    rec_stack = defaultdict(bool)

    for node in graph:
        if not visited[node]:
            if has_cycle_dfs(graph, node, visited, rec_stack):
                return True

    return False