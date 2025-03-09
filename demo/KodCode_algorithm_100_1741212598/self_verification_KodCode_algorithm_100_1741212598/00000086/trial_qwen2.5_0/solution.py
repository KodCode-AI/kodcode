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
    if l is not None and f is not None and x_l is not None and x_c is not None:
        raise ValueError("Exactly one property must be None")
    
    if l is not None and f is not None and x_l is None and x_c is None:
        x_l = 2 * 3.14159 * f * l
        return {'inductive reactance': x_l}
    elif l is not None and f is None and x_l is not None and x_c is None:
        f = x_l / (2 * 3.14159 * l)
        return {'frequency': f}
    elif l is not None and f is None and x_l is None and x_c is not None:
        l = 1 / (2 * 3.14159 * f * x_c)
        return {'inductance': l}
    elif f is not None and x_c is not None and l is None and x_l is None:
        c = 1 / (2 * 3.14159 * f * x_c)
        return {'capacitance': c}
    else:
        raise ValueError("Invalid input configuration")