def find_min_element(lst):
    if not lst:
        raise ValueError("List is empty")
    return min(lst)