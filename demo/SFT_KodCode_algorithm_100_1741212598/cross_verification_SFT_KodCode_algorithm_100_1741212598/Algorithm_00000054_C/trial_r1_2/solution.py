from typing import List, Optional

def find_peak(lst: List[int]) -> Optional[int]:
    if not lst:
        return None

    max_val = max(lst)
    max_indices = [i for i, val in enumerate(lst) if val == max_val]

    for i in max_indices:
        # Check if elements before i are non-decreasing
        if i > 0:
            non_decreasing = True
            for j in range(i - 1):
                if lst[j] > lst[j + 1]:
                    non_decreasing = False
                    break
            if not non_decreasing:
                continue

        # Check if elements after i are non-increasing
        if i < len(lst) - 1:
            non_increasing = True
            for j in range(i, len(lst) - 1):
                if lst[j] < lst[j + 1]:
                    non_increasing = False
                    break
            if not non_increasing:
                continue

        return max_val

    return None