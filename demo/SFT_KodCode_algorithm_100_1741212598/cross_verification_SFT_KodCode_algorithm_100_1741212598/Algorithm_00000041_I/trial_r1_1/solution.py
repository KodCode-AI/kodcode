def quick_sort_in_place(arr: list) -> None:
    """
    Sorts the given list arr in-place using the quick sort algorithm.
    """
    if not arr:
        return

    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()
        if low >= high:
            continue

        mid = (low + high) // 2
        x, y, z = arr[low], arr[mid], arr[high]
        median_val = sorted([x, y, z])[1]

        if arr[low] == median_val:
            arr[low], arr[high] = arr[high], arr[low]
        elif arr[mid] == median_val:
            arr[mid], arr[high] = arr[high], arr[mid]

        pivot = arr[high]

        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pivot_idx = i + 1

        stack.append((pivot_idx + 1, high))
        stack.append((low, pivot_idx - 1))