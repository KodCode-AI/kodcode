def find_subsets(s):
    if not s:
        return [[]]
    elements = list(s)
    n = len(elements)
    subsets = []
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(elements[j])
        subsets.append(subset)
    return subsets