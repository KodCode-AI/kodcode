from collections import Counter

def find_common_elements(a, b):
    count_b = Counter(b)
    result = []
    for elem in a:
        if count_b.get(elem, 0) > 0:
            result.append(elem)
            count_b[elem] -= 1
    return result