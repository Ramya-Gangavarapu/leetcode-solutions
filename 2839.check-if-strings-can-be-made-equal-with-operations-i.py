#
# @lc app=leetcode id=2839 lang=python3
#
# [2839] Check if Strings Can be Made Equal With Operations I
#

# @lc code=start
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        count_s1 = {}
        count_s2 = {}

        
        for char in s1:
            count_s1[char] = count_s1.get(char, 0) + 1

        
        for char in s2:
            count_s2[char] = count_s2.get(char, 0) + 1

        
        return count_s1 == count_s2

        
# @lc code=end

