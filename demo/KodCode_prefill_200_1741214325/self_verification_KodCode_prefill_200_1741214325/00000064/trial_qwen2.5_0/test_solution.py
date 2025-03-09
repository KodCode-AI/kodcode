from solution import *

def test_remove_duplicates():
    # Test with a list that has duplicates
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Test with a list that has no duplicates
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Test with an empty list
    assert remove_duplicates([]) == []
    
    # Test with a list that has all the same elements
    assert remove_duplicates([1, 1, 1, 1, 1]) == [1]
    
    # Test with a list that has strings with duplicates
    assert remove_duplicates(["apple", "banana", "apple", "orange"]) == ["apple", "banana", "orange"]