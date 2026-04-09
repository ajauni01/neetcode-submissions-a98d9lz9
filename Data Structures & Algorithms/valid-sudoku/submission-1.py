"""
Understand:
input: a list of strings
output: Boolean
constraints: board.length == 9 and board[i].length == 9 and board[i][j] is a digit 1-9 or '.'
edge cases: empty list of strings

Plan:
1. Address the constraints
2. Loop through the list
3. Find duplicates in the row and return false
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3,c//3]:
                        return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[r//3,c//3].add(board[r][c]) 
        return True           

        