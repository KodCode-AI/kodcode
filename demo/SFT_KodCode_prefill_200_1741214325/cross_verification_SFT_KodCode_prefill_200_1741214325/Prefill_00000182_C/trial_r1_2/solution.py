from typing import List

def find_subsets(s: set) -> List[List[int]]:
    if not s:
        return [ [] ]
    s_list = sorted(s)
    n = len(s_list)
    subsets = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(s_list[j])
        subsets.append(subset)
    return subsets