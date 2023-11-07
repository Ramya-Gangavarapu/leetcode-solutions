#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start
class Solution:
    def countAndSay(self, n: int) -> str:
        # Base case for n = 1
        if n == 1:
            return "1"
        
        # Start with the first term
        result = "1"
        
        # Generate the next terms
        for _ in range(2, n + 1):
            next_term = ""
            count = 1
            
            for i in range(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    next_term += str(count) + result[i - 1]
                    count = 1
            
            next_term += str(count) + result[-1]
            result = next_term
        
        return result

        
# @lc code=end

