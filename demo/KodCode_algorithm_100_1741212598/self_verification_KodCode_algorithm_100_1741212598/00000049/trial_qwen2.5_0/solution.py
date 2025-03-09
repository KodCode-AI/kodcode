import numpy as np

def batch_sigmoid(x):
    """
    Applies the sigmoid function element-wise to a 2D numpy array.
    The function is optimized to avoid numerical instability for large and small input values.
    """
    if not isinstance(x, np.ndarray) or x.ndim != 2:
        raise ValueError("Input must be a 2D numpy array")
    
    # Avoid numerical instability for large input values
    x = np.clip(x, -500, 500)
    
    return 1 / (1 + np.exp(-x))