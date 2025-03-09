def terminal_velocity(mass: float, density: float, area: float, drag_coefficient: float) -> float:
    """
    Calculates the terminal velocity of a sphere based on given parameters.
    
    :param mass: Mass of the sphere in kilograms (Kg).
    :param density: Density of the fluid in kilograms per cubic meter (Kg/m³).
    :param area: Cross-sectional area of the sphere in square meters (m²).
    :param drag_coefficient: Drag coefficient (dimensionless).
    :return: Terminal velocity in meters per second (m/s).
    
    Raises ValueError for non-positive inputs.
    """
    if mass <= 0 or density <= 0 or area <= 0 or drag_coefficient <= 0:
        raise ValueError("All inputs must be positive.")
    
    g = 9.81  # acceleration due to gravity (m/s²)
    numerator = 2 * mass * g
    denominator = density * area * drag_coefficient
    vt = (numerator / denominator) ** 0.5
    return vt