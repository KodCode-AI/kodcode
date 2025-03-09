from math import gcd
from collections import defaultdict

def is_coprime(a, b):
    return gcd(a, b) == 1

def dfs(tree, values, node, parent):
    children = tree[node].difference({parent})
    coprime_count = 1 if is_coprime(values[node], values[parent]) else 0
    coprime_children = coprime_count
    for child in children:
        coprime_children_, coprime_count_ = dfs(tree, values, child, node)
        coprime_children += coprime_children_
        coprime_count += coprime_count_
    return coprime_children, coprime_count

def max_coprime_components(edges, values, remove_node=None):
    n = len(values)
    tree = defaultdict(set)
    for u, v in edges:
        tree[u].add(v)
        tree[v].add(u)
    
    if remove_node is None:
        max_comp, max_count = 0, 0
        for i in range(n):
            coprime_children, coprime_count = dfs(tree, values, i, -1)
            if coprime_count > max_count or (coprime_count == max_count and i < max_comp):
                max_comp, max_count = i, coprime_count
        return max_comp if max_count > 0 else -1
    else:
        coprime_children, coprime_count = dfs(tree, values, remove_node, -1)
        return coprime_count

def find_node_for_max_components(values, edges):
    return max_coprime_components(edges, values)