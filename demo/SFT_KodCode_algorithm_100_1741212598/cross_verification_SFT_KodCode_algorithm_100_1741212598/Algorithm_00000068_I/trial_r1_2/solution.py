import numpy as np

def activation_function(vector: np.ndarray, mode: str) -> np.ndarray:
    if mode == 'binary_step':
        return np.where(vector >= 0, 1, 0)
    elif mode == 'relu':
        return np.maximum(vector, 0)
    elif mode == 'sigmoid':
        return 1 / (1 + np.exp(-vector))
    else:
        raise ValueError("Invalid mode.")