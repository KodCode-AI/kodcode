from typing import List

def fibonacci(n: int) -> List[int]:
    """Returns the first n terms of the Fibonacci sequence.
    The Fibonacci sequence is a series of numbers where each number is the sum 
    of the two preceding ones, usually starting with 0 and 1.
    
    Parameters:
    n (int): The number of terms in the Fibonacci sequence to generate.
    
    Returns:
    list: A list containing the first n terms of the Fibonacci sequence.
    """
    if n == 0:
        return []
    elif n == 1:
        return [0]
    else:
        sequence = [0, 1]
        for i in range(2, n):
            next_num = sequence[i-1] + sequence[i-2]
            sequence.append(next_num)
        return sequence