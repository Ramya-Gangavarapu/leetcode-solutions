#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_len = len(words[0])
        total_len = word_len * len(words)
        word_count = Counter(words)
        result = []

        for i in range(word_len):
            left = i
            right = i
            current_count = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    current_count[word] += 1

                    while current_count[word] > word_count[word]:
                        removed_word = s[left:left + word_len]
                        current_count[removed_word] -= 1
                        left += word_len

                    if right - left == total_len:
                        result.append(left)

                else:
                    current_count.clear()
                    left = right

        return result

        
# @lc code=end

