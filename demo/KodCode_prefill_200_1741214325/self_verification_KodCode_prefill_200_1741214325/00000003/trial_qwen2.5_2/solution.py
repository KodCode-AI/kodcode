import heapq

def merge_sorted_lists(lst1, lst2):
    """
    Given two sorted lists, it merges them into a single sorted list
    using the heapq.merge function.
    """
    # Ensure both lists are sorted
    sorted_lst1 = sorted(lst1)
    sorted_lst2 = sorted(lst2)
    
    # Use heapq.merge to merge the two sorted lists
    result = list(heapq.merge(sorted_lst1, sorted_lst2))
    
    return result