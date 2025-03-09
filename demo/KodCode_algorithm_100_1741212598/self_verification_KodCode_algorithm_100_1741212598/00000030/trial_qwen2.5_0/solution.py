import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def sigmoid_function(z: float) -> float:
    return 1 / (1 + np.exp(-z))

def cost_function(h: np.ndarray, y: np.ndarray) -> float:
    return float((-y * np.log(h) - (1 - y) * np.log(1 - h)).mean())

def load_data(filepath: str) -> np.ndarray:
    data = pd.read_csv(filepath)
    y = data['class'].apply(lambda x: 1 if x == 'setosa' else 0).values
    X = data[['sepal_length', 'sepal_width']].values
    return X, y

def logistic_reg(alpha, x, y, max_iterations=10000):
    """
    Implement the logistic regression algorithm here.
    """
    m, n = x.shape
    theta = np.zeros(n)

    for i in range(max_iterations):
        z = np.dot(x, theta)
        h = sigmoid_function(z)
        gradients = np.dot(x.T, (h - y)) / m
        theta -= alpha * gradients

        # Early stopping if cost is not decreasing
        if i > 0:
            prev_cost = prev_cost
            current_cost = cost_function(h, y)
            if np.abs(prev_cost - current_cost) < 1e-6:
                break

        prev_cost = current_cost

    return theta

if __name__ == "__main__":
    filepath = 'iris.csv'
    X, y = load_data(filepath)
    X = (X - X.mean(axis=0)) / X.std(axis=0)  # Normalize the data
    alpha = 0.1
    theta = logistic_reg(alpha, X, y, max_iterations=10000)
    print("theta: ", theta)

    # Plot the decision boundary
    x1 = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
    x2 = (-theta[0] - theta[1] * x1) / theta[2]
    plt.plot(x1, x2, '-r', label='Decision boundary')
    plt.scatter(X[y == 0, 0], X[y == 0, 1], label='Non-setosa')
    plt.scatter(X[y == 1, 0], X[y == 1, 1], label='Setosa')
    plt.xlabel('Sepal length')
    plt.ylabel('Sepal width')
    plt.legend()
    plt.show()