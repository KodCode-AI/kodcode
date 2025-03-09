def terminal_velocity(mass: float, density: float, area: float, drag_coefficient: float) -> float:
    """
    Calculates the terminal velocity of a sphere given its mass, fluid density, cross-sectional area, and drag coefficient.
    """
    if mass <= 0 or density <= 0 or area <= 0 or drag_coefficient <= 0:
        raise ValueError("All input parameters must be positive.")

    g = 9.81  # Acceleration due to gravity
    terminal_velocity = (2 * mass * g / (density * area * drag_coefficient))**0.5
    return terminal_velocity