import numpy as np
import tensorflow as tf

def simplified_k_means_clustering(vectors, noofclusters, iterations=100):
    """
    Simplified K-Means clustering algorithm implementation using TensorFlow.
    
    :param vectors: 2D NumPy array of shape (n, d) containing the data points.
    :param noofclusters: Number of clusters to form.
    :param iterations: Number of iterations to run the algorithm.
    :return: centroids (2D NumPy array of shape (k, d)), assignments (list)
    """
    # Initialize centroids
    indices = np.random.choice(vectors.shape[0], noofclusters, replace=False)
    centroids = vectors[indices]
    
    for _ in range(iterations):
        # Expectation step: Compute distances and assign data points to the nearest centroid
        distances = tf.reduce_sum(tf.square(tf.expand_dims(vectors, axis=1) - centroids), axis=2)
        assignments = tf.argmin(distances, axis=1).numpy()
        
        # Maximization step: Update centroids
        new_centroids = []
        for i in range(noofclusters):
            assigned_points = vectors[assignments == i]
            if assigned_points.shape[0] > 0:
                new_centroids.append(tf.reduce_mean(assigned_points, axis=0).numpy())
            else:
                new_centroids.append(centroids[i])
        centroids = np.array(new_centroids)
    
    return centroids, assignments