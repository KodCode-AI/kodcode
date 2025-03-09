def comb_sort(data: list) -> list:
    """
    Sorts a list in ascending order using the comb sort algorithm.
    """
    gap = len(data)
    shrink = 1.3  # Common shrink factor
    sorted_flag = False

    while not sorted_flag:
        # Update the gap value for a next comb
        gap = int(gap / shrink)
        if gap > 1:
            sorted_flag = False
        else:
            gap = 1
            sorted_flag = True

        i = 0
        while i + gap < len(data):
            if data[i] > data[i + gap]:
                data[i], data[i + gap] = data[i + gap], data[i]
                sorted_flag = False
            i += 1

    return data