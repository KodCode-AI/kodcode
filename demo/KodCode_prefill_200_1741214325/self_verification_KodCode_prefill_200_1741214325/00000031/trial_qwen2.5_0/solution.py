def find_closest_element(arr, target):
    """
    Given an almost sorted array and a target value, finds the index of the element 
    in the array which is closest to the target value. An almost sorted array is 
    defined as an array where each element is no more than two positions away from 
    its sorted position.
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if mid - 2 >= 0 and arr[mid - 2] == target:
            return mid - 2
        elif mid + 2 < len(arr) and arr[mid + 2] == target:
            return mid + 2
        elif arr[mid - 1] == target:
            return mid - 1
        elif arr[mid + 1] == target:
            return mid + 1
        elif mid - 1 >= 0 and mid + 2 < len(arr):
            if abs(target - arr[mid - 1]) < abs(target - arr[mid + 1]):
                right = mid - 1
            else:
                left = mid + 1
        elif mid - 1 >= 0:
            left = mid + 1
        elif mid + 2 < len(arr):
            right = mid - 1
        else:
            break
    # If the target is not found, return the closest value (based on index distance to target)
    closest_diff = min(abs(arr[left] - target), abs(arr[right] - target))
    return left if closest_diff == abs(arr[left] - target) else right