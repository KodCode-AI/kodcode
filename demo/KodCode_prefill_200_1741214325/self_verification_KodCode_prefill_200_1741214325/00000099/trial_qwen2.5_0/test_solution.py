from solution import *

from solution import detect_cycle_in_directed_graph

def create_graph(edges):
    """
    Helper function to create a graph from a list of edges.
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    return graph

def test_empty_graph():
    assert not detect_cycle_in_directed_graph(create_graph([]))

def test_directed_cycle():
    assert detect_cycle_in_directed_graph(create_graph([(0, 1), (1, 2), (2, 0)]))

def test_cyclic_graph():
    assert detect_cycle_in_directed_graph(create_graph([(0, 1), (1, 3), (3, 2), (2, 0), (2, 4), (4, 2)]))

def test_non_cyclic_graph():
    assert not detect_cycle_in_directed_graph(create_graph([(1, 2), (3, 4)]))
    
def test_self_loop():
    assert detect_cycle_in_directed_graph(create_graph([(0, 0)]))
    
def test_chain():
    assert not detect_cycle_in_directed_graph(create_graph([(0, 1), (1, 2), (2, 3)]))