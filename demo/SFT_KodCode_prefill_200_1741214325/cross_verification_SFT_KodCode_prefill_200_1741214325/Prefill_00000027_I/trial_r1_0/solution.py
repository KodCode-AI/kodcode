def union_of_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    union_set = set1.union(set2)
    return list(union_set)