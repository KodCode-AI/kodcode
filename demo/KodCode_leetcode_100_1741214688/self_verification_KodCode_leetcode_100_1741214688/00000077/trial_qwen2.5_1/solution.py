from collections import defaultdict
from math import gcd

def are_coprime(a, b):
    return gcd(a, b) == 1

def find_max_coprime_components(values, edges):
    """
    Returns the node that, when removed, results in the maximum number of connected components with coprime values.
    """
    if not values or not edges:
        return -1
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    def dfs(node, parent):
        subtree_values = {values[node]}
        for child in graph[node]:
            if child != parent:
                subtree_values.add(values[child])
                subtree_values |= dfs(child, node)
        return subtree_values
    
    n = len(values)
    node_tuple = [(-1, -1)] * n
    for i in range(n):
        subtree = dfs(i, -1)
        coprime_pairs = sum(1 for x in subtree for y in subtree if x != y and are_coprime(x, y))
        node_tuple[i] = (coprime_pairs, i)
    
    node_tuple.sort(reverse=True)
    return node_tuple[0][1] if node_tuple[0][0] > 0 else -1