from typing import List

def find_subsets(nums: List[int]) -> List[List[int]]:
    """
    Returns all possible subsets of the given list of numbers.
    """
    subsets = [[]]
    for num in nums:
        subsets += [subset + [num] for subset in subsets]
    return subsets