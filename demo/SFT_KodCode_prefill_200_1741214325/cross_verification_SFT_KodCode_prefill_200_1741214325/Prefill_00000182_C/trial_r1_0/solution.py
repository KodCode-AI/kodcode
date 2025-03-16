from typing import List

def find_subsets(s: set) -> List[List[int]]:
    s_list = sorted(s)
    n = len(s_list)
    subsets = []
    for mask in range(2 ** n):
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(s_list[i])
        subsets.append(subset)
    return subsets