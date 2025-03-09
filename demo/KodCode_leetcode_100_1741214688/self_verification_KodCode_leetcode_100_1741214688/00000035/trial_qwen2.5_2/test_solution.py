from solution import *

import pytest
from typing import List

def test_maxGCD():
    assert maxGCD([2, 3, 5, 7], 1) == 1
    assert maxGCD([6, 9, 3, 15], 3) == 3
    assert maxGCD([30, 60, 120, 60], 10) == 60
    assert maxGCD([5, 7, 11], 2) == 1
    assert maxGCD([10, 10, 10], 1) == 10