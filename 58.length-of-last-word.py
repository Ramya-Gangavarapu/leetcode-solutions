#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        s = s.rstrip()

        
        length = 0
        in_word = False

        
        for char in reversed(s):
            if char.isalpha():
                
                length += 1
                in_word = True
            elif in_word:
                
                break

        return length

        
# @lc code=end

