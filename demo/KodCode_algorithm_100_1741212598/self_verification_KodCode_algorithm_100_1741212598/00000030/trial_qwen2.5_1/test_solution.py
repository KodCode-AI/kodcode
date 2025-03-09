from solution import *

import pytest
import numpy as np

def test_logistic_reg():
    # Test data
    X = np.array([[1, 2], [1, 3], [1, 4], [1, 5]])
    y = np.array([0, 1, 1, 0])
    
    # Expected theta
    expected_theta = np.array([-3, 1, 1])
    
    # Run logistic regression
    theta = logistic_reg(0.1, X, y, max_iterations=10000)
    
    # Verify the result is close to the expected theta
    np.testing.assert_array_almost_equal(theta, expected_theta, decimal=2)

def test_sigmoid_function():
    # Test sigmoid function
    z = 0
    expected_output = 0.5
    assert np.isclose(sigmoid_function(z), expected_output)

def test_cost_function():
    # Test cost function
    h = np.array([0.5, 0.5, 0.5])
    y = np.array([1, 0, 1])
    expected_output = 0.69314718
    assert np.isclose(cost_function(h, y), expected_output)

def test_load_data():
    # Test loading data
    filepath = 'iris.csv'
    X, y = load_data(filepath)
    assert X.shape[0] == y.shape[0]
    assert X.shape[1] == 2
    assert y.shape[0] == X.shape[0]