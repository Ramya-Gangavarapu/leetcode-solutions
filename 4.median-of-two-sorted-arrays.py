#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        n = len(merged)
        
        if n % 2 == 1:
            # Odd number of elements
            return float(merged[n // 2])
        else:
            # Even number of elements
            middle1 = merged[n // 2]
            middle2 = merged[n // 2 - 1]
            return (middle1 + middle2) / 2.0

        
# @lc code=end

