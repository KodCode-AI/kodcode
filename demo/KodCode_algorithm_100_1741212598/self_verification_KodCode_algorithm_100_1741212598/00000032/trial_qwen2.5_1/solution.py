def collatz_sequence_length(n):
    """
    Returns the length of the Collatz sequence starting from n.
    """
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def find_longest_collatz_sequence(n):
    """
    Returns the starting number under n that produces the longest Collatz sequence.
    """
    max_length = 0
    starting_number = 0
    for i in range(1, n):
        length = collatz_sequence_length(i)
        if length > max_length:
            max_length = length
            starting_number = i
    return starting_number