def remove_duplicates(input_list):
    """Remove duplicate elements from a list while preserving order."""
    seen = set()
    unique_list = []
    for element in input_list:
        if element not in seen:
            seen.add(element)
            unique_list.append(element)
    return unique_list

# Test case
def test_remove_duplicates():
    test_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
    expected_output = [1, 2, 3, 4, 5, 6]
    assert remove_duplicates(test_list) == expected_output, "Test failed: Output does not match expected."
    print("Test passed.")

test_remove_duplicates()