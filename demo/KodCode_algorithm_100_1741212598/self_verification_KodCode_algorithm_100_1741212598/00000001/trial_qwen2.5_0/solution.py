def insertion_sort(arr, start, end):
    for i in range(start + 1, end + 1):
        key = arr[i]
        j = i - 1
        while j >= start and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def intro_sort(array, start, end, size_threshold, max_depth):
    max_depth -= 1
    if (end - start) < 1:
        return
    elif (end - start) < size_threshold:
        insertion_sort(array, start, end)
    elif max_depth < 0:
        from heapq import nlargest, nsmallest
        # Convert to minheap by negating elements
        neg_array = [-x for x in array[start:end+1]]
        heapq.heapify(neg_array)
        # Extract elements back to array
        for i in range(start, end + 1):
            array[i] = -heapq.heappop(neg_array)
    else:
        pivot = array[end]
        i = start - 1
        for j in range(start, end):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[end] = array[end], array[i + 1]
        p = i + 1
        intro_sort(array, start, p - 1, size_threshold, max_depth)
        intro_sort(array, p + 1, end, size_threshold, max_depth)