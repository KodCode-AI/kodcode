from solution import *

import math
from solution import calculate_circle_area

def test_circle_area():
    assert abs(calculate_circle_area(0) - 0) < 1e-6
    assert abs(calculate_circle_area(1) - math.pi) < 1e-6
    assert abs(calculate_circle_area(2) - (math.pi * 4)) < 1e-6
    assert abs(calculate_circle_area(5) - (math.pi * 25)) < 1e-6