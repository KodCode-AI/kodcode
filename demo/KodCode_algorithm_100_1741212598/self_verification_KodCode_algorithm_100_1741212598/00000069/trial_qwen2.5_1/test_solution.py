from solution import *

import numpy as np
from sklearn.datasets import make_blobs
import tensorflow as tf

# Generate sample data
def test_simplified_k_means_clustering():
    vectors, _ = make_blobs(n_samples=1000, centers=5, n_features=2, random_state=42)
    noofclusters = 5
    
    # Run the k-means clustering
    centroids, assignments = simplified_k_means_clustering(vectors, noofclusters)
    
    # Check the shape of the centroids
    assert centroids.shape == (noofclusters, 2), f"Unexpected shape for centroids: {centroids.shape}"
    
    # Check the length of the assignments
    assert len(assignments) == vectors.shape[0], f"Unexpected length of assignments: {len(assignments)}"
    
    # Check for unique assignments within the expected range
    unique_assignments = set(assignments)
    expected_clusters = set(range(noofclusters))
    assert unique_assignments.issubset(expected_clusters), f"Assignments do not match expected clusters: {unique_assignments}"
    
    print("All tests passed.")

test_simplified_k_means_clustering()