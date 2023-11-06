#
# @lc app=leetcode id=2855 lang=python3
#
# [2855] Minimum Right Shifts to Sort the Array
#

# @lc code=start
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        shifts = 0

        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                shifts += 1

        return shifts

        
# @lc code=end

