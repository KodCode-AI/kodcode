def find_first_unique(arr):
    # Count the frequency of each element
    frequency = {}
    for num in arr:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # Find the first element with frequency 1
    for num in arr:
        if frequency[num] == 1:
            return num
    return -1