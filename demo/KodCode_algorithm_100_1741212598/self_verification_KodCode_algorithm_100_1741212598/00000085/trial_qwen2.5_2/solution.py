def real_quadratic_roots(a: int, b: int, c: int) -> tuple[float, ...]:
    """
    Returns the real roots of a quadratic equation ax^2 + bx + c = 0.
    Returns an empty tuple if the equation has no real roots.
    Raises ValueError if 'a' is zero.
    """
    if a == 0:
        raise ValueError("Coefficient 'a' must not be zero.")
    
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant < 0:
        return ()
    elif discriminant == 0:
        return (-b / (2 * a),)
    else:
        sqrt_discriminant = discriminant ** 0.5
        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)
        return (root1, root2)