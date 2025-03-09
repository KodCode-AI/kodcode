def collatz_sequence_length(n, cache={1: 1}):
    """
    Returns the length of the Collatz sequence starting from n.
    Cache is used to store previously computed lengths for efficiency.
    """
    if n in cache:
        return cache[n]
    if n % 2 == 0:
        cache[n] = 1 + collatz_sequence_length(n // 2)
    else:
        cache[n] = 2 + collatz_sequence_length((n - 1) // 2)
    return cache[n]

def find_longest_collatz_sequence(limit):
    """
    Finds the starting number under limit that produces the longest Collatz sequence.
    """
    longest_sequence = 0
    starting_number = 0
    for i in range(1, limit):
        length = collatz_sequence_length(i)
        if length > longest_sequence:
            longest_sequence = length
            starting_number = i
    return starting_number