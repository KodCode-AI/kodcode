def comb_sort(data: list) -> list:
    """
    Sorts a list of integers in ascending order using the comb sort algorithm.
    The function handles edge cases such as empty lists and single-element lists.
    """
    if not data:
        return data

    gap = len(data)
    shrink_factor = 1.3
    sorted = False

    while not sorted:
        # Update the gap value for the next comb
        gap = int(gap / shrink_factor)
        if gap > 1:
            sorted = False  # We are not done yet
        else:
            gap = 1
            sorted = True  # If there are no swaps this pass, we are done

        # A single "comb" over the input list
        for i in range(0, len(data) - gap):
            if data[i] > data[i + gap]:
                # Swap the elements
                data[i], data[i + gap] = data[i + gap], data[i]
                sorted = False

    return data