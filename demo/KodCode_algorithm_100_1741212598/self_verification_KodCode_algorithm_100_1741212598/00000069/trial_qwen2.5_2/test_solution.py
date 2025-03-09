from solution import *

import numpy as np
import tensorflow as tf
from solution import simplified_k_means_clustering

def test_simplified_k_means_clustering():
    # Generate sample data
    vectors, _ = make_blobs(n_samples=100, centers=5, n_features=2, random_state=42)
    noofclusters = 5

    # Perform K-Means clustering
    centroids, assignments = simplified_k_means_clustering(vectors, noofclusters)

    # Check the shape of the centroids
    assert centroids.shape == (noofclusters, vectors.shape[1])

    # Check the length of the assignments
    assert len(assignments) == vectors.shape[0]

    # Check that the assignments are within the range of centroids
    assert np.all(np.logical_and(assignments >= 0, assignments < noofclusters))

def test_k_means_with_random_data():
    # Generate random data
    vectors = np.random.rand(1000, 2)
    noofclusters = 5

    # Perform K-Means clustering
    centroids, assignments = simplified_k_means_clustering(vectors, noofclusters)

    # Check the shape of the centroids
    assert centroids.shape == (noofclusters, vectors.shape[1])

    # Check the length of the assignments
    assert len(assignments) == vectors.shape[0]

    # Check that the assignments are within the range of centroids
    assert np.all(np.logical_and(assignments >= 0, assignments < noofclusters))

def test_k_means_with_zeros():
    # Construct data with all zeros
    vectors = np.zeros((100, 2))
    noofclusters = 5

    # Perform K-Means clustering
    centroids, assignments = simplified_k_means_clustering(vectors, noofclusters)

    # Check the shape of the centroids
    assert centroids.shape == (noofclusters, vectors.shape[1])

    # Check the length of the assignments
    assert len(assignments) == vectors.shape[0]

    # Check that all assignments are zeros
    assert np.all(assignments == 0)

# Run tests
test_simplified_k_means_clustering()
test_k_means_with_random_data()
test_k_means_with_zeros()