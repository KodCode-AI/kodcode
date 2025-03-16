def binary_search(sorted_list, target):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif target < sorted_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1