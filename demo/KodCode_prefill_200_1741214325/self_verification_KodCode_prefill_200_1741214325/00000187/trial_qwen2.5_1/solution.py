import numpy as np

def floyd_warshall(graph):
    """
    Finds the shortest paths between all pairs of vertices in a given directed graph using the Floyd Warshall algorithm.
    The graph is represented as an adjacency matrix where graph[i][j] is the weight of the edge from vertex i to vertex j.
    If there is no direct edge, graph[i][j] is set to np.inf.
    """
    # Copy the graph matrix as we will be modifying it
    dist = np.copy(graph)
    
    # Apply Floyd Warshall algorithm
    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist