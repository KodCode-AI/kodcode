from solution import *

import pytest
from solution import enhanced_builtin_voltage

def test_enhanced_builtin_voltage_basic():
    assert pytest.approx(enhanced_builtin_voltage(donor_conc=1e17, acceptor_conc=1e17, intrinsic_conc=1e10, temperature=300), rel=1e-3) == 0.833370010652644
    assert pytest.approx(enhanced_builtin_voltage(donor_conc=1000, acceptor_conc=3000, intrinsic_conc=2000, temperature=400), rel=1e-3) == 1.7257443376740775

def test_enhanced_builtin_voltage_acceptor_zero():
    with pytest.raises(ValueError):
        enhanced_builtin_voltage(donor_conc=1000, acceptor_conc=0, intrinsic_conc=1000, temperature=300)

def test_enhanced_builtin_voltage_concentration_outside_range():
    with pytest.raises(ValueError):
        enhanced_builtin_voltage(donor_conc=1e19, acceptor_conc=1e18, intrinsic_conc=1e10, temperature=300)

def test_enhanced_builtin_voltage_temperature_outside_range():
    with pytest.raises(ValueError):
        enhanced_builtin_voltage(donor_conc=1000, acceptor_conc=3000, intrinsic_conc=2000, temperature=100)
    with pytest.raises(ValueError):
        enhanced_builtin_voltage(donor_conc=1000, acceptor_conc=3000, intrinsic_conc=2000, temperature=1000)

def test_enhanced_builtin_voltage_concentration_order():
    with pytest.raises(ValueError):
        enhanced_builtin_voltage(donor_conc=1000, acceptor_conc=1000, intrinsic_conc=2000, temperature=300)