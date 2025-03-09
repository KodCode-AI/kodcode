def real_quadratic_roots(a: int, b: int, c: int) -> tuple[float, ...]:
    if a == 0:
        raise ValueError("Coefficient 'a' must not be zero.")
    
    discriminant = b ** 2 - 4 * a * c
    
    if discriminant < 0:
        return ()
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        sqrt_discriminant = discriminant ** 0.5
        root1 = (-b + sqrt_discriminant) / (2 * a)
        root2 = (-b - sqrt_discriminant) / (2 * a)
        return (root1, root2)