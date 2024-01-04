# 36. Valid Sudoku
# Medium
# 10.1K
# 1.1K
# Companies

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#     Each row must contain the digits 1-9 without repetition.
#     Each column must contain the digits 1-9 without repetition.
#     Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:

#     A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     Only the filled cells need to be validated according to the mentioned rules.

 

# Example 1:

# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

 

# Constraints:

#     board.length == 9
#     board[i].length == 9
#     board[i][j] is a digit 1-9 or '.'.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        VALID_NUMBER = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        VALID_INPUTS = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}

        
        def check_row(row):
            filled_row = list(filter(lambda x: x in VALID_NUMBER, row))
            rowvals = set(row) - {'.'}
            # validate
            if rowvals - VALID_INPUTS:
                return False
            if len(rowvals) != len(filled_row):
                return False
            
            return True
        
        def build_columns(board):
            cols = [ [] ] * len(board[0])
            for i in range(len(cols)):
                for row in board:
                    cols[i] = cols[i] + [row[i]]
            return cols


        def build_grids(board):
            grids = [ [] ] * 9
            for i in range(len(grids)):
                start = (i*3 % 9, i // 3 * 3)
                for row in board[start[1]:start[1]+3]:
                    grids[i] = grids[i] + row[start[0]:start[0]+3]
            return grids
        for row in board:
            if check_row(row) is False:
                return False

        for column in build_columns(board):
            if check_row(column) is False:
                return False
        
        for grid in build_grids(board):
            if check_row(grid) is False:
                return False
        
        return True
