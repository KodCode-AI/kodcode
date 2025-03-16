from typing import List

def single_number(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result

# Example usage:
# print(single_number([2, 2, 1]))          # Output: 1
# print(single_number([4, 1, 2, 1, 2]))    # Output: 4
# print(single_number([8]))                # Output: 8
# print(single_number([7, 3, 5, 3, 7, 5, 6]))  # Output: 6