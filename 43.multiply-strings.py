#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        int_num1 = int(num1)
        int_num2 = int(num2)

        
        result = int_num1 * int_num2

        
        result_str = str(result)

        return result_str

        
# @lc code=end

