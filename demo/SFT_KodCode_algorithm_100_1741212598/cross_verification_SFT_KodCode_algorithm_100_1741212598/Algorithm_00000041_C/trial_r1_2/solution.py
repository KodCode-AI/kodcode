def quick_sort_in_place(arr: list) -> None:
    def helper(low, high):
        if low < high:
            # Partition the array
            i = low - 1
            pivot = arr[high]
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            # Swap the pivot element to its final position
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            pivot_index = i + 1
            # Recursively sort the sub-arrays
            helper(low, pivot_index - 1)
            helper(pivot_index + 1, high)
    
    if not arr:
        return
    helper(0, len(arr) - 1)