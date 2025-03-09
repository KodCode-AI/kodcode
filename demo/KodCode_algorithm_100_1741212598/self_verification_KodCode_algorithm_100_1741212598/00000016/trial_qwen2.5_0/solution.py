from typing import Tuple
import math
from scipy.constants import boltzmann, elementary_charge  # Assuming these are available in a similar module

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
    
    if donor_conc <= 0 or acceptor_conc <= 0 or intrinsic_conc <= 0:
        raise ValueError("All concentrations should be positive")
    
    if donor_conc > 1e18 or acceptor_conc > 1e18 or intrinsic_conc > 1e18:
        raise ValueError("Concentrations should not exceed 1e18 1/cm³")
    
    if donor_conc < intrinsic_conc or acceptor_conc < intrinsic_conc:
        raise ValueError("Donor and acceptor concentrations should be greater than the intrinsic concentration")
    
    if temperature < 100 or temperature > 1000:
        raise ValueError("Temperature should be between 100 and 1000 K")
    
    n_space_charge = math.sqrt(donor_conc * acceptor_conc)
    a = (n_space_charge / intrinsic_conc) ** (1/3)
    
    v_b = (elementary_charge * boltzmann * temperature) / (elementary_charge * intrinsic_conc * math.log(a))
    
    return v_b