import numpy as np

def find_closest_document(dataset, query_document):
    """
    Finds the closest document to the query document based on Euclidean distance.

    Parameters:
    - dataset: A 2D NumPy array where each row represents a document vector.
    - query_document: A 1D NumPy array representing the query document vector.

    Returns:
    - A tuple containing the index of the closest document and the Euclidean distance.
    """
    euclidean_distances = np.linalg.norm(dataset - query_document, axis=1)
    closest_doc_index = np.argmin(euclidean_distances)
    closest_distance = euclidean_distances[closest_doc_index]
    return (closest_doc_index, closest_distance)

# Example usage
dataset = np.array([[1, 2], [3, 4], [5, 6]])
query_document = np.array([4, 5])
print(find_closest_document(dataset, query_document))