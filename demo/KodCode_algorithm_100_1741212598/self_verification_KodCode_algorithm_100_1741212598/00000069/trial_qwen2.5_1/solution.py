import numpy as np
import tensorflow as tf

def simplified_k_means_clustering(vectors, noofclusters, max_iterations=100):
    """
    Simplified K-Means clustering algorithm implementation using TensorFlow.
    
    :param vectors: 2D NumPy array of shape (n, d)
    :param noofclusters: Number of clusters to form
    :param max_iterations: Maximum number of iterations to perform
    
    :return centroids: 2D NumPy array of shape (k, d)
    :return assignments: List of integers of length n
    """
    n, d = vectors.shape

    # Initialize centroids randomly from the dataset
    centroids_init = vectors[np.random.choice(n, noofclusters, replace=False)]

    # Convert vectors and centroids_init to TensorFlow constants
    vectors_tf = tf.constant(vectors, dtype=tf.float32)
    centroids_tf = tf.constant(centroids_init, dtype=tf.float32)

    # Define placeholders for distances and assignments
    distances = tf.placeholder(tf.float32, shape=(noofclusters, n))
    assignments_tf = tf.argmin(distances, axis=0)

    for _ in range(max_iterations):
        # Calculate distances from each point to each centroid
        distances_tf = tf.reduce_sum(tf.square(tf.expand_dims(vectors_tf, 0) - tf.expand_dims(centroids_tf, 1)), axis=2)
        
        # Get the current assignments
        with tf.Session() as sess:
            assignments_np = sess.run(assignments_tf, feed_dict={distances: distances_tf.eval()})

        # Update centroids
        new_centroids = np.zeros((noofclusters, d))
        counts = np.zeros((noofclusters,))
        for i in range(n):
            centroid_id = assignments_np[i]
            new_centroids[centroid_id] += vectors[i]
            counts[centroid_id] += 1
        for i in range(noofclusters):
            if counts[i] > 0:
                new_centroids[i] /= counts[i]
        
        # Check for convergence
        if np.allclose(new_centroids, centroids_tf.eval()):
            break
        
        # Update centroids
        centroids_tf = tf.assign(centroids_tf, new_centroids)
    
    with tf.Session() as sess:
        final_centroids = sess.run(centroids_tf)
        final_assignments = sess.run(assignments_tf, feed_dict={distances: distances_tf.eval()})

    return final_centroids, final_assignments.tolist()