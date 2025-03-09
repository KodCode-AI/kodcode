def max_road_importance(n, roads):
    """
    Assigns unique integer values to cities to maximize the sum of the values
    of the two cities connected by each road. Returns the maximum possible sum.
    """
    # Initialize adjacency list
    adj_list = [[] for _ in range(n)]
    for a, b in roads:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    # Sort cities by their degree in descending order
    cities = sorted(range(n), key=lambda x: len(adj_list[x]), reverse=True)
    
    # Assign city values
    values = list(range(1, n + 1))
    total_importance = 0
    for i, city in enumerate(cities):
        for neighbor in adj_list[city]:
            total_importance += values[i] + values[neighbor]
    
    return total_importance