from typing import List

def generate_all_subsequences(sequence: List[int]) -> None:
    """
    Generates and prints all possible non-empty subsequences of the given sequence using a backtracking algorithm.
    
    :param sequence: A list of integers.
    """
    def backtrack(start, current):
        if current:  # Only print if the subsequence is non-empty
            print(current)
        for i in range(start, len(sequence)):
            current.append(sequence[i])
            backtrack(i + 1, current.copy())
            current.pop()
    
    backtrack(0, [])

sequence = [1, 2, 3]
generate_all_subsequences(sequence)