from typing import Union

def electrical_properties(
    l: float = None,
    f: float = None,
    x_l: float = None,
    x_c: float = None,
) -> Union[float, dict[str, float]]:
    from math import pi
    
    if sum([prop is None for prop in [l, f, x_l, x_c]]) != 1:
        raise ValueError("Exactly one property must be None.")
    
    if any([prop is not None and prop < 0 for prop in [l, f, x_l, x_c]]):
        raise ValueError("All given values must be non-negative.")
    
    if l is None:
        l = x_l / (2 * pi * f)
        return {'inductance': l}
    
    if f is None:
        f = x_l / (2 * pi * l)
        return {'frequency': f}
    
    if x_l is None:
        x_l = 2 * pi * f * l
        return {'inductive reactance': x_l}
    
    if x_c is None:
        x_c = 1 / (2 * pi * f * 1e-9 * l)
        return {'capacitive reactance': x_c}