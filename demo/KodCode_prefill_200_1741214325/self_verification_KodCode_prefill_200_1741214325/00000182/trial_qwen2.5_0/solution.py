from itertools import chain, combinations

def all_subsets(s):
    """
    Returns a list of all possible subsets of the input set s.
    """
    return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))