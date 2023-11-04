#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(board, row, col):
            # Check if no queens threaten the current position
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
                left_col = col - (row - i)
                right_col = col + (row - i)
                if 0 <= left_col < n and board[i][left_col] == 'Q':
                    return False
                if 0 <= right_col < n and board[i][right_col] == 'Q':
                    return False
            return True

        def solve(row):
            if row == n:
                result.append([''.join(row) for row in board])
                return

            for col in range(n):
                if is_safe(board, row, col):
                    board[row][col] = 'Q'
                    solve(row + 1)
                    board[row][col] = '.'

        result = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        solve(0)
        return result

        
# @lc code=end

