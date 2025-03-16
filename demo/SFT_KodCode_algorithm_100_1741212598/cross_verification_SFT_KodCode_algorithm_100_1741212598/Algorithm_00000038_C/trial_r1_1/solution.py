from typing import List

def generate_all_subsequences(sequence: List[int]) -> None:
    """
    Generates and prints all possible subsequences of the given sequence using a backtracking algorithm.
    
    :param sequence: A list of integers.
    """
    def backtrack(start, current):
        print(current)
        for i in range(start, len(sequence)):
            # Add the element at index i to the current subsequence
            current.append(sequence[i])
            # Recurse with the next element
            backtrack(i + 1, current.copy())  # Use copy to avoid modifying the same subsequence
            # Remove the last element to explore other subsequences
            current.pop()
    
    backtrack(0, [])

sequence = [1, 2, 3]
generate_all_subsequences(sequence)