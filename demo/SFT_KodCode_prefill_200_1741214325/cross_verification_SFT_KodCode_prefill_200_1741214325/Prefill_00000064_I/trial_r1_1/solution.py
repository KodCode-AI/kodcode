def remove_duplicates(input_list):
    seen = set()
    unique_list = []
    for item in input_list:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list

# Test cases
def test_remove_duplicates():
    # Test case 1: List with duplicates
    test_list1 = [1, 2, 2, 3, 4, 4, 5]
    expected_output1 = [1, 2, 3, 4, 5]
    assert remove_duplicates(test_list1) == expected_output1, "Test case 1 failed."

    # Test case 2: Empty list
    test_list2 = []
    expected_output2 = []
    assert remove_duplicates(test_list2) == expected_output2, "Test case 2 failed."

    # Test case 3: All elements are unique
    test_list3 = [5, 10, 15]
    expected_output3 = [5, 10, 15]
    assert remove_duplicates(test_list3) == expected_output3, "Test case 3 failed."

    # Test case 4: All elements are duplicates
    test_list4 = [5, 5, 5]
    expected_output4 = [5]
    assert remove_duplicates(test_list4) == expected_output4, "Test case 4 failed."

    print("All test cases passed.")

if __name__ == "__main__":
    test_remove_duplicates()