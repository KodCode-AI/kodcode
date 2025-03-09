from typing import Tuple
import math
from scipy.constants import k, e  # Boltzmann constant and elementary charge

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
    if not (1e10 <= donor_conc <= 1e18 and 1e10 <= acceptor_conc <= 1e18 and 1e10 <= intrinsic_conc <= 1e18):
        raise ValueError("Concentrations should be between 1e10 and 1e18")
    if acceptor_conc <= intrinsic_conc:
        raise ValueError("Acceptor concentration should be greater than intrinsic concentration")
    if donor_conc <= intrinsic_conc:
        raise ValueError("Donor concentration should be greater than intrinsic concentration")
    
    if temperature < 100 or temperature > 1000:
        raise ValueError("Temperature should be between 100 and 1000 K")
    
    n0 = math.sqrt(donor_conc * acceptor_conc)
    Vp = (k * temperature) / (e * math.log(n0 / intrinsic_conc))
    
    return Vp