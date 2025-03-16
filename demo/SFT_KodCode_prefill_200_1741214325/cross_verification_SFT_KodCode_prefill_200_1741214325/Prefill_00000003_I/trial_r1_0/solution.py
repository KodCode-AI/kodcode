import heapq

def merge_sorted_lists(list1, list2):
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    merged_iterator = heapq.merge(sorted_list1, sorted_list2)
    return list(merged_iterator)