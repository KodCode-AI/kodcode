import numpy as np

def activation_function(vector: np.ndarray, mode: str) -> np.ndarray:
    """
    Applies the specified activation function to each element of the vector.

    Args:
        vector: A numpy array of input values.
        mode: A string specifying the activation function to apply.
            - 'binary_step': Outputs 1 for values >= 0 and 0 otherwise.
            - 'relu': Outputs max(0, x) for each element x.
            - 'sigmoid': Applies the sigmoid function to each element.

    Returns:
        A numpy array of the results after applying the activation function.

    Raises:
        ValueError: If the mode is not one of the supported activation functions.
    """
    if mode == 'binary_step':
        return (vector >= 0).astype(int)
    elif mode == 'relu':
        return np.maximum(vector, 0)
    elif mode == 'sigmoid':
        return 1 / (1 + np.exp(-vector))
    else:
        raise ValueError(f"Mode '{mode}' is not supported.")

def test_activation_function():
    vector = np.array([-1.2, 0, 2, 1.45, -3.7, 0.3])
    expected = np.array([0, 1, 1, 1, 0, 1])
    result = activation_function(vector, 'binary_step')
    assert np.array_equal(result, expected)

    vector = np.array([-1, 0, 1, -2, 2])
    expected = np.array([0, 0, 1, 0, 2])
    result = activation_function(vector, 'relu')
    assert np.array_equal(result, expected)

    vector = np.array([-1, 0, 1])
    expected = 1 / (1 + np.exp(-vector))  # Using manual sigmoid implementation
    result = activation_function(vector, 'sigmoid')
    assert np.allclose(result, expected, rtol=1e-4, atol=1e-8)

    try:
        activation_function(np.array([-1, 0, 1]), 'unknown')
    except ValueError:
        pass  # Test passes if it raises the expected ValueError

if __name__ == "__main__":
    test_activation_function()