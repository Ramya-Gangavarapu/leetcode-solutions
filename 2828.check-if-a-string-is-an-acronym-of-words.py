#
# @lc app=leetcode id=2828 lang=python3
#
# [2828] Check if a String Is an Acronym of Words
#

# @lc code=start
from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        
        if len(words) != len(s):
            return False

        for i in range(len(words)):
            
            if words[i][0] != s[i]:
                return False

        return True

        
# @lc code=end

