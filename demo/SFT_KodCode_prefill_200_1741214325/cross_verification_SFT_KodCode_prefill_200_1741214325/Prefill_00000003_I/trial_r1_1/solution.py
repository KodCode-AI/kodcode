import heapq

def merge_sorted_lists(a, b):
    # Check if list a is sorted in ascending order
    is_a_sorted = True
    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            is_a_sorted = False
            break
    if not is_a_sorted:
        a = sorted(a)
    
    # Check if list b is sorted in ascending order
    is_b_sorted = True
    for i in range(len(b) - 1):
        if b[i] > b[i + 1]:
            is_b_sorted = False
            break
    if not is_b_sorted:
        b = sorted(b)
    
    # Merge the sorted lists using heapq.merge()
    merged_iterator = heapq.merge(a, b)
    
    # Convert the iterator to a list and return
    return list(merged_iterator)