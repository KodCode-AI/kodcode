from solution import *

def test_floyd_warshall():
    graph = [
        [0, 3, float('inf'), 7],
        [8, 0, 2, float('inf')],
        [5, float('inf'), 0, 1],
        [2, float('inf'), float('inf'), 0]
    ]
    expected_result = [
        [0, 3, 5, 7],
        [8, 0, 2, 4],
        [5, 7, 0, 1],
        [2, 7, 6, 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected_result

def test_floyd_warshall_with_suboptimal_paths():
    graph = [
        [0, 2, 1],
        [float('inf'), 0, 4],
        [float('inf'), float('inf'), 0]
    ]
    expected_result = [
        [0, 2, 1],
        [3, 0, 3],
        [4, 5, 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected_result

def test_floyd_warshall_all_positive_edges():
    graph = [
        [0, 3, 1],
        [1, 0, 1],
        [2, 2, 0]
    ]
    expected_result = [
        [0, 3, 2],
        [2, 0, 1],
        [2, 2, 0]
    ]
    result = floyd_warshall(graph)
    assert result == expected_result

def test_floyd_warshall_empty_graph():
    graph = [[]]
    expected_result = [[0]]
    result = floyd_warshall(graph)
    assert result == expected_result

def test_floyd_warshall_single_vertex():
    graph = [[0]]
    expected_result = [[0]]
    result = floyd_warshall(graph)
    assert result == expected_result