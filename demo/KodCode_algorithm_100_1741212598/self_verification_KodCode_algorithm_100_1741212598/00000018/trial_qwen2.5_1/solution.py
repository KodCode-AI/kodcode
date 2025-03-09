import numpy as np

def find_closest_document(dataset, query_document):
    """
    Finds the closest document to the query document based on Euclidean distance.
    
    :param dataset: 2D NumPy array where each row represents a document vector.
    :param query_document: 1D NumPy array representing the query document vector.
    :return: A tuple containing the index of the closest document and the Euclidean distance.
    """
    # Calculate the Euclidean distance between the query document and each document in the dataset
    distances = np.linalg.norm(dataset - query_document, axis=1)
    # Find the index of the minimum distance
    min_index = np.argmin(distances)
    # Return the index of the closest document and its Euclidean distance
    return min_index, distances[min_index]