import heapq

def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into one sorted list.
    """
    # Ensure the lists are sorted
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    # Merge the sorted lists using heapq.merge and convert the result to a list
    merged_list = list(heapq.merge(sorted_list1, sorted_list2))
    return merged_list