def assign_values(n, roads):
    """
    Assigns each city a unique value from 1 to n to maximize the sum of the values
    of the two cities connected by each road. Returns the maximum possible sum.
    """
    # Create a graph representation
    graph = [[] for _ in range(n)]
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(city, values, visited):
        visited[city] = True
        value = n - len(graph[city])
        for neighbor in graph[city]:
            if not visited[neighbor]:
                value += dfs(neighbor, values, visited)
        values.append(value)
        return value
    
    # Perform DFS to assign values
    values = []
    for i in range(n):
        if not values:
            dfs(i, values, [False] * n)
    
    # Sort values in descending order
    values.sort(reverse=True)
    
    # Calculate the result
    max_sum = 0
    for i in range(n):
        max_sum += (n + 1 - i) * values[i]
    
    return max_sum