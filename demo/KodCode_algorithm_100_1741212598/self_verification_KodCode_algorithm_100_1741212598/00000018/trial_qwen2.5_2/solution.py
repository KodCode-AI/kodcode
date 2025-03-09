import numpy as np

def find_closest_document(dataset, query_document):
    """
    Finds the closest document to the query document based on Euclidean distance.
    
    :param dataset: A 2D NumPy array where each row represents a document vector.
    :param query_document: A 1D NumPy array representing the query document vector.
    :return: A tuple containing the index of the closest document and the Euclidean distance.
    """
    distances = np.linalg.norm(dataset - query_document, axis=1)
    closest_index = np.argmin(distances)
    closest_distance = distances[closest_index]
    return closest_index, closest_distance