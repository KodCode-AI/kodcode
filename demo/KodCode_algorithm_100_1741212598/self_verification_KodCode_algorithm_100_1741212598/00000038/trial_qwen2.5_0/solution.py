from typing import List

def generate_all_subsequences(sequence: List[int]) -> None:
    """
    Generates and prints all possible subsequences of the given sequence using a backtracking algorithm.
    
    :param sequence: A list of integers.
    """
    def backtrack(start, path):
        # Print the current path
        print(path)
        for i in range(start, len(sequence)):
            # Include the current element in the path
            backtrack(i + 1, path + [sequence[i]])
    
    backtrack(0, [])