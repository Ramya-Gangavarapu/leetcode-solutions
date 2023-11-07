#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0):
            if first == n:
                result.append(nums[:])
                return

            used = set()
            for i in range(first, n):
                if nums[i] in used:
                    continue  
                used.add(nums[i])
                
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first] 

        n = len(nums)
        result = []
        backtrack()
        return result

        
# @lc code=end

