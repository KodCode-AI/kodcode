def find_common_elements(list1, list2):
    seen = set()
    set2 = set(list2)
    result = []
    for element in list1:
        if element in set2 and element not in seen:
            result.append(element)
            seen.add(element)
    return result