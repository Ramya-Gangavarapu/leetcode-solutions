#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
import re
class Solution:
    def isNumber(self, s: str) -> bool:

        
        pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        
        
        match = re.match(pattern, s)
        
        return match is not None




# @lc code=end

