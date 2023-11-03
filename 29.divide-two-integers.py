#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        
        sign = 1
        if (dividend < 0) ^ (divisor < 0):
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)

        
        result = 0
        while dividend >= divisor:
            temp_divisor = divisor
            temp_result = 1

            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                temp_result <<= 1

            dividend -= temp_divisor
            result += temp_result

        return result * sign

        
# @lc code=end

