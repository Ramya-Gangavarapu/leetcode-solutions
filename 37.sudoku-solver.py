#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def is_valid(num, row, col):
            # Check if 'num' is valid in the current row and column
            for i in range(9):
                if board[i][col] == num or board[row][i] == num:
                    return False

            # Check if 'num' is valid in the current 3x3 subgrid
            row_start, col_start = 3 * (row // 3), 3 * (col // 3)
            for i in range(row_start, row_start + 3):
                for j in range(col_start, col_start + 3):
                    if board[i][j] == num:
                        return False

            return True

        def solve():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for num in map(str, range(1, 10)):
                            if is_valid(num, row, col):
                                board[row][col] = num
                                if solve():
                                    return True
                                board[row][col] = "."
                        return False
            return True

        solve()






        
# @lc code=end

