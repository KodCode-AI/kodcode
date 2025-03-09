def collatz_sequence_length(start):
    """
    Returns the length of the Collatz sequence starting from `start`.
    """
    length = 1
    while start != 1:
        if start % 2 == 0:
            start = start // 2
        else:
            start = 3 * start + 1
        length += 1
    return length

def find_longest_collatz_sequence(limit):
    """
    Returns the starting number under `limit` that produces the longest Collatz sequence.
    """
    max_length = 0
    number_with_max_length = 0
    for i in range(1, limit):
        length = collatz_sequence_length(i)
        if length > max_length:
            max_length = length
            number_with_max_length = i
    return number_with_max_length