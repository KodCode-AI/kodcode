import numpy as np

def activation_function(vector: np.ndarray, mode: str) -> np.ndarray:
    """
    Applies a specific activation function to the input vector based on the mode.
    """
    if mode == 'binary_step':
        return (vector > 0).astype(int)
    elif mode == 'relu':
        return np.maximum(0, vector)
    elif mode == 'sigmoid':
        return 1 / (1 + np.exp(-vector))
    else:
        raise ValueError("Unknown activation mode: {}".format(mode))

# Example usage
if __name__ == "__main__":
    vector1 = np.array([-1.2, 0, 2, 1.45, -3.7, 0.3])
    vector2 = np.array([-1, 0, 1, -2, 2])
    vector3 = np.array([-1, 0, 1])
    
    print(activation_function(vector1, 'binary_step'))
    print(activation_function(vector2, 'relu'))
    print(activation_function(vector3, 'sigmoid'))