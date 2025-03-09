from typing import List, Optional

def find_peak(lst: List[int]) -> Optional[int]:
    """
    Find the peak element in a unimodal list.
    """
    if not lst:
        return None

    left, right = 0, len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if mid is the peak element
        if (mid == 0 or lst[mid - 1] < lst[mid]) and (mid == len(lst) - 1 or lst[mid] > lst[mid + 1]):
            return lst[mid]
        # If the middle element is smaller than the next element, the peak lies on the right half
        elif mid < len(lst) - 1 and lst[mid + 1] > lst[mid]:
            left = mid + 1
        # Otherwise, the peak lies on the left half
        else:
            right = mid - 1

    return None