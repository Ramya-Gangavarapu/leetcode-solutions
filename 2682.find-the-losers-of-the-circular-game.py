#
# @lc app=leetcode id=2682 lang=python3
#
# [2682] Find the Losers of the Circular Game
#

# @lc code=start
class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        players = list(range(1, n + 1))
        losers = []

        current_idx = 0
        while len(players) > 1:
            current_idx = (current_idx + k - 1) % len(players)
            losers.append(players.pop(current_idx))

        return losers

        
# @lc code=end

