from solution import *

import pytest

def test_circular_array_initialization():
    ca = CircularArray(4)
    assert ca.to_string() == '[0, 0, 0, 0]'

def test_set_and_get():
    ca = CircularArray(4)
    ca.set(1, 10)
    ca.set(3, 20)
    assert ca.get(1) == 10
    assert ca.get(3) == 20

def test_wrap_around_set():
    ca = CircularArray(4)
    ca.set(3, 10)
    ca.set(4, 20)
    assert ca.to_string() == '[0, 0, 0, 20]'

def test_wrap_around_get():
    ca = CircularArray(4)
    ca.set(0, 10)
    ca.set(3, 20)
    assert ca.get(3) == 20
    assert ca.get(4) == 10

def test_increment():
    ca = CircularArray(4)
    ca.set(1, 10)
    ca.increment(1, 5)
    assert ca.get(1) == 15

def test_to_string():
    ca = CircularArray(4)
    ca.set(1, 10)
    ca.set(2, 20)
    ca.set(3, 30)
    assert ca.to_string() == '[0, 10, 20, 30]'