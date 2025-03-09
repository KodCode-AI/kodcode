def calculate_energy_from_mass(mass: float) -> float:
    """
    Calculates the energy (in Joules) equivalent of the given mass (in kilograms).
    
    mass (float): The mass in kilograms.
    
    Returns:
    float: The energy in Joules.
    
    Raises:
    ValueError: If the mass is negative.
    """
    if mass < 0:
        raise ValueError("Mass can't be negative.")
    speed_of_light = 299792458  # speed of light in meters per second
    energy = mass * (speed_of_light ** 2)
    return energy

def calculate_mass_from_energy(energy: float) -> float:
    """
    Calculates the mass (in kilograms) equivalent of the given energy (in Joules).
    
    energy (float): The energy in Joules.
    
    Returns:
    float: The mass in kilograms.
    
    Raises:
    ValueError: If the energy is negative.
    """
    if energy < 0:
        raise ValueError("Energy can't be negative.")
    speed_of_light = 299792458  # speed of light in meters per second
    mass = energy / (speed_of_light ** 2)
    return mass