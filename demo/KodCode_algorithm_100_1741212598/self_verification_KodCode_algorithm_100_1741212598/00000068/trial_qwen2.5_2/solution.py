import numpy as np

def activation_function(vector: np.ndarray, mode: str) -> np.ndarray:
    """
    Returns the numpy array of the values after applying the specified activation function.
    """
    if mode == 'binary_step':
        return np.where(vector >= 0, 1, 0)
    elif mode == 'relu':
        return np.maximum(0, vector)
    elif mode == 'sigmoid':
        return 1 / (1 + np.exp(-vector))
    else:
        raise ValueError("Unknown activation mode: {}".format(mode))