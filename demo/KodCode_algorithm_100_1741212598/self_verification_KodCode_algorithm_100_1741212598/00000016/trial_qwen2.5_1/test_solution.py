from solution import *

from solution import enhanced_builtin_voltage

def test_enhanced_builtin_voltage():
    assert abs(enhanced_builtin_voltage(1e17, 1e17, 1e10) - 0.833370010652644) < 1e-9
    assert abs(enhanced_builtin_voltage(1000, 3000, 2000, 400) - 1.7257443376740775) < 1e-9
    with pytest.raises(ValueError):
        enhanced_builtin_voltage(1000, 0, 1000, 300)
    with pytest.raises(ValueError):
        enhanced_builtin_voltage(1e12, 1e16, 1e15, 300)
    with pytest.raises(ValueError):
        enhanced_builtin_voltage(1e17, 1e17, 1e10, 50)
    with pytest.raises(ValueError):
        enhanced_builtin_voltage(1e17, 1e17, 1e10, 1100)