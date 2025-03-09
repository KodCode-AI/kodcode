from solution import *

import pytest
import numpy as np

def f(x, y):
    return x + y

def test_runge_kutta_fehlberg_45():
    y = runge_kutta_fehlberg_45(f, 0, 0, 0.1, 1)
    expected_y = np.array([0.0, 0.1000000, 0.2050000, 0.3155000, 0.4322500, 0.5567850,
                           0.6893645, 0.8299954, 0.9787949, 1.1368744, 1.3044619,
                           1.4817353, 1.6697973, 1.8690473, 2.0797837, 2.2922042,
                           2.5164144, 2.7526104, 2.9999999, 3.2586794, 3.5287373,
                           3.8091737, 4.0999999, 4.3922139, 4.6857134, 4.9804931,
                           5.2765510, 5.5738847, 5.8725032, 6.1723043, 6.4732858,
                           6.7754467, 7.0787847, 7.3833074, 7.6889137, 8.0000000])
    np.testing.assert_allclose(y, expected_y, rtol=1e-5)

def test_invalid_step_size():
    with pytest.raises(ValueError):
        runge_kutta_fehlberg_45(f, 0, 0, -0.1, 1)

def test_invalid_x_final():
    with pytest.raises(ValueError):
        runge_kutta_fehlberg_45(f, 0, 0, 0.1, 0)

def test_zero_step_size():
    with pytest.raises(ValueError):
        runge_kutta_fehlberg_45(f, 0, 0, 0, 1)