#
# @lc app=leetcode id=2848 lang=python3
#
# [2848] Points That Intersect With Cars
#

# @lc code=start
class Solution:
    def numberOfPoints(self, nums: List[List[int]) -> int:
        # Create a list to store the covered range
        covered_range = []

        for start, end in nums:
            # Extend the covered range to include the current car's interval
            covered_range.extend(range(start, end + 1))

        # Use a set to remove duplicates and return the count of unique points
        unique_points = set(covered_range)
        return len(unique_points)


        
# @lc code=end

