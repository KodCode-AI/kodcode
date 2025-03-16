from typing import List

def generate_all_subsequences(sequence: List[int]) -> None:
    """
    Generates and prints all possible subsequences of the given sequence using a backtracking algorithm.
    
    :param sequence: A list of integers.
    """
    result = []
    n = len(sequence)
    
    def backtrack(start, current_path):
        if start == n:
            result.append(current_path.copy())
            return
        # Include the current element
        current_path.append(sequence[start])
        backtrack(start + 1, current_path)
        current_path.pop()
        # Exclude the current element
        backtrack(start + 1, current_path)
    
    backtrack(0, [])
    
    # Sort the result lexicographically
    sorted_result = sorted(result)
    
    # Print each subsequence
    for subset in sorted_result:
        print(subset)