def exist(board, word):
    """
    Check if the word can be constructed from the board.
    """
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
            return False
        board[r][c] = "#"  # Mark as visited
        res = (dfs(r+1, c, i+1) or
               dfs(r-1, c, i+1) or
               dfs(r, c+1, i+1) or
               dfs(r, c-1, i+1))
        board[r][c] = word[i]  # Restore the cell
        return res
    
    for r in range(rows):
        for c in range(cols):
            if dfs(r, c, 0):
                return True
    return False