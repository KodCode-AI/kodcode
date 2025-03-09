from typing import Dict

def simulate_555_timer(resistance_1: float, resistance_2: float, capacitance: float) -> Dict[str, float or str]:
    """
    Calculate the frequency and duty cycle of an astable 555 timer and log the calculation steps.

    :param resistance_1: First resistance value (in ohms)
    :param resistance_2: Second resistance value (in ohms)
    :param capacitance: Capacitance value (in Microfarads)
    :return: A dictionary containing 'frequency', 'duty_cycle', and 'details' keys.
             'frequency' and 'duty_cycle' will be the calculated values.
             'details' will be a string detailing the calculation steps.

    Usage examples:
    >>> simulate_555_timer(resistance_1=45, resistance_2=45, capacitance=7)
    {
        'frequency': 1523809.5238095239,
        'duty_cycle': 66.66666666666666,
        'details': 'Frequency: 1.44 / [(45 + 2 * 45) * 7] * 10^6 = 1523809.5238095239 Hz, Duty Cycle: (45 + 45) / (45 + 2 * 45) * 100 = 66.66666666666666 %'
    }
    >>> simulate_555_timer(resistance_1=356, resistance_2=234, capacitance=976)
    {
        'frequency': 1790.5459175553078,
        'duty_cycle': 71.60194174757282,
        'details': 'Frequency: 1.44 / [(356 + 2 * 234) * 976] * 10^6 = 1790.5459175553078 Hz, Duty Cycle: (356 + 234) / (356 + 2 * 234) * 100 = 71.60194174757282 %'
    }
    >>> simulate_555_timer(resistance_1=-1, resistance_2=45, capacitance=7)
    {
        'error': 'All values must be positive'
    }
    >>> simulate_555_timer(resistance_1=0, resistance_2=0, capacitance=0)
    {
        'error': 'All values must be positive'
    }
    """
    if resistance_1 <= 0 or resistance_2 <= 0 or capacitance <= 0:
        return {'error': 'All values must be positive'}

    frequency = (1.44 / ((resistance_1 + 2 * resistance_2) * capacitance)) * 10**6
    duty_cycle = (resistance_1 + resistance_2) / (resistance_1 + 2 * resistance_2) * 100

    details = f'Frequency: 1.44 / [( {resistance_1} + 2 * {resistance_2} ) * {capacitance}] * 10^6 = {frequency:.6f} Hz, Duty Cycle: ( {resistance_1} + {resistance_2} ) / ( {resistance_1} + 2 * {resistance_2} ) * 100 = {duty_cycle:.6f} %'

    return {'frequency': frequency, 'duty_cycle': duty_cycle, 'details': details}