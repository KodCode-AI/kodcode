def energy_conversion(from_type, to_type, value):
    """
    Convert energy from one unit to another.
    
    Parameters:
    - from_type: The unit to convert from. Supports 'joule', 'wattsecond', 'electronvolt_per_photon'.
    - to_type: The unit to convert to. Supports 'joule', 'wattsecond', 'electronvolt_per_photon'.
    - value: The numeric value to convert.
    
    Returns:
    - A float representing the converted value.
    
    Raises:
    - ValueError: If invalid units are provided.
    """
    units_to_joules = {
        'joule': 1,
        'wattsecond': 1,
        'electronvolt_per_photon': 6.241509074460763e+15
    }
    
    if from_type not in units_to_joules or to_type not in units_to_joules:
        raise ValueError(f"Invalid units provided. Supported units: {list(units_to_joules.keys())}")
    
    if from_type == to_type:
        return value
    
    conversion_factor_from = units_to_joules[from_type]
    conversion_factor_to = units_to_joules[to_type]
    
    converted_value = value * (conversion_factor_to / conversion_factor_from)
    return converted_value

# Add unit tests in the docstring