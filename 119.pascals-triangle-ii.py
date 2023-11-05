#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex < 0:
            return []
        
       
        row = [1]

        for i in range(rowIndex):
            
            next_row = [1]
            for j in range(1, len(row)):
                next_row.append(row[j - 1] + row[j])
            next_row.append(1)
            
            row = next_row  

        return row

        
# @lc code=end

