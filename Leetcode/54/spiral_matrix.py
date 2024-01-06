# 54. Spiral Matrix
# Medium
# 14K
# 1.2K
# Companies

# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:

# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

 

# Constraints:

#     m == matrix[i].length
#     n == matrix.length
#     1 <= m, n <= 10
#     -100 <= matrix[i][j] <= 100

# The Hard Way:
class Solution:
    def spiralOrder(self, board: List[List[int]]) -> List[int]:
        
        def next(i, board):
            m = len(board[0])
            n = len(board)

            if i <= m:
                x = i-1
                y = 0
            elif i <= m + n - 1:
                x = m - 1
                y = i - m
            elif i <= m + m + n-2:
                x = -1 * (i - m - n + 2)
                y = n - 1
            elif i <= (m + n - 2) * 2:
                x = 0
                y = -1 * (i - m - m - n + 3)
            else:
                i -= m + n - 1 + m - 1 + n - 1 - 1
                return next(i, reduce_board(board))
            # print(f"i: {i}, x: {x}, y: {y}")
            return board[y][x]
        
        def reduce_board(board):
            new_board = board[1:-1]
            new_board = [x[1:-1] for x in new_board]
            # print(new_board)
            return new_board

        i = 1
        ret = []
        m = len(board[0])
        n = len(board)
        
        import pprint
        pprint.pprint(board)
        # print(f"m x n: {m} x {n}")

        while i < m*n+1:
            ret.append(next(i, board))
            i += 1
        return ret

