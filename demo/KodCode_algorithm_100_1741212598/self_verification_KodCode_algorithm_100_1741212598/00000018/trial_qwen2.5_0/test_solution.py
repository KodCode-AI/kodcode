from solution import *

import numpy as np
from solution import find_closest_document

def test_find_closest_document():
    dataset = np.array([[1, 2], [3, 4], [5, 6]])
    query_document = np.array([4, 5])
    assert find_closest_document(dataset, query_document) == (1, 1.0)

    dataset = np.array([[10, 20], [30, 40], [50, 60]])
    query_document = np.array([45, 55])
    assert find_closest_document(dataset, query_document) == (1, 5.0)

    dataset = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    query_document = np.array([5, 5, 5])
    assert find_closest_document(dataset, query_document) == (1, 2.0)

    dataset = np.array([[0, 0], [1, 1]])
    query_document = np.array([1, 1])
    assert find_closest_document(dataset, query_document) == (1, 0.0)

    dataset = np.array([[2, 3], [4, 5], [6, 7]])
    query_document = np.array([7, 8])
    assert find_closest_document(dataset, query_document) == (2, 1.4142135623730951)

test_find_closest_document()