from solution import *

import numpy as np
from solution import floyd_warshall

def test_floyd_warshall_empty_graph():
    graph = np.array([[np.inf, 2, np.inf], [np.inf, np.inf, 3], [4, np.inf, np.inf]])
    expected = np.array([[np.inf, 2, 5], [np.inf, np.inf, 3], [4, np.inf, np.inf]])
    assert np.array_equal(floyd_warshall(graph), expected)

def test_floyd_warshall_single_node_graph():
    graph = np.array([[0]])
    expected = np.array([[0]])
    assert np.array_equal(floyd_warshall(graph), expected)

def test_floyd_warshall_no_negative_cycle():
    graph = np.array([[0, 5, 10], [np.inf, 0, 3], [1, np.inf, 0]])
    expected = np.array([[0, 5, 8], [4, 0, 3], [1, 6, 0]])
    assert np.array_equal(floyd_warshall(graph), expected)

def test_floyd_warshall_with_negative_cycle():
    graph = np.array([[0, -2, 1], [-1, 0, -1], [1, 1, 0]])
    expected = np.array([[0, -2, -1], [-1, 0, -1], [1, 1, 0]])
    assert np.array_equal(floyd_warshall(graph), expected)

def test_floyd_warshall_general_case():
    graph = np.array([[0, -2, 1, np.inf], [np.inf, 0, -1, 4], [np.inf, np.inf, 0, -1], [2, np.inf, np.inf, 0]])
    expected = np.array([[0, -2, -1, 1], [2, 0, -1, 3], [2, 1, 0, -1], [0, 2, 1, 0]])
    assert np.array_equal(floyd_warshall(graph), expected)