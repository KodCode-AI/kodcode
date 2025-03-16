from typing import List

def generate_all_subsequences(sequence: List[int]) -> None:
    """
    Generates and prints all possible subsequences of the given sequence using a backtracking algorithm.
    
    :param sequence: A list of integers.
    """
    result = []
    
    def backtrack(start, current):
        if start == len(sequence):
            result.append(current.copy())
            return
        # Include the current element
        current.append(sequence[start])
        backtrack(start + 1, current)
        # Exclude the current element
        current.pop()
        backtrack(start + 1, current)
    
    backtrack(0, [])
    # Sort the result in lexicographical order
    result.sort()
    # Print each subsequence
    for subseq in result:
        print(subseq)