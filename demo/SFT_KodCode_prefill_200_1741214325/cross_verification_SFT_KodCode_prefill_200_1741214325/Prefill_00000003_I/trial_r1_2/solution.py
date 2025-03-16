import heapq

def merge_sorted_lists(a, b):
    sorted_a = sorted(a)
    sorted_b = sorted(b)
    merged = list(heapq.merge(sorted_a, sorted_b))
    return merged