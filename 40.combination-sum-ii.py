#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        from typing import List
        def backtrack(remaining_target, start, current_combination):
            if remaining_target == 0:
                result.append(current_combination[:])
                return
            if remaining_target < 0:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue  # Skip duplicates to avoid duplicates in combinations
                current_combination.append(candidates[i])
                backtrack(remaining_target - candidates[i], i + 1, current_combination)
                current_combination.pop()

        candidates.sort()  # Sort the candidates to easily skip duplicates
        result = []
        backtrack(target, 0, [])
        return result

        
# @lc code=end

