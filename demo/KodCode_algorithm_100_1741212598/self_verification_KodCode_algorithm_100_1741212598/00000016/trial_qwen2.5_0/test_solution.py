from solution import *

from solution import enhanced_builtin_voltage

def test_enhanced_builtin_voltage():
    # Test with default temperature
    assert abs(enhanced_builtin_voltage(donor_conc=1e17, acceptor_conc=1e17, intrinsic_conc=1e10) - 0.833370010652644) < 1e-6
    # Test with different temperature
    assert abs(enhanced_builtin_voltage(donor_conc=1000, acceptor_conc=3000, intrinsic_conc=2000, temperature=400) - 1.7257443376740775) < 1e-6
    # Test edge case: minimum temperature
    assert abs(enhanced_builtin_voltage(donor_conc=1e13, acceptor_conc=1e13, intrinsic_conc=1e10, temperature=100) - 0.0742222044226079) < 1e-6
    # Test edge case: maximum temperature
    assert abs(enhanced_builtin_voltage(donor_conc=1e13, acceptor_conc=1e13, intrinsic_conc=1e10, temperature=1000) - 0.2562434251524992) < 1e-6

def test_enhanced_builtin_voltage_invalid_inputs():
    # Test with invalid donor concentration
    try:
        enhanced_builtin_voltage(donor_conc=-1e17, acceptor_conc=1e17, intrinsic_conc=1e10)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative donor_conc"
    
    # Test with invalid acceptor concentration
    try:
        enhanced_builtin_voltage(donor_conc=1e17, acceptor_conc=-1e17, intrinsic_conc=1e10)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative acceptor_conc"
    
    # Test with invalid intrinsic concentration
    try:
        enhanced_builtin_voltage(donor_conc=1e17, acceptor_conc=1e17, intrinsic_conc=-1e10)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for negative intrinsic_conc"
    
    # Test with invalid temperature
    try:
        enhanced_builtin_voltage(donor_conc=1e17, acceptor_conc=1e17, intrinsic_conc=1e10, temperature=50)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for temperature < 100 K"
    
    try:
        enhanced_builtin_voltage(donor_conc=1e17, acceptor_conc=1e17, intrinsic_conc=1e10, temperature=1050)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for temperature > 1000 K"
    
    # Test with donor and acceptor less than intrinsic concentration
    try:
        enhanced_builtin_voltage(donor_conc=1e10, acceptor_conc=1e10, intrinsic_conc=1e10)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for donor_conc == intrinsic_conc"
    
    # Test with acceptor_conc < intrinsic_conc
    try:
        enhanced_builtin_voltage(donor_conc=1e13, acceptor_conc=1e10, intrinsic_conc=1e12)
    except ValueError:
        pass
    else:
        assert False, "Expected ValueError for acceptor_conc < intrinsic_conc"

# Run the tests
test_enhanced_builtin_voltage()
test_enhanced_builtin_voltage_invalid_inputs()