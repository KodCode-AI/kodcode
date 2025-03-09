import numpy as np

def activation_function(vector: np.ndarray, mode: str) -> np.ndarray:
    """
    Applies a specified activation function to the input vector based on the given mode.
    """
    if mode == 'binary_step':
        return (vector > 0).astype(int)
    elif mode == 'relu':
        return np.maximum(0, vector)
    elif mode == 'sigmoid':
        return 1 / (1 + np.exp(-vector))
    else:
        raise ValueError("Unsupported mode. Choose from 'binary_step', 'relu', 'sigmoid'.")