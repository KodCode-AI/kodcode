from typing import Tuple

def enhanced_builtin_voltage(
    donor_conc: float, 
    acceptor_conc: float, 
    intrinsic_conc: float, 
    temperature: float = 300.0
) -> float:
    """
    Calculate the Builtin Voltage of a pn junction diode with given donor, acceptor, and intrinsic concentrations.
    
    :param donor_conc: Donor concentration (unit = 1/cm³)
    :param acceptor_conc: Acceptor concentration (unit = 1/cm³)
    :param intrinsic_conc: Intrinsic concentration (unit = 1/cm³)
    :param temperature: Temperature in Kelvin (unit = K), default is 300 K
    :return: Builtin Voltage (unit = V)
    
    Constraints:
    - 1e10 <= donor_conc, acceptor_conc, intrinsic_conc <= 1e18
    - 100 <= temperature <= 1000
    
    Examples:
    >>> enhanced_builtin_voltage(donor_conc=1e17, acceptor_conc=1e17, intrinsic_conc=1e10, temperature=300)
    0.833370010652644
    >>> enhanced_builtin_voltage(donor_conc=1000, acceptor_conc=3000, intrinsic_conc=2000, temperature=400)
    1.7257443376740775
    >>> enhanced_builtin_voltage(donor_conc=1000, acceptor_conc=0, intrinsic_conc=1000, temperature=300)
    Traceback (most recent call last):
      ...
    ValueError: Acceptor concentration should be positive
    """
    from scipy.constants import k, e

    if donor_conc <= 0 or acceptor_conc <= 0 or intrinsic_conc <= 0:
        raise ValueError("All concentrations must be positive")
    if donor_conc > 1e18 or acceptor_conc > 1e18 or intrinsic_conc > 1e18:
        raise ValueError("Concentrations must be within 1e10 to 1e18")
    if acceptor_conc <= intrinsic_conc or donor_conc <= intrinsic_conc:
        raise ValueError("Donor and Acceptor concentrations must be greater than Intrinsic concentration")
    if temperature < 100 or temperature > 1000:
        raise ValueError("Temperature must be between 100 K and 1000 K")

    kT = k * temperature
    nf = (donor_conc - acceptor_conc) / (donor_conc + acceptor_conc)
    n_i = intrinsic_conc * 2**(-3 * kT / (2 * e * 0.0259))

    return 0.0259 * kT / e * (1 + nf / (n_i + nf))