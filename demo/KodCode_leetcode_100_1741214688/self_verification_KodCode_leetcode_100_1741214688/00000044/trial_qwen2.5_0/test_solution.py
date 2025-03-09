from solution import *

def test_cheapest_itinerary():
    assert cheapest_itinerary([(0, 1, 100), (1, 2, 100), (2, 0, 100), (1, 2, 600)], [(0, 1), (1, 2)]) == 260
    assert cheapest_itinerary([(0,1,10),(1,2,100),(2,0,100),(1,2,100),(2,0,100)], [(0,1)]) == -1
    assert cheapest_itinerary([(0,1,100),(1,2,100),(2,0,100)], [(0,1),(1,2)]) == 200
    assert cheapest_itinerary([(0,1,100),(1,2,100),(2,0,100)], [(0,1),(2,0)]) == -1
    assert cheapest_itinerary([(1,2,5), (1,3,5), (3,2,5)], [(2,1)]) == -1