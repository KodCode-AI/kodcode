from solution import *

from solution import find_cheapest_itinerary

def test_find_cheapest_itinerary():
    assert find_cheapest_itinerary([("SFO", "ATL", 100), ("ATL", "SFO", 100), ("ATL", "NHM", 450), ("NHM", "ATL", 450), ("NHM", "EWR", 800)], [("SFO", "ATL"), ("ATL", "SFO")]) == 650
    assert find_cheapest_itinerary([("SFO", "ATL", 100), ("ATL", "SFO", 100), ("ATL", "NHM", 450), ("NHM", "ATL", 450), ("NHM", "EWR", 800)], [("SFO", "ATL"), ("ATL", "NHM")]) == 1300
    assert find_cheapest_itinerary([("SFO", "ATL", 100), ("ATL", "NHM", 450), ("NHM", "EWR", 800), ("EWR", "SFO", 500), ("ATL", "SFO", 100)], [("SFO", "ATL")]) == 650
    assert find_cheapest_itinerary([("SFO", "ATL", 100), ("ATL", "NHM", 450), ("NHM", "EWR", 800), ("EWR", "SFO", 500), ("ATL", "SFO", 100)], [("SFO", "ATL")], "SFO") == -1  # No valid itinerary
    assert find_cheapest_itinerary([("SFO", "ATL", 100), ("ATL", "NHM", 450), ("NHM", "EWR", 800)], [("SFO", "ATL"), ("ATL", "NHM"), ("NHM", "EWR")]) == 1800