from solution import *

from solution import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
    assert round(celsius_to_fahrenheit(0), 2) == 32.00

def test_celsius_to_fahrenheit_positive():
    assert round(celsius_to_fahrenheit(100), 2) == 212.00

def test_celsius_to_fahrenheit_negative():
    assert round(celsius_to_fahrenheit(-40), 2) == -40.00

def test_celsius_to_fahrenheit_half():
    assert round(celsius_to_fahrenheit(-273.15), 2) == -459.67