def real_quadratic_roots(a: int, b: int, c: int) -> tuple[float, ...]:
    """
    Calculate the real roots of a quadratic equation based on given coefficients a, b, and c.
    Returns a tuple of real roots (if there are any) or an empty tuple if the roots are not real.
    Raises ValueError if a is zero.
    """
    if a == 0:
        raise ValueError("Coefficient 'a' must not be zero.")
    
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        return ()
    elif discriminant == 0:
        return (-b / (2*a),)
    else:
        sqrt_discriminant = discriminant**0.5
        root1 = (-b + sqrt_discriminant) / (2*a)
        root2 = (-b - sqrt_discriminant) / (2*a)
        return (root1, root2)