import heapq

def merge_sorted_lists(lst1, lst2):
    """
    Merges two sorted lists into one sorted list using the heapq.merge function.
    
    Parameters:
    lst1 (list): First sorted list.
    lst2 (list): Second sorted list.
    
    Returns:
    list: Merged and sorted list.
    """
    # Ensure both lists are sorted
    sorted_lst1 = sorted(lst1) if lst1 else []
    sorted_lst2 = sorted(lst2) if lst2 else []
    # Merge the sorted lists using heapq.merge and convert the result to a list
    merged_list = list(heapq.merge(sorted_lst1, sorted_lst2))
    return merged_list