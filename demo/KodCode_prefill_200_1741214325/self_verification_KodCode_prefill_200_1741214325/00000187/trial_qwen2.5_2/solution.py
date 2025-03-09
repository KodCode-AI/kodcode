def floyd_warshall(graph):
    """
    Function to implement Floyd-Warshall algorithm to find the shortest paths between all pairs of vertices.
    The graph should be represented as an adjacency matrix, where graph[i][j] represents the weight of the edge
    from vertex i to vertex j. If there is no edge, graph[i][j] should be infinity.
    """
    V = len(graph)  # Number of vertices
    # Adding the vertices separately
    for k in range(V):
        for i in range(V):
            for j in range(V):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph