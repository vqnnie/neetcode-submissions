from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_boxes = defaultdict(set) # key = (r // 3, c // 3)

        # sudoku board is 9 x 9
        for r in range(9):
            for c in range(9):
                # continue iterating if there is an empty space
                if board[r][c] == ".": # "." indicates an empty space
                    continue

                # check if we found a duplicate, if yes then return False
                # a sudoku board is not valid if it contains duplicates within the 3 conditions
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in sub_boxes[r // 3, c // 3]): # tells us the current square we're in
                        return False

                # continue iterating and update each hashset by adding what we've already seen to the current row/col/sub-box we're in
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                sub_boxes[r // 3, c // 3].add(board[r][c])
                
        return True
