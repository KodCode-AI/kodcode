import numpy as np

def run_steep_gradient_descent(x, y, theta, alpha, lambda_reg, iterations):
    n = x.shape[1]
    m = len(y)
    for _ in range(iterations):
        error = x.dot(theta) - y
        gradient = x.T.dot(error) / m + 2 * lambda_reg * theta
        theta -= alpha * gradient
    return theta

def sum_of_square_error(y_true, y_pred):
    return np.sum((y_true - y_pred) ** 2)

def mean_absolute_error(y_true, y_pred):
    return np.mean(np.abs(y_true - y_pred))

def run_linear_regression(data_x, data_y):
    alpha = 0.0001550
    lambda_reg = 0.01
    iterations = 100000
    theta = np.zeros((1, data_x.shape[1]))
    
    theta = run_steep_gradient_descent(data_x, data_y, theta, alpha, lambda_reg, iterations)
    
    return theta