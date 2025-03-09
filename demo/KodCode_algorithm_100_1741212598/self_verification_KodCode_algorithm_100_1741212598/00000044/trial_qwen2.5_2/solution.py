def comb_sort(data: list) -> list:
    """
    Sorts a list of integers in ascending order using the comb sort algorithm.
    """
    if not data:
        return data

    gap = len(data)
    shrink_factor = 1.3
    sorted_flag = False

    while not sorted_flag:
        # Update the gap value for a next comb
        gap = int(gap / shrink_factor)
        if gap <= 1:
            gap = 1
            sorted_flag = True

        # A single "comb" over the input list
        for i in range(len(data) - gap):
            if data[i] > data[i + gap]:
                # Swap elements
                data[i], data[i + gap] = data[i + gap], data[i]
                sorted_flag = False

    return data