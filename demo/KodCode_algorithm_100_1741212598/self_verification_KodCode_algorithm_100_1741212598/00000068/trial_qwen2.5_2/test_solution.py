from solution import *

import numpy as np
from scipy.special import expit  # Import the expit function for sigmoid

def test_activation_function():
    # Binary Step Function
    vector = np.array([-1.2, 0, 2, 1.45, -3.7, 0.3])
    expected = np.array([0, 1, 1, 1, 0, 1])
    result = activation_function(vector, 'binary_step')
    assert np.array_equal(result, expected)

    # ReLU Function
    vector = np.array([-1, 0, 1, -2, 2])
    expected = np.array([0, 0, 1, 0, 2])
    result = activation_function(vector, 'relu')
    assert np.array_equal(result, expected)

    # Sigmoid Function
    vector = np.array([-1, 0, 1])
    expected = expit(vector)  # Using scipy's expit for exact sigmoid implementation
    result = activation_function(vector, 'sigmoid')
    assert np.allclose(result, expected)

    # Unknown activation mode
    try:
        activation_function(np.array([-1, 0, 1]), 'unknown')
    except ValueError:
        pass  # Test passes if it raises the expected ValueError

test_activation_function()