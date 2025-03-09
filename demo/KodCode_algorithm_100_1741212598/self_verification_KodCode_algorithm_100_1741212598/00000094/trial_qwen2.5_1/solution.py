import numpy as np

def runge_kutta_fehlberg_45(func, x_initial, y_initial, step_size, x_final):
    """
    Solves an ODE using the Runge-Kutta-Fehlberg 45 method.
    
    :param func: A function representing the ODE, which takes two arguments (x, y) and returns dy/dx.
    :param x_initial: The initial value of x.
    :param y_initial: The initial value of y.
    :param step_size: The increment value of x.
    :param x_final: The final value of x.
    :return: A NumPy array containing the solution y at each nodal point.
    """
    if step_size <= 0 or x_final <= x_initial:
        raise ValueError("Step size must be positive and final x must be greater than initial x.")
    
    x = x_initial
    y = y_initial
    solution = [y_initial]
    
    while x < x_final:
        k1 = step_size * func(x, y)
        k2 = step_size * func(x + 0.25 * step_size, y + 0.25 * k1)
        k3 = step_size * func(x + 0.5 * step_size, y + 0.5 * (k1 + k2) / 3)
        k4 = step_size * func(x + 7 * step_size / 8, y + 7 * k1 / 24 + 7 * k2 / 8 - 7 * k3 / 24 + k4)
        k5 = step_size * func(x + step_size, y + 1932 * k1 / 2197 - 7200 * k2 / 2197 + 7296 * k3 / 2197 - 432 * k4 / 2197)
        k6 = step_size * func(x + 14 * step_size / 59, y + 448 * k1 / 255 - 5600 * k2 / 1181 + 4800 * k3 / 1181 - 1250 * k4 / 1181 + 110056 * k5 / 45927))
        
        k1 = (37 * k1 + 7296 * k2 - 7200 * k3 - 432 * k4 + 8454451 * k5 + 165029184 * k6) / 845455
        k2 = (-845455 * k1 + 844224 * k2 - 693000 * k3 + 307716 * k4 - 103687520 * k5 - 382495296 * k6) / 5529600
        k3 = (4177200 * k1 - 8046720 * k2 + 6652800 * k3 - 2851200 * k4 + 2079676320 * k5 + 2242987456 * k6) / 56980800
        k4 = (1286400 * k1 - 1433600 * k2 + 763200 * k3 - 198240 * k4 + 909954688 * k5 + 1714210496 * k6) / 13809600
        k5 = (-21244800 * k1 + 3014400 * k2 + 13884000 * k3 - 4305600 * k4 + 5277303680 * k5 + 10230395520 * k6) / 151876800
        k6 = (12988800 * k1 - 2299200 * k2 + 15014400 * k3 - 4670400 * k4 + 1919371200 * k5 + 3818459200 * k6) / 151876800
        
        y += (9 * k1 + 19 * k3 + 5 * k4 + 9 * k5 + 44 / 45 * k6) / 84
        x += step_size
        solution.append(y)
    
    return np.array(solution)