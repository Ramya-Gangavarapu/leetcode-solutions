#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(partial, open_count, close_count):
            if len(partial) == 2 * n:
                result.append(partial)
                return
            if open_count < n:
                generate(partial + '(', open_count + 1, close_count)
            if close_count < open_count:
                generate(partial + ')', open_count, close_count + 1)

        result = []
        generate('', 0, 0)
        return result

        
# @lc code=end

