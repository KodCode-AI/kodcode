from solution import *

import numpy as np
from solution import run_linear_regression, sum_of_square_error, mean_absolute_error, run_steep_gradient_descent

# Test data
data_x = np.array([[1, 50], [1, 70], [1, 90], [1, 110]])
data_y = np.array([4, 5, 6, 7])
theta = run_linear_regression(data_x, data_y)

def test_run_linear_regression():
    expected_theta = np.array([[4.00244117, 0.00982216]])
    np.testing.assert_almost_equal(theta, expected_theta, decimal=5)

def test_sum_of_square_error():
    y_true = np.array([4, 5, 6, 7])
    y_pred = np.dot(data_x, expected_theta.T)
    assert sum_of_square_error(y_true, y_pred) == 0.03074165673623418

def test_mean_absolute_error():
    y_true = np.array([4, 5, 6, 7])
    y_pred = np.dot(data_x, expected_theta.T)
    assert mean_absolute_error(y_true, y_pred) == 0.012724940181889844

def test_run_steep_gradient_descent():
    theta_init = np.zeros((1, 2))
    alpha = 0.000155
    num_iterations = 100
    theta = run_steep_gradient_descent(data_x, data_y, theta_init, alpha, num_iterations)
    assert np.allclose(theta, expected_theta, atol=1e-5)