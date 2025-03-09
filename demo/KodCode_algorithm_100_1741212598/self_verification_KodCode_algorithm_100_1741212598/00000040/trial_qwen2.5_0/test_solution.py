from solution import *

import pytest
from solution import analyze_network_connections

def test_network_connections_example():
    connections = [(0, 1), (1, 2), (3, 4), (4, 5), (2, 6)]
    assert analyze_network_connections(connections) == 3

def test_single_connection():
    connections = [(0, 1)]
    assert analyze_network_connections(connections) == 1

def test_no_connections():
    connections = []
    assert analyze_network_connections(connections) == 10  # Assuming maximum nodes are 10 as given constraint 0 to 10^4

def test_complex_connections():
    connections = [(0, 1), (2, 3), (4, 5), (5, 6), (7, 8), (8, 7)]
    assert analyze_network_connections(connections) == 4

def test_duplicate_connections():
    connections = [(0, 1), (1, 0), (2, 3), (3, 2), (4, 5), (5, 4)]
    assert analyze_network_connections(connections) == 3

def test_strongly_connected_graph():
    connections = [(0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3)]
    assert analyze_network_connections(connections) == 1