from solution import *

import numpy as np
from solution import activation_function

def test_activation_function():
    # Binary Step
    vector = np.array([-1.2, 0, 2, 1.45, -3.7, 0.3])
    expected = np.array([0, 0, 1, 1, 0, 1])
    assert np.array_equal(activation_function(vector, 'binary_step'), expected)

    # ReLU
    vector = np.array([-1, 0, 1, -2, 2])
    expected = np.array([0, 0, 1, 0, 2])
    assert np.array_equal(activation_function(vector, 'relu'), expected)

    # Sigmoid
    vector = np.array([-1, 0, 1])
    expected = np.round([0.26894142, 0.5, 0.73105858], decimals=9)
    assert np.allclose(activation_function(vector, 'sigmoid'), expected)

def test_invalid_mode():
    vector = np.array([-1, 0, 1])
    with pytest.raises(ValueError):
        activation_function(vector, 'invalid_mode')

# Running tests
if __name__ == "__main__":
    test_activation_function()
    print("All tests passed!")