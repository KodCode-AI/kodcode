import numpy as np

def run_linear_regression(data_x, data_y):
    """
    Perform linear regression with L2 regularization.
    
    Parameters:
    - data_x: A matrix of shape (n_samples, n_features + 1)
    - data_y: A vector of shape (n_samples,)
    
    Returns:
    - theta: A vector of shape (1, n_features + 1)
    """
    alpha = 0.0001550
    num_iterations = 100000
    lambda_ = 0.01
    n_samples, n_features = data_x.shape
    theta = np.zeros((1, n_features))
    
    for _ in range(num_iterations):
        predictions = np.dot(data_x, theta.T)
        error = predictions - data_y
        gradient = np.dot(data_x.T, error) / n_samples + lambda_ * theta
        theta -= alpha * gradient
    
    return theta

def run_steep_gradient_descent(data_x, data_y, theta, alpha, num_iterations):
    """
    Perform gradient descent for linear regression.
    """
    for _ in range(num_iterations):
        predictions = np.dot(data_x, theta.T)
        error = predictions - data_y
        gradient = np.dot(data_x.T, error) / len(data_y)
        theta -= alpha * gradient
    return theta

def sum_of_square_error(data_x, data_y, theta):
    """
    Compute the sum of square error.
    """
    predictions = np.dot(data_x, theta.T)
    return np.sum((predictions - data_y) ** 2)

def mean_absolute_error(data_x, data_y, theta):
    """
    Compute the mean absolute error.
    """
    predictions = np.dot(data_x, theta.T)
    return np.mean(np.abs(predictions - data_y))

# Initialize data
data_x = np.array([[1, 50], [1, 70], [1, 90], [1, 110]])
data_y = np.array([4, 5, 6, 7])

# Run the linear regression model
theta = run_linear_regression(data_x, data_y)
print(theta)