from solution import *

import numpy as np
from solution import run_linear_regression, run_steep_gradient_descent, sum_of_square_error, mean_absolute_error

# Test cases
def test_run_linear_regression():
    # Test with a simple dataset
    data_x = np.array([[1, 50], [1, 70], [1, 90], [1, 110]])
    data_y = np.array([4, 5, 6, 7])
    theta = run_linear_regression(data_x, data_y)
    # Expected theta values can be based on the model fitting and validation
    assert np.isclose(theta[0, 0], 4.0, atol=0.01)
    assert np.isclose(theta[0, 1], 0.01, atol=0.001)

def test_sum_of_square_error():
    # Example data
    data_x = np.array([[1, 2], [1, 3], [1, 4]])
    data_y = np.array([2, 3, 4])
    theta = np.array([[1, 1]])
    assert np.isclose(sum_of_square_error(data_x, data_y, theta), 0.0)

def test_mean_absolute_error():
    # Example data
    data_x = np.array([[1, 2], [1, 3], [1, 4]])
    data_y = np.array([2, 3, 4])
    theta = np.array([[1, 1]])
    assert np.isclose(mean_absolute_error(data_x, data_y, theta), 0.0)

# Run the test functions
if __name__ == "__main__":
    test_run_linear_regression()
    test_sum_of_square_error()
    test_mean_absolute_error()