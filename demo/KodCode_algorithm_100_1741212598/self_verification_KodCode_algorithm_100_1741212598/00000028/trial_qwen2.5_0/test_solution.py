from solution import *

import numpy as np
from solution import run_linear_regression, run_steep_gradient_descent, sum_of_square_error, mean_absolute_error

def test_linear_regression():
    data_x = np.array([[1, 50], [1, 70], [1, 90], [1, 110]])
    data_y = np.array([4, 5, 6, 7])
    theta = run_linear_regression(data_x, data_y)
    assert theta.shape == (1, 2)
    y_pred = data_x.dot(theta.T)
    assert np.isclose(sum_of_square_error(data_y, y_pred), 0.0644, atol=1e-4)
    assert np.isclose(mean_absolute_error(data_y, y_pred), 0.0161, atol=1e-4)

def test_steepest_gradient_descent():
    np.random.seed(0)
    X = np.random.rand(100, 2)
    X = np.c_[np.ones((X.shape[0], 1)), X]  # adding bias term
    y = 2 + 3 * X[:, 1] + 4 * X[:, 2] + np.random.randn(100) * 0.1  # y = 2 + 3x1 + 4x2
    theta = np.zeros((1, 3))
    alpha = 0.0001550
    lambda_reg = 0.01
    iterations = 100000
    theta = run_steep_gradient_descent(X, y, theta, alpha, lambda_reg, iterations)
    y_pred = X.dot(theta.T)
    assert np.isclose(sum_of_square_error(y, y_pred), 0.0753, atol=1e-3)
    assert np.isclose(mean_absolute_error(y, y_pred), 0.0190, atol=1e-3)

# Running tests
test_linear_regression()
test_steepest_gradient_descent()