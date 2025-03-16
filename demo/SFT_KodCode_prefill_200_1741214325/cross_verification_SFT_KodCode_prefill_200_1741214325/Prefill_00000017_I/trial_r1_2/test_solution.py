from solution import *

from solution import celsius_to_fahrenheit

def test_celsius_to_fahrenheit_freezing_point():
    assert celsius_to_fahrenheit(0) == 32.0

def test_celsius_to_fahrenheit_boiling_point():
    assert celsius_to_fahrenheit(100) == 212.0

def test_celsius_to_fahrenheit_room_temperature():
    assert celsius_to_fahrenheit(25) == 77.0

def test_celsius_to_fahrenheit_negative_temperature():
    assert celsius_to_fahrenheit(-40) == -40.0

def test_celsius_to_fahrenheit_freezing_point_reverse():
    assert round(celsius_to_fahrenheit(0) - 32, 1) == 0  # Using round to allow for floating point precision issues