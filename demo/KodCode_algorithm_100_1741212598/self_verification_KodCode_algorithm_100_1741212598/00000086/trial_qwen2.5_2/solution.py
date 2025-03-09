from typing import Union

def electrical_properties(
    l: float = None,
    f: float = None,
    x_l: float = None,
    x_c: float = None,
) -> Union[float, dict[str, float]]:
    """
    Calculate one of the electrical properties (inductance, frequency, inductive reactance, or capacitive reactance)
    given the other three properties. Exactly one property must be `None`.

    Parameters:
    l (float): Inductance in Henries.
    f (float): Frequency in Hertz.
    x_l (float): Inductive reactance in Ohms.
    x_c (float): Capacitive reactance in Ohms.
    
    Returns:
    Union[float, dict[str, float]]: The calculated property as a float or a dictionary with the calculated property.
    
    Raises:
    ValueError: If more than one property is `None` or if any of the given values are negative.
    """
    if sum(param is None for param in (l, f, x_l, x_c)) != 1:
        raise ValueError("Exactly one property must be None.")
    
    if any(param is not None and param < 0 for param in (l, f, x_l, x_c)):
        raise ValueError("All given values must be non-negative.")
    
    if l is None:
        if x_c is not None:
            l = 1 / (2 * 3.141592653589793 * f * x_c)
            return {'inductance': l}
        else:
            l = x_l / (2 * 3.141592653589793 * f)
            return {'inductance': l}
    elif f is None:
        if x_c is not None:
            f = 1 / (2 * 3.141592653589793 * x_c * l)
            return {'frequency': f}
        else:
            f = x_l / (2 * 3.141592653589793 * l)
            return {'frequency': f}
    elif x_l is None:
        if x_c is not None:
            x_l = 1 / (2 * 3.141592653589793 * f * l)
            return {'inductive reactance': x_l}
        else:
            x_l = 2 * 3.141592653589793 * f * l
            return {'inductive reactance': x_l}
    elif x_c is None:
        x_c = 1 / (2 * 3.141592653589793 * f * l)
        return {'capacitance': 1 / (2 * 3.141592653589793 * f * x_c)}