import numpy as np

def batch_sigmoid(x):
    """
    Applies the sigmoid function element-wise to a 2D numpy array.
    Args:
        x (np.ndarray): A 2D numpy array of shape (N, M).
    Returns:
        np.ndarray: A 2D numpy array of the same shape as x, with the sigmoid function applied element-wise.
    """
    if not isinstance(x, np.ndarray) or x.ndim != 2:
        raise ValueError("Input must be a 2D numpy array.")
    
    # To avoid numerical instability with large input values, subtract the max of x from x.
    x_max = np.max(x)
    result = 1 / (1 + np.exp(- (x - x_max)))
    return result