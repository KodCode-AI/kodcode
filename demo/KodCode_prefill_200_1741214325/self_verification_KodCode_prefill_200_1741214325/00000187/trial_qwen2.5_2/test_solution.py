from solution import *

import numpy as np

def test_floyd_warshall():
    # Create a sample adjacency matrix with an infinity indicating no direct edge
    graph = np.array([
        [0, 3, inf, inf],
        [inf, 0, 1, 7],
        [inf, inf, 0, inf],
        [inf, inf, 2, 0]
    ])
    # Expected output after applying Floyd-Warshall algorithm
    expected_output = np.array([
        [0, 3, 4, 11],
        [inf, 0, 1, 8],
        [inf, inf, 0, 3],
        [inf, inf, 2, 0]
    ])
    # Convert inf to np.inf for comparison
    graph[np.isinf(graph)] = np.inf
    expected_output[np.isinf(expected_output)] = np.inf
    # Run the Floyd-Warshall algorithm
    output = floyd_warshall(graph)
    # Check if the output matches the expected output
    assert np.array_equal(output, expected_output)

def test_floyd_warshall_empty():
    # An empty graph
    graph = np.array([[]])
    output = floyd_warshall(graph)
    assert output == graph

def test_floyd_warshall_single_node():
    # A single node graph
    graph = np.array([[0]])
    output = floyd_warshall(graph)
    assert output == graph