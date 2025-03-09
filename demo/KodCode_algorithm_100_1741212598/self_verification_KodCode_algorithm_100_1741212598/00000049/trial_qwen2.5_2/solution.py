import numpy as np

def batch_sigmoid(x):
    """
    Applies the sigmoid function element-wise to a 2D numpy array.
    """
    if not isinstance(x, np.ndarray) or x.ndim != 2:
        raise ValueError("Input must be a 2D numpy array.")
    
    # Avoid numerical instability for very large or very small input values.
    max_val = np.max(x)
    adjusted_x = x - max_val
    result = 1 / (1 + np.exp(-adjusted_x))
    return result