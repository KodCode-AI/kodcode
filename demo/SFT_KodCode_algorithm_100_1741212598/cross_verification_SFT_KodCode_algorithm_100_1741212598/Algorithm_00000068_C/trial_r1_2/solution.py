import numpy as np

def activation_function(vector: np.ndarray, mode: str) -> np.ndarray:
    """
    Returns the numpy array of after applying the specified activation function.
    
    Parameters:
    vector (np.ndarray): Input array to apply the activation function.
    mode (str): The activation function to apply. Can be 'binary_step', 'relu', or 'sigmoid'.
    
    Returns:
    np.ndarray: Array after applying the activation function.
    
    Raises:
    ValueError: If the mode is not one of the specified activation functions.
    """
    if mode == 'binary_step':
        return np.where(vector >= 0, 1, 0)
    elif mode == 'relu':
        return np.where(vector < 0, 0, vector)
    elif mode == 'sigmoid':
        return 1 / (1 + np.exp(-vector))
    else:
        raise ValueError(f"Invalid activation mode: {mode}.")