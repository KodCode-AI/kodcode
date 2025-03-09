def energy_conversion(from_type, to_type, value):
    """
    Converts between different energy units. The function supports the new unit
    "electronvolt_per_photon" and includes robust error handling.

    Parameters:
    - from_type (str): The unit to convert from.
    - to_type (str): The unit to convert to.
    - value (float): The value to convert.

    Returns:
    - float: The converted value.

    Supported units:
    - joule, wattsecond, electronvolt, electronvolt_per_photon

    Raises:
    - ValueError: If an invalid unit is provided.
    """
    conversion_factors = {
        "joule": 1.0,
        "wattsecond": 1.0,
        "electronvolt": 1.602176634e-19,
        "electronvolt_per_photon": 6.241509074460763e+15,
    }

    if from_type not in conversion_factors or to_type not in conversion_factors:
        raise ValueError(f"Invalid unit conversion from {from_type} to {to_type}")

    factor_from = conversion_factors[from_type]
    factor_to = conversion_factors[to_type]

    if from_type == to_type:
        return value

    if "electronvolt_per_photon" in [from_type, to_type]:
        if from_type == "electronvolt_per_photon":
            factor_from *= 6.241509074460763e+15
        else:
            factor_to *= 1.602176634e-19 / 6.241509074460763e+15

    return (value * factor_from) / factor_to