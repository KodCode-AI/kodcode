from solution import *

import numpy as np
from solution import activation_function

def test_binary_step():
    assert np.array_equal(activation_function(np.array([-1.2, 0, 2, 1.45, -3.7, 0.3]), 'binary_step'), np.array([0, 1, 1, 1, 0, 1]))

def test_relu():
    assert np.array_equal(activation_function(np.array([-1, 0, 1, -2, 2]), 'relu'), np.array([0, 0, 1, 0, 2]))

def test_sigmoid():
    vector = np.array([-1, 0, 1])
    expected_output = np.array([0.26894142, 0.5, 0.73105858])
    np.testing.assert_almost_equal(activation_function(vector, 'sigmoid'), expected_output)

def test_invalid_mode():
    with np.testing.assert_raises(ValueError):
        activation_function(np.array([-1, 2]), 'tanh')