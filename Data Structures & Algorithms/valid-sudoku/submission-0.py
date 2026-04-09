"""
Understand =
input: 
output: boolean
constraints: board length cannot exceed 9 also any element of the board
cannot be more than 9 and any digit of the board must be from 1 to 9 or blank
edge cases:

Plan: 
1. Have a nested for loop
2. check for eacj column and row
3. handle the constraints
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       # Check row
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] != ".":
                    item = board[i][j]
                    if item in seen:
                        return False
                    else:
                        seen.add(item)

        # Check column
        for i in range(9):
            seen = set()
            for j in range(9):
                item = board[j][i]
                if item != ".":
                    if item in seen:
                        return False
                    else:
                        seen.add(item)


        for br in (0,3,6):
            for bc in (0,3,6):
                seen = set()
                for r in range(br, br+3):
                    for c in range(bc, bc+3):
                        if board[r][c] != ".":
                            item = board[r][c]
                            if item in seen:
                                return False
                            else:
                                seen.add(item)
        return True                                    



