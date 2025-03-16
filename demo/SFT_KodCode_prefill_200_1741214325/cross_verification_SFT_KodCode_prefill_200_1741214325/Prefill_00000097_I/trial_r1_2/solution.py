def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for element in lst:
        if element not in seen:
            result.append(element)
            seen.add(element)
    return result