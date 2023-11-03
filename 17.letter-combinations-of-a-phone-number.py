#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_to_letters = {
            '2': 'abc', '3': 'def', '4': 'ghi',
            '5': 'jkl', '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        def generate_combinations(index, current_combination):
            if index == len(digits):
                result.append(current_combination)
                return

            current_digit = digits[index]
            letters = digit_to_letters[current_digit]

            for letter in letters:
                generate_combinations(index + 1, current_combination + letter)

        result = []
        generate_combinations(0, '')

        return result


        
# @lc code=end

