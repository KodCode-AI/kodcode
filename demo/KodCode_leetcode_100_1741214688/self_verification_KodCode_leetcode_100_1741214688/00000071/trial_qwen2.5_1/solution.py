def max_road_importance(n, roads):
    """
    Assigns each city a unique integer value from 1 to n such that the sum of the values of the two cities
    connected by each road is maximized, and returns the maximum possible sum of the importance of all roads.
    """
    degree = [0] * n
    for a, b in roads:
        degree[a] += 1
        degree[b] += 1
    cities = sorted(range(n), key=lambda i: -degree[i])
    values = {cities[i]: i + 1 for i in range(n)}
    
    max_sum = 0
    for a, b in roads:
        max_sum += values[a] + values[b]
    
    return max_sum