#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkHeight(node):
            if not node:
                return 0  # The height of an empty tree is 0.

            left_height = checkHeight(node.left)
            if left_height == -1:
                return -1  # Left subtree is unbalanced.

            right_height = checkHeight(node.right)
            if right_height == -1:
                return -1  # Right subtree is unbalanced.

            if abs(left_height - right_height) > 1:
                return -1  # Tree is unbalanced.

            return 1 + max(left_height, right_height)

        return checkHeight(root) != -1

        
# @lc code=end

