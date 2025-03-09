import numpy as np

def run_linear_regression(data_x, data_y):
    """
    Performs linear regression with L2 regularization on the provided data.
    """
    alpha = 0.0001550
    lambda_ = 0.01
    num_iterations = 100000
    n_samples, n_features = data_x.shape
    
    # Initialize theta
    theta = np.zeros((1, n_features + 1))
    
    for _ in range(num_iterations):
        gradient = np.dot(data_x.T, (np.dot(data_x, theta) - data_y)) / n_samples + \
                   (2 * lambda_ / n_samples) * theta
        theta -= alpha * gradient
    
    return theta

# Helper functions for testing
def sum_of_square_error(y_true, y_pred):
    return np.sum((y_true - y_pred) ** 2)

def mean_absolute_error(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

def run_steep_gradient_descent(data_x, data_y, theta, alpha, num_iterations):
    n_samples, n_features = data_x.shape
    for _ in range(num_iterations):
        gradient = np.dot(data_x.T, (np.dot(data_x, theta) - data_y)) / n_samples + \
                   (2 * 0.01 / n_samples) * theta
        theta -= alpha * gradient
    return theta