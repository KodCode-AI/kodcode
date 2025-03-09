import numpy as np

def runge_kutta_fehlberg_45(func, x_initial, y_initial, step_size, x_final):
    """
    Solves an ODE using the Runge-Kutta-Fehlberg method.
    
    Parameters:
    func (callable): The ODE function dy/dx = f(x, y).
    x_initial (float): The initial value of x.
    y_initial (float): The initial value of y.
    step_size (float): The step size for x.
    x_final (float): The final value of x.
    
    Returns:
    np.ndarray: Solutions y at each nodal point.
    """
    if step_size <= 0:
        raise ValueError("Step size must be positive.")
    if x_final <= x_initial:
        raise ValueError("Final x value must be greater than initial x value.")
    
    x = x_initial
    y = y_initial
    solutions = [y_initial]
    
    while x < x_final:
        k1 = step_size * func(x, y)
        k2 = step_size * func(x + 0.5 * step_size, y + 0.5 * k1)
        k3 = step_size * func(x + 0.5 * step_size, y + 0.5 * k2)
        k4 = step_size * func(x + step_size, y + k3)
        
        y_new = y + (k1 + 4 * k2 + 4 * k3 + k4) / 9
        y = y_new
        x += step_size
        solutions.append(y)
    
    return np.array(solutions)