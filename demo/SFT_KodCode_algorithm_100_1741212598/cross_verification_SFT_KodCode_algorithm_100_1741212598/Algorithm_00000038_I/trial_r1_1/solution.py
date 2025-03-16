from typing import List

def generate_all_subsequences(sequence: List[int]) -> None:
    """
    Generates and prints all possible subsequences of the given sequence using a backtracking algorithm.
    
    :param sequence: A list of integers.
    """
    result = []
    
    def backtrack(start, current_path):
        # Add the current path to the result list
        result.append(current_path.copy())
        # Iterate through each possible starting index
        for i in range(start, len(sequence)):
            # Include the current element in the path
            current_path.append(sequence[i])
            # Recur for the next index
            backtrack(i + 1, current_path)
            # Backtrack: remove the current element from the path
            current_path.pop()
    
    # Start the backtracking process with an empty path and index 0
    backtrack(0, [])
    # Sort the result lexicographically
    result.sort()
    # Print each subsequence
    for subseq in result:
        print(subseq)