from solution import *

import pytest

def test_analyze_network_connections():
    connections = [(0, 1), (1, 2), (3, 4), (4, 5), (2, 6)]
    assert analyze_network_connections(connections) == 3

def test_single_connections():
    connections = [(0, 1), (2, 3)]
    assert analyze_network_connections(connections) == 2

def test_multiple_clusters():
    connections = [(0, 1), (1, 2), (3, 4), (4, 5), (6, 7), (2, 9)]
    assert analyze_network_connections(connections) == 5

def test_self_connections():
    connections = [(0, 0), (1, 1), (2, 2)]
    assert analyze_network_connections(connections) == 3

def test_no_connections():
    connections = []
    assert analyze_network_connections(connections) == 10001  # Assuming 0 to 10000 nodes

def test_overlapping_connections():
    connections = [(0, 1), (1, 2), (0, 2), (3, 4), (4, 5), (5, 6)]
    assert analyze_network_connections(connections) == 3