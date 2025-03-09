def terminal_velocity(mass: float, density: float, area: float, drag_coefficient: float) -> float:
    """
    Calculates the terminal velocity of a sphere in a given fluid.

    :param mass: Mass of the sphere in kilograms.
    :param density: Density of the fluid in kilograms per cubic meter.
    :param area: Cross-sectional area of the sphere in square meters.
    :param drag_coefficient: Drag coefficient of the sphere.
    :return: Terminal velocity of the sphere in meters per second.

    Raises ValueError if any input is non-positive.
    """
    if mass <= 0 or density <= 0 or area <= 0 or drag_coefficient <= 0:
        raise ValueError("All inputs must be positive and non-zero.")

    g = 9.81  # Acceleration due to gravity in m/s^2
    vt = (2 * mass * g / (density * area * drag_coefficient)) ** 0.5
    return vt