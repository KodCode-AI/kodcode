import numpy as np
import tensorflow as tf

def initialize_centroids(vectors, noofclusters):
    """Initialize centroids randomly from the dataset."""
    idx = np.random.choice(vectors.shape[0], size=noofclusters, replace=False)
    centroids = vectors[idx]
    return centroids

def expectation_step(vectors, centroids):
    """Assign each data point to the nearest centroid."""
    distances = tf.reduce_sum(tf.pow(tf.expand_dims(vectors, 1) - centroids, 2), axis=2)
    assignments = tf.argmin(distances, axis=1)
    return assignments

def maximization_step(vectors, assignments, noofclusters):
    """Update the centroids to be the mean of the assigned data points."""
    new_centroids = tf.dynamic_partition(vectors, assignments, noofclusters)
    new_centroids = tf.math.reduce_mean(new_centroids, axis=1)
    return new_centroids

def simplified_k_means_clustering(vectors, noofclusters, max_iterations=100):
    """
    Perform K-Means clustering on the given dataset.

    :param vectors: 2D NumPy array of shape (n, d)
    :param noofclusters: Number of clusters
    :param max_iterations: Maximum number of iterations
    :return: Final centroids and assignments
    """
    # Convert numpy arrays to TensorFlow constants for efficient computation
    vectors_tf = tf.constant(vectors)
    noofclusters_tf = tf.constant(noofclusters)

    # Initialize centroids
    centroids = initialize_centroids(vectors, noofclusters_tf)
    init_centroids = tf.Variable(centroids, dtype=tf.float32, trainable=False)

    # Perform K-Means iterations
    for _ in range(max_iterations):
        with tf.GradientTape() as tape:
            assignments = expectation_step(vectors_tf, init_centroids)
            new_centroids = maximization_step(vectors_tf, assignments, noofclusters_tf)

        # Update centroids
        init_centroids.assign(new_centroids)

    # Convert TensorFlow tensors back to numpy arrays
    final_centroids = init_centroids.numpy()
    final_assignments = assignments.numpy()

    return final_centroids, final_assignments