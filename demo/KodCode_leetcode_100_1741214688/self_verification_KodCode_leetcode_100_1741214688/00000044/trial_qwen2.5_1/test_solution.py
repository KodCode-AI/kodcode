from solution import *

def test_cheapest_itinerary():
    # Test case 1: Basic case
    flights = [(0, 1, 100), (1, 2, 100), (2, 0, 100)]
    reservations = [(0, 1), (1, 2), (2, 0)]
    assert cheapest_itinerary(flights, reservations) == (300, [0, 1, 2])
    
    # Test case 2: No valid itininerary
    flights = [(0, 1, 100), (1, 2, 100), (2, 0, 100)]
    reservations = [(0, 2), (2, 1)]
    assert cheapest_itinerary(flights, reservations) == -1
    
    # Test case 3: Lexicographically smallest itinerary
    flights = [(0, 1, 100), (1, 2, 100), (2, 0, 100)]
    reservations = [(0, 1), (1, 2), (1, 2)]
    assert cheapest_itinerary(flights, reservations) == (200, [0, 1, 1, 2])

# To run the tests, use pytest