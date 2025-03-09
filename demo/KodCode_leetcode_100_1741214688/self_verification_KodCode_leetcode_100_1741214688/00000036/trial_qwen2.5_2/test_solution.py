from solution import *

def test_min_flips_to_alternate():
    assert min_flips_to_alternate("00110") == 2, "Test case 1 failed"
    assert min_flips_to_alternate("10") == 1, "Test case 2 failed"
    assert min_flips_to_alternate("1111") == -1, "Test case 3 failed"
    assert min_flips_to_alternate("0101010") == 0, "Test case 4 failed"
    assert min_flips_to_alternate("111000") == 3, "Test case 5 failed"
    assert min_flips_to_alternate("00011110") == 4, "Test case 6 failed"
    print("All test cases passed!")

# Call the test function to run all the tests
test_min_flips_to_alternate()