from solution import *

import numpy as np
from solution import find_closest_document

def test_find_closest_document():
    dataset = np.array([[1, 2], [3, 4], [5, 6]])
    query_document = np.array([4, 5])
    expected = (1, 1.0)
    assert find_closest_document(dataset, query_document) == expected

def test_find_closest_document_random_data():
    dataset = np.random.rand(100, 10)
    query_document = np.random.rand(10)
    expected_distance = np.linalg.norm(dataset[0] - query_document)
    closest_index, closest_distance = find_closest_document(dataset, query_document)
    assert closest_index != 0  # Ensure it's not the first document
    assert np.isclose(closest_distance, np.linalg.norm(dataset[closest_index] - query_document))
    assert np.isclose(closest_distance, expected_distance)

def test_find_closest_document_single_document():
    dataset = np.array([[1, 1]])
    query_document = np.array([1, 1])
    expected = (0, 0.0)
    assert find_closest_document(dataset, query_document) == expected

def test_find_closest_document_empty_dataset():
    dataset = np.array([])
    query_document = np.array([1, 1])
    expected = None
    assert find_closest_document(dataset, query_document) == expected

def test_find_closest_document_same_document():
    dataset = np.array([[1, 1], [1, 1], [1, 1]])
    query_document = np.array([1, 1])
    expected = (0, 0.0)
    assert find_closest_document(dataset, query_document) == expected