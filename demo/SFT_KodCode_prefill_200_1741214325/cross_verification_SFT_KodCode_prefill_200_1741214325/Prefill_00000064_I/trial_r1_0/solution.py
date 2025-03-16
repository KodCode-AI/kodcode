def remove_duplicates(input_list):
    seen = set()
    result = []
    for element in input_list:
        if element not in seen:
            seen.add(element)
            result.append(element)
    return result

def test_remove_duplicates():
    # Test case 1: List with duplicates
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Test case 2: Empty list
    assert remove_duplicates([]) == []
    
    # Test case 3: All elements are unique
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    
    # Test case 4: Duplicate elements of different types
    assert remove_duplicates([1, 'a', 2, 'a', 1]) == [1, 'a', 2]
    
    # Test case 5: Duplicate elements including tuples
    assert remove_duplicates([(1, 2), (3, 4), (1, 2)]) == [(1, 2), (3, 4)]
    
    print("All test cases pass.")

# Run the test
test_remove_duplicates()