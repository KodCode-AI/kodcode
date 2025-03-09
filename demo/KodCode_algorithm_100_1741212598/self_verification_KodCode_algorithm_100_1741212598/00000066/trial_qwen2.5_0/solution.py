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
    """
    if resistance_1 <= 0 or resistance_2 <= 0 or capacitance <= 0:
        return {'error': 'All values must be positive'}

    frequency = (1.44 / ((resistance_1 + 2 * resistance_2) * capacitance)) * 10**6
    duty_cycle = (resistance_1 + resistance_2) / (resistance_1 + 2 * resistance_2) * 100

    details = f'Frequency: 1.44 / [( {resistance_1} + 2 * {resistance_2} ) * {capacitance}] * 10^6 = {frequency:.6f} Hz, Duty Cycle: ( {resistance_1} + {resistance_2} ) / ( {resistance_1} + 2 * {resistance_2} ) * 100 = {duty_cycle:.6f} %'

    return {'frequency': frequency, 'duty_cycle': duty_cycle, 'details': details}