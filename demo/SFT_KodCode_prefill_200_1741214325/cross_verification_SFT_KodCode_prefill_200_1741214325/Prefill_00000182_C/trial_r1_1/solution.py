from typing import Set, List

def find_subsets(s: Set[int]) -> List[List[int]]:
    elements = list(s)
    subsets = [ [] ]
    for e in elements:
        temp = []
        for subset in subsets:
            new_subset = subset.copy()
            new_subset.append(e)
            temp.append(new_subset)
        subsets += temp
    return subsets