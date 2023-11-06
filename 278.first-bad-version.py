#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n  # Initial range of versions
        
        while left < right:
            mid = left + (right - left) // 2  # Calculate the middle version
            if isBadVersion(mid):
                right = mid  # The bad version is in the left half
            else:
                left = mid + 1  # The bad version is in the right half
        
        return left  # When left and right meet, you've found the first bad version

        
# @lc code=end

