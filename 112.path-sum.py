#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False  

        def checkPath(node, current_sum):
            if not node:
                return False  

            current_sum += node.val  

            if not node.left and not node.right:
                return current_sum == targetSum  

            left_result = checkPath(node.left, current_sum)
            right_result = checkPath(node.right, current_sum)

            return left_result or right_result  

        return checkPath(root, 0)

        
# @lc code=end

