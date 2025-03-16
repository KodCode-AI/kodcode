def bubble_sort(lst):
    lst_copy = lst.copy()
    n = len(lst_copy)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if lst_copy[j] > lst_copy[j + 1]:
                lst_copy[j], lst_copy[j + 1] = lst_copy[j + 1], lst_copy[j]
                swapped = True
        if not swapped:
            break
    return lst_copy