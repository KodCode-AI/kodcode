from solution import *

import numpy as np
import pytest

def test_batch_sigmoid_positive_numbers():
    input_array = np.array([[0, -1, 1], [10, -10, 0]])
    expected_output = np.array([[0.5, 0.26894142, 0.73105858], 
                                [0.9999546, 0.0000454, 0.5]])
    np.testing.assert_almost_equal(batch_sigmoid(input_array), expected_output, decimal=7)

def test_batch_sigmoid_large_input_values():
    input_array = np.array([[100, -100, 0]])
    expected_output = np.array([[1., 2.0611536e-45, 0.5]])
    np.testing.assert_almost_equal(batch_sigmoid(input_array), expected_output, decimal=5)

def test_batch_sigmoid_zero_input():
    input_array = np.zeros((1000, 1000))
    expected_output = np.full((1000, 1000), 0.5)
    np.testing.assert_equal(batch_sigmoid(input_array), expected_output)

def test_batch_sigmoid_with_negative_values():
    input_array = np.array([[-1000, 1000]])
    expected_output = np.array([[1.78179747e-437, 5.19681036e+432]])
    np.testing.assert_almost_equal(batch_sigmoid(input_array), expected_output, decimal=5)

def test_batch_sigmoid_shape():
    input_array = np.random.rand(1000, 1000)
    output_array = batch_sigmoid(input_array)
    assert output_array.shape == input_array.shape

def test_batch_sigmoid_type():
    input_array = np.random.rand(1000, 1000)
    with pytest.raises(ValueError):
        batch_sigmoid(input_array[0, :])  # Should raise an error for 1D array
    with pytest.raises(ValueError):
        batch_sigmoid(np.random.rand(1000, 1000, 1000))  # Should raise an error for 3D array

def test_batch_sigmoid_input_type():
    with pytest.raises(ValueError):
        batch_sigmoid([1, 2, 3])  # Should raise an error for list input
    with pytest.raises(ValueError):
        batch_sigmoid(np.random.rand())  # Should raise an error for scalar input