from solution import *

from solution import max_distinct_elements

def test_max_distinct_elements():
    assert max_distinct_elements([1, 2, 1, 3, 4, 3], 3) == 3
    assert max_distinct_elements([1, 2, 1, 3, 4, 3], 5) == 4
    assert max_distinct_elements([1, 2, 1, 3, 4, 3], 6) == 6
    assert max_distinct_elements([1, 2, 3, 4, 5], 2) == 5
    assert max_distinct_elements([1, 2, 3, 4, 5], 3) == 4
    assert max_distinct_elements([1, 3, 1, 2, 2], 2) == 2
    assert max_distinct_elements([1], 1) == 1
    assert max_distinct_elements([], 5) == 0

def test_window_counter_logn_update():
    nums = [1, 2, 1, 3, 4, 3]
    k = 3
    window_counter = Counter()
    for i in range(k):
        window_counter[nums[i]] += 1
    # Check if the counter contains 3 distinct elements
    assert len(window_counter) == 3
    for i in range(k, len(nums)):
        window_counter[nums[i]] += 1
        window_counter[nums[i - k]] -= 1
        if window_counter[nums[i - k]] == 0:
            del window_counter[nums[i - k]]
        # Check if the counter contains the maximum possible distinct elements
        assert len(window_counter) in [2, 3]