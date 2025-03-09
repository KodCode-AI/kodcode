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

def logistic_reg(alpha: float, x: np.ndarray, y: np.ndarray, max_iterations: int = 10000) -> np.ndarray:
    m, n = x.shape
    x = np.column_stack((np.ones(m), x))  # Add bias term
    theta = np.zeros(n + 1)
    
    for _ in range(max_iterations):
        z = np.dot(x, theta)
        h = sigmoid_function(z)
        gradient = (1 / m) * np.dot(x.T, (h - y))
        theta -= alpha * gradient
    
    return theta

if __name__ == "__main__":
    filepath = 'iris.csv'
    X, y = load_data(filepath)
    X = (X - X.mean()) / X.std()  # Normalize the data
    alpha = 0.1
    theta = logistic_reg(alpha, X, y, max_iterations=10000)
    print("theta: ", theta)

    # Plot the decision boundary
    sepal_length = np.linspace(X[:, 1].min(), X[:, 1].max(), 100)
    sepal_width = -(theta[0] + theta[1] * sepal_length) / theta[2]
    plt.plot(sepal_length, sepal_width, 'r')
    
    # Scatter plot for setosa and non-setosa
    setosa = X[y == 1]
    non_setosa = X[y == 0]
    plt.scatter(setosa[:, 1], setosa[:, 2], c='b', marker='o')
    plt.scatter(non_setosa[:, 1], non_setosa[:, 2], c='r', marker='x')
    
    plt.xlabel('sepal length (normalized)')
    plt.ylabel('sepal width (normalized)')
    plt.show()