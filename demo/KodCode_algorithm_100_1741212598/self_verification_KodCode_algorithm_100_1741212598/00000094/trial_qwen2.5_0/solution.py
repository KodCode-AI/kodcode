import numpy as np

def runge_kutta_fehlberg_45(func, x_initial, y_initial, step_size, x_final):
    """
    Solves the ordinary differential equation given by func using the Runge-Kutta-Fehlberg method.
    
    Parameters:
    - func: A function representing the ODE, taking two arguments (x, y) and returning dy/dx.
    - x_initial: The initial value of x.
    - y_initial: The initial value of y.
    - step_size: The increment value of x.
    - x_final: The final value of x.
    
    Returns:
    - A NumPy array containing the solution y at each nodal point.
    """
    if not callable(func):
        raise TypeError("func must be a callable function.")
    if not (isinstance(x_initial, (int, float)) and isinstance(step_size, (int, float)) and isinstance(x_final, (int, float))):
        raise TypeError("x_initial, step_size, and x_final must be numeric values.")
    if not (isinstance(y_initial, (int, float)) or (isinstance(y_initial, np.ndarray) and y_initial.ndim == 1)):
        raise TypeError("y_initial must be a numeric value or an array of initial values.")
    if not (step_size > 0 and x_final > x_initial):
        raise ValueError("Step size must be positive and x_final must be greater than x_initial.")
    
    x = x_initial
    y = y_initial
    if isinstance(y_initial, np.ndarray):
        # Preserving the shape of the initial condition
        n = y_initial.size
        y_solution = np.zeros((n, int((x_final - x_initial) / step_size) + 1))
        y_solution[:, 0] = y_initial
    else:
        y_solution = np.zeros(int((x_final - x_initial) / step_size) + 1)
        y_solution[0] = y_initial
    
    for i in range(int((x_final - x_initial) / step_size)):
        k1 = func(x, y)
        k2 = func(x + step_size/4, y + step_size/4 * k1)
        k3 = func(x + 3*step_size/8, y + step_size/3 * (2*k1 + 2*k2) / 3)
        k4 = func(x + 12*step_size/13, y + step_size * (1932*k1 - 7200*k3 + 7296*k4) / 2197)
        k5 = func(x + step_size, y + step_size * (439*k1 - 84*k3 + 800*k4 - 25*k5) / 4096)
        k6 = func(x + step_size/2, y + step_size * (1408*k1 - 256*k3 + 1920*k4 - 124*k5) / 4275)
        k6 = func(x + step_size/2, y - step_size * (21*k1 - 4*k3 - 5*k4 + 9*k5 + 2*k6) / 14)

        y = y + step_size * (25*k1 + 1408*k4 + 21*k5 - 27*k6) / 2196
        x = x + step_size
        
        y_solution[:, i+1] = y
        
    return y_solution