from solution import *

def test_remove_duplicates_preserve_order():
    assert remove_duplicates_preserve_order([1, 2, 3, 1, 2, 5]) == [1, 2, 3, 5]
    assert remove_duplicates_preserve_order(['a', 'b', 'a', 'c', 'b']) == ['a', 'b', 'c']
    assert remove_duplicates_preserve_order([1, 1, 1, 1, 1]) == [1]
    assert remove_duplicates_preserve_order([]) == []
    assert remove_duplicates_preserve_order([5, 4, 3, 2, 1, 4, 3]) == [5, 4, 3, 2, 1]

def test_remove_duplicates_with_duplicates_inside_tuple():
    # This tests for a potential pitfall with immutable types, where a mutable object might be stored in the list.
    test_list = [1, (2, 3), 'a', (2, 3), 'b', 1]
    expected_result = [1, (2, 3), 'a', 'b']
    assert remove_duplicates_preserve_order(test_list) == expected_result

def test_remove_duplicates_with_tuple_elements_in_list():
    # Test with a list that contains tuples
    test_list = [(1,), (2,), (1,), (3,), (2,)]
    expected_result = [(1,), (2,), (3,)]
    assert remove_duplicates_preserve_order(test_list) == expected_result