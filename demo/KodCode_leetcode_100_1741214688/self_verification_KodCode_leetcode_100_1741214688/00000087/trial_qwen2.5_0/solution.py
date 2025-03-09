def exist(board, word):
    """
    Check if a word can be constructed from the given board of characters.
    """
    if not board or not board[0]:
        return False
    m, n = len(board), len(board[0])
    
    def dfs(x, y, word):
        if len(word) == 0:
            return True
        if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[0]:
            return False
        tmp, board[x][y] = board[x][y], '#'  # Mark the cell as visited
        found = dfs(x+1, y, word[1:]) or dfs(x-1, y, word[1:]) or dfs(x, y+1, word[1:]) or dfs(x, y-1, word[1:])
        board[x][y] = tmp  # Revert the change for backtracking
        return found
    
    for i in range(m):
        for j in range(n):
            if dfs(i, j, word):
                return True
    return False