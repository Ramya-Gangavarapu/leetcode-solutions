#
# @lc app=leetcode id=2833 lang=python3
#
# [2833] Furthest Point From Origin
#

# @lc code=start
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        x, y = 0, 0  # Initial position at the origin (0, 0)
        max_distance = 0  # Variable to track the furthest distance

        # Loop through each move in the input string
        for move in moves:
            if move == 'U':
                y += 1
            elif move == 'D':
                y -= 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1

            # Calculate the squared distance from the origin
            distance = x * x + y * y

            # Update the furthest distance if the current distance is greater
            max_distance = max(max_distance, distance)

        return max_distance
# @lc code=end

