from solution import *

def test_logistic_regression():
    # Create a temporary dataset for testing
    data = {
        'sepal_length': [5.1, 4.9, 4.7, 4.6, 5.0, 5.4],
        'sepal_width': [3.5, 3.0, 3.2, 3.1, 3.3, 3.9],
        'class': ['setosa', 'versicolor', 'versicolor', 'versicolor', 'setosa', 'setosa']
    }
    df = pd.DataFrame(data)
    X, y = df[['sepal_length', 'sepal_width']].values, df['class'].apply(lambda x: 1 if x == 'setosa' else 0).values

    X = (X - X.mean(axis=0)) / X.std(axis=0)  # Normalize the data
    alpha = 0.1
    
    theta = logistic_reg(alpha, X, y, max_iterations=10000)
    assert theta.shape == (2,)

def test_sigmoid_function():
    assert np.isclose(sigmoid_function(0), 0.5)
    assert np.isclose(sigmoid_function(100), 1.0)
    assert np.isclose(sigmoid_function(-100), 0.0)

def test_cost_function():
    h = np.array([0.8, 0.3, 0.9, 0.2])
    y = np.array([1, 0, 1, 0])
    cost = cost_function(h, y)
    assert np.isclose(cost, -0.2776557852)

if __name__ == "__main__":
    import pytest
    pytest.main(['-v', __file__])