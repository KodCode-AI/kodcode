def union_of_lists(l1, l2):
    seen = set()
    result = []
    for elem in l1:
        if elem not in seen:
            result.append(elem)
            seen.add(elem)
    for elem in l2:
        if elem not in seen:
            result.append(elem)
            seen.add(elem)
    return result