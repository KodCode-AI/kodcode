def exist(board, word):
    """
    Determines if the word can be constructed from letters on the board.
    :param board: List[List[str]] representing the grid.
    :param word: str representing the word to find.
    :return: bool indicating whether the word can be formed.
    """
    def dfs(board, row, col, word, index):
        if index == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[index]:
            return False
        
        temp, board[row][col] = board[row][col], ''  # Mark as visited
        found = dfs(board, row + 1, col, word, index + 1) or \
                dfs(board, row - 1, col, word, index + 1) or \
                dfs(board, row, col + 1, word, index + 1) or \
                dfs(board, row, col - 1, word, index + 1)
        board[row][col] = temp  # Unmark for future iterations
        return found
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word, 0):
                return True
    return False