from solution import *

``
import numpy as np
import pytest

def test_batch_sigmoid_performance():
    input_array = np.random.uniform(-1000, 1000, size=(1000, 1000))
    start_time = time.time()
    output_array = batch_sigmoid(input_array)
    end_time = time.time()
    assert (end_time - start_time) < 1, "The function took too long to process the array."

def test_batch_sigmoid_positive_numbers():
    input_array = np.array([[0, -1, 1], [100, -100, 0]])
    expected_output = np.array([[0.5, 0.26894142, 0.73105858], [1., 2.06115362e-45, 0.5]])
    np.testing.assert_array_almost_equal(batch_sigmoid(input_array), expected_output)

def test_batch_sigmoid_with_zeros():
    input_array = np.array([[0, 0, 0], [0, 0, 0]])
    expected_output = np.array([[0.5, 0.5, 0.5], [0.5, 0.5, 0.5]])
    np.testing.assert_array_almost_equal(batch_sigmoid(input_array), expected_output)

def test_batch_sigmoid_negative_numbers():
    input_array = np.array([[-10, -20, -30], [10, 20, 30]])
    expected_output = np.array([[4.53970023e-05, 2.06115362e-45, 1.39155858e-50], 
                                [0.9999547, 0.99998013, 0.99999786]])
    np.testing.assert_array_almost_equal(batch_sigmoid(input_array), expected_output)

def test_batch_sigmoid_mixed_sign_numbers():
    input_array = np.array([[-1, 0, 1], [-1000, 0, 1000]])
    expected_output = np.array([[0.26894142, 0.5, 0.73105858], 
                                [1.25834254e-434, 0.5, 0.99999999]])
    np.testing.assert_array_almost_equal(batch_sigmoid(input_array), expected_output)

def test_batch_sigmoid_zero_input():
    input_array = np.zeros((100, 100))
    expected_output = np.full((100, 100), 0.5)
    np.testing.assert_array_equal(batch_sigmoid(input_array), expected_output)

def test_batch_sigmoid Invalid_input():
    with pytest.raises(ValueError):
        batch_sigmoid(np.array([1, 2, 3]))
    with pytest.raises(ValueError):
        batch_sigmoid(np.random.uniform(-1000, 1000, size=(1000, 1000, 1000)))