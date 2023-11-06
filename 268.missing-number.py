#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = (n * (n + 1)) // 2  # Sum of the first n natural numbers
        actual_sum = sum(nums)  # Sum of the given numbers
        return expected_sum - actual_sum

        
# @lc code=end

