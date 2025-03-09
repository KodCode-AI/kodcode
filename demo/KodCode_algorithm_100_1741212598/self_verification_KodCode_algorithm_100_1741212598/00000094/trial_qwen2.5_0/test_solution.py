from solution import *

import numpy as np
from solution import runge_kutta_fehlberg_45

def f1(x, y):
    return x + y

# Test case 1: Simple ODE with exponential solution
y1 = runge_kutta_fehlberg_45(f1, 0, 0, 0.1, 1)
expected_y1 = np.exp(np.linspace(0, 1, len(y1)))
assert np.allclose(y1, expected_y1)

# Test case 2: ODE with initial condition as an array
y_initial = np.array([0, 0])
y2 = runge_kutta_fehlberg_45(f1, 0, y_initial, 0.1, 1)
expected_y2 = np.exp(np.linspace(0, 1, len(y2)))
assert np.allclose(y2, np.vstack((expected_y2, expected_y2)).T)

# Test case 3: ODE with negative initial condition
y3 = runge_kutta_fehlberg_45(f1, 0, -1, 0.1, 1)
expected_y3 = np.exp(np.linspace(0, 1, len(y3))) - 1
assert np.allclose(y3, expected_y3)

# Test case 4: ODE with non-integer initial condition
y4 = runge_kutta_fehlberg_45(f1, 0.5, 0, 0.1, 1)
expected_y4 = np.exp(np.linspace(0.5, 1, len(y4)))
assert np.allclose(y4, expected_y4)

# Test case 5: ODE with non-integer step size
y5 = runge_kutta_fehlberg_45(f1, 0, 0, 0.25, 1)
expected_y5 = np.exp(np.linspace(0, 1, len(y5)))
assert np.allclose(y5, expected_y5)

# Test case 6: ODE with step size exactly reaching the final state
y6 = runge_kutta_fehlberg_45(f1, 0, 0, 1.5, 1.5)
expected_y6 = np.exp(np.linspace(0, 1.5, len(y6)))
assert np.allclose(y6, expected_y6)