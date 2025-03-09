from collections import defaultdict
from math import gcd
from typing import List

def max_coprime_components(values: List[int], edges: List[List[int]]) -> int:
    """
    Finds the node whose removal leads to the maximum number of coprime components.
    """
    n = len(values)
    tree = defaultdict(list)
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)
    
    # Helper function to find the resulting components.
    def dfs(node: int, parent: int) -> List[List[int]]:
        result = [[node]]
        for child in tree[node]:
            if child != parent:
                for comp in dfs(child, node):
                    if any(gcd(values[node], values[x]) != 1 for x in comp):
                        # If the values are not coprime, only add the current node
                        result.append([node])
                    else:
                        # Otherwise, merge the component with the current node
                        result[-1].extend(comp)
        return result
    
    max_components = 0
    result_node = -1
    
    for node in range(n):
        components = dfs(node, -1)
        count = len(components)
        if count > max_components or (count == max_components and node < result_node):
            max_components, result_node = count, node
    
    return result_node