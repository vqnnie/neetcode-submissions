from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # input: 
        # output: boolean
        # edge cases: duplicates in each row, each column, and 3x3 sub-box

        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9): # sudoku covers digits
            for c in range(9):
                if (board[r][c] == "."): # ".", as shown in the example, indicates an empty box
                    continue
                if (board[r][c] in rows[r] 
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[r//3,c//3].add(board[r][c])
        return True