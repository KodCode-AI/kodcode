from solution import *

import numpy as np
from sklearn.datasets import make_blobs
import pytest

def test_simplified_k_means_clustering():
    # Generate sample data
    vectors, _ = make_blobs(n_samples=1000, centers=5, n_features=2, random_state=42)
    noofclusters = 5
    
    # Run the K-Means clustering algorithm
    centroids, assignments = simplified_k_means_clustering(vectors, noofclusters)
    
    # Check the shape of the centroids
    assert centroids.shape == (noofclusters, vectors.shape[1]), "Centroids shape is incorrect"
    
    # Check the correctness of the assignments
    assert len(assignments) == vectors.shape[0], "Assignments length is incorrect"
    
    # Check if all assignments are valid cluster indices
    assert np.all(np.isin(assignments, list(range(noofclusters)))), "Invalid assignments found"
    
    # Check if the centroids are not empty
    assert np.all(np.not_equal(centroids, 0)), "Centroids are not properly updated"

# Run the tests
if __name__ == "__main__":
    pytest.main()