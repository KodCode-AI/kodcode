from typing import List

class DynamicArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
    
    def add(self, index: int, val: int) -> None:
        self.nums[index] += val
    
    def find(self, left: int, right: int) -> int:
        return max(self.nums[left:right+1])