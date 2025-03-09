from solution import *

import numpy as np
from solution import find_closest_document

def test_find_closest_document():
    dataset = np.array([[1, 2], [3, 4], [5, 6]])
    query_document = np.array([4, 5])
    expected_index, expected_distance = 1, 1.0
    index, distance = find_closest_document(dataset, query_document)
    assert index == expected_index and np.isclose(distance, expected_distance)

def test_find_closest_document_with_negative_values():
    dataset = np.array([[1, 2], [-3, -4], [-5, -6]])
    query_document = np.array([-2, -3])
    expected_index, expected_distance = 1, 1.0
    index, distance = find_closest_document(dataset, query_document)
    assert index == expected_index and np.isclose(distance, expected_distance)

def test_find_closest_document_with_single_document():
    dataset = np.array([[1, 2]])
    query_document = np.array([1, 2])
    expected_index, expected_distance = 0, 0.0
    index, distance = find_closest_document(dataset, query_document)
    assert index == expected_index and np.isclose(distance, expected_distance)

def test_find_closest_document_with_large_dataset():
    dataset = np.random.rand(1000, 10)
    query_document = np.random.rand(10)
    index, distance = find_closest_document(dataset, query_document)
    assert 0 <= index < 1000