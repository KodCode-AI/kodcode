from solution import *

from solution import celsius_to_fahrenheit

def test_celsius_to_fahrenheit_freezing_point():
    assert celsius_to_fahrenheit(0) == 32

def test_celsius_to_fahrenheit_boiling_point():
    assert celsius_to_fahrenheit(100) == 212

def test_celsius_to_fahrenheit_room_temperature():
    assert celsius_to_fahrenheit(25) == 77

def test_celsius_to_fahrenheit_negative_temperature():
    assert celsius_to_fahrenheit(-40) == -40

def test_celsius_to_fahrenheit_float_temperature():
    assert celsius_to_fahrenheit(23.5) == 74.3