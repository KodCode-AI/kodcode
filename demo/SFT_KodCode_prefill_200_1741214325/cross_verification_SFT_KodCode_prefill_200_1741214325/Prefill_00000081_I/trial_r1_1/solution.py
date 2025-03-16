from collections import Counter

def count_unique_elements(lst):
    if not lst:
        return 0
    counts = Counter(lst)
    return sum(1 for count in counts.values() if count == 1)