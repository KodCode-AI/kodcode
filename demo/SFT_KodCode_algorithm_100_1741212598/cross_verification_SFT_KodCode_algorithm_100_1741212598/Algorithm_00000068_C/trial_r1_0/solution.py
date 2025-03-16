import numpy as np

def activation_function(vector: np.ndarray, mode: str) -> np.ndarray:
    """
    Returns the numpy array of the values after applying the specified activation function.
    """
    if mode == 'binary_step':
        return (vector >= 0).astype(int)
    elif mode == 'relu':
        return np.maximum(vector, 0)
    elif mode == 'sigmoid':
        return 1 / (1 + np.exp(-vector))
    else:
        raise ValueError("Invalid activation mode.")