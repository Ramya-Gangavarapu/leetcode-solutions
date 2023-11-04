#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        factorial = [1]  # Precompute factorials from 0! to (n-1)!
        for i in range(1, n):
            factorial.append(factorial[-1] * i)

        numbers = list(map(str, range(1, n + 1)))
        k -= 1  # Convert to 0-based index
        result = []

        for i in range(n - 1, -1, -1):
            index = k // factorial[i]
            result.append(numbers.pop(index))
            k %= factorial[i]

        return ''.join(result)



        
# @lc code=end

