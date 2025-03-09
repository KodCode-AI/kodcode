def energy_conversion(from_type, to_type, value):
    """
    Converts energy units from one type to another.
    
    Parameters:
    - from_type (str): The unit to convert from.
    - to_type (str): The unit to convert to.
    - value (float): The numeric value to convert.
    
    Supported units:
    - joule
    - electronvolt
    - electronvolt_per_photon
    - wattsecond
    
    Returns:
    - float: The converted value.
    
    Raises:
    - ValueError: If an invalid unit is provided.
    """
    conversion_factors = {
        "joule": 1.0,
        "electronvolt": 1.602176634e-19,
        "electronvolt_per_photon": 6.241509074460763e+15,
        "wattsecond": 1.0
    }
    
    if from_type not in conversion_factors or to_type not in conversion_factors:
        raise ValueError(f"Invalid unit: from {from_type} to {to_type}. Supported units are {list(conversion_factors.keys())}")
    
    if from_type == to_type:
        return value
    
    conversion_factor_from = conversion_factors[from_type]
    conversion_factor_to = conversion_factors[to_type]
    
    return value * (conversion_factor_from / conversion_factor_to)