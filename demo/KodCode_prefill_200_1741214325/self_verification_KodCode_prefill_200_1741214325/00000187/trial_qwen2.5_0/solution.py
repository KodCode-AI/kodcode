def floyd_warshall(graph):
    """
    Finds and returns the shortest paths between all pairs of vertices using Floyd-Warshall algorithm.
    :param graph: List[List[int]], where graph[i][j] is the weight of the edge from vertex i to vertex j.
                  If there is no direct edge, graph[i][j] should be None.
    :return: List[List[int]], where res[i][j] is the length of the shortest path from vertex i to vertex j.
    """
    V = len(graph)
    res = [[graph[i][j] if graph[i][j] is not None else float('inf') for j in range(V)] for i in range(V)]
    
    for via in range(V):
        for start in range(V):
            for end in range(V):
                if res[start][end] > res[start][via] + res[via][end]:
                    res[start][end] = res[start][via] + res[via][end]
    return res