from solution import *

from solution import detect_cycle

def test_digraph_with_cycle():
    # Example of a graph with a cycle: a -> b, b -> c, c -> a
    graph = {
        'a': ['b'],
        'b': ['c'],
        'c': ['a'],
    }
    assert detect_cycle(graph) == True

def test_digraph_without_cycle():
    # Example of a graph without a cycle: a -> b, b -> c
    graph = {
        'a': ['b'],
        'b': ['c'],
    }
    assert detect_cycle(graph) == False

def test_digraph_single_node():
    # Single node graph should not contain a cycle
    graph = {
        'a': [],
    }
    assert detect_cycle(graph) == False

def test_digraph_complex_cycle():
    # Example of a graph with a different cycle: a -> b, b -> c, c -> d, d -> a
    graph = {
        'a': ['b'],
        'b': ['c'],
        'c': ['d'],
        'd': ['a'],
    }
    assert detect_cycle(graph) == True

def test_digraph_complex_no_cycle():
    # Example of a graph without any cycles: a -> b, b -> c, c -> d
    graph = {
        'a': ['b'],
        'b': ['c'],
        'c': ['d'],
    }
    assert detect_cycle(graph) == False