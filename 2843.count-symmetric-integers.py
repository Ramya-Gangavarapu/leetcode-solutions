#
# @lc app=leetcode id=2843 lang=python3
#
# [2843]   Count Symmetric Integers
#

# @lc code=start
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0

        for num in range(low, high + 1):
            num_str = str(num)
            if num_str == num_str[::-1]:  # Check if the string is equal to its reverse
                count += 1

        return count

# @lc code=end

