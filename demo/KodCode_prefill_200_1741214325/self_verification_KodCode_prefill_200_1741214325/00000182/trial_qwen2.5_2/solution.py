def find_subsets(s: set):
    """
    Returns all possible subsets of a given set s as a list of lists.
    """
    subsets = [[]]
    for elem in s:
        # For each element in the set, create new subsets by adding the element to existing subsets.
        new_subsets = [subset + [elem] for subset in subsets]
        subsets.extend(new_subsets)
    return subsets