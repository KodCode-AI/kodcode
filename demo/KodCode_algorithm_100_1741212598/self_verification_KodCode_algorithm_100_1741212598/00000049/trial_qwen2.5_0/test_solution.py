from solution import *

`python
import numpy as np
import pytest

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

def test_batch_sigmoid_with_small_values():
    input_array = np.array([[0, -1, 1], [100, -100, 0]])
    output_array = batch_sigmoid(input_array)
    expected_output = np.array([[0.5        , 0.26894142 , 0.73105858 ],
                                [1.         , 2.06115362e-45 , 0.5       ]])
    assert np.allclose(output_array, expected_output)

def test_batch_sigmoid_with_large_values():
    input_array = np.array([[1000, -1000], [1000, -1000]])
    output_array = batch_sigmoid(input_array)
    expected_output = np.array([[1.        , 1.1164171e-435],
                                [1.        , 1.1164171e-435]])
    assert np.allclose(output_array, expected_output)

def test_batch_sigmoid_with_negative_zero():
    input_array = np.array([[1, -1, 0], [0, -1, 0]])
    output_array = batch_sigmoid(input_array)
    expected_output = np.array([[0.73105858 , 0.26894142 , 0.5       ],
                                [0.5       , 0.26894142 , 0.5       ]])
    assert np.allclose(output_array, expected_output)

def test_batch_sigmoid_with_edge_cases():
    input_array = np.array([[np.inf, -np.inf, 0], [-np.inf, np.inf, 0]])
    output_array = batch_sigmoid(input_array)
    expected_output = np.array([[1., 0., 0.5], [0., 1., 0.5]])
    assert np.allclose(output_array, expected_output)

def test_batch_sigmoid_type_error():
    with pytest.raises(ValueError):
        batch_sigmoid([1, 2, 3])

def test_batch_sigmoid_non_2d_array():
    with pytest.raises(ValueError):
        batch_sigmoid(np.array([1, 2, 3]).reshape(3, 1, 1))